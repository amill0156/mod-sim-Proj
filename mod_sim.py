import simpy
import random
from clubhouse import Clubhouse
from hole_par import HolePar
from course_operator import CourseOperator

# Carts list
carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# Taken carts list
taken_carts = []

# Clubhouse class call
clubhouse = Clubhouse(carts, taken_carts)
# HolePar class call
hole_par = HolePar()

class ModSim:
    def __init__(self, env):
        self.env = env
        self.course_operator = CourseOperator()

    # Intro messages
    def main(self):
        print("Hello and welcome to Miller's Landing Golf and Country Club!")
        print("We're glad you're here!")
        print("When you're ready, grab a cart and take off!")

    # Setting the hole number config via par number
    def get_par_wait_time(self, hole_number):
        if hole_number in [3, 6, 13, 16]:  # Par 3 holes
            return hole_par.par_3()
        elif hole_number in [2, 4, 5, 7, 9, 10, 11, 12, 14, 17]:  # Par 4 holes
            return hole_par.par_4()
        else:  # Par 5 holes (holes 1, 8, 15, 18)
            return hole_par.par_5()

    # Setting the standard avg time taken to complete the hole per hole number
    def get_standard_time(self, hole_number):
        if hole_number in [3, 6, 13, 16]:  # Par 3 holes
            return 12
        elif hole_number in [2, 4, 5, 7, 9, 10, 11, 12, 14, 17]:  # Par 4 holes
            return 14
        else:  # Par 5 holes (holes 1, 8, 15, 18)
            return 18

    def play_hole(self, env, cart, group_num, hole_number, wait_time):
        # Creating a standard time variable within the function
        standard_time = self.get_standard_time(hole_number)
        # Starting the groups at whatever new hole they arrive at and showing the time taken to complete
        print(f"Cart {cart} is starting hole {hole_number} at time {env.now}. Time taken at hole: {wait_time} minutes.")
        # Simulate time taken to complete the hole
        yield env.timeout(wait_time)
        # Identifying when the group is finished at the given hole
        print(f"Cart {cart} has finished hole {hole_number} at time {env.now} after {wait_time} minutes.")

        # Actual time taken to finish the hole
        actual_wait_time = wait_time
        # Using the course_operator class to detect when a group is playing slow
        self.course_operator.detect_slow(group_num, hole_number, actual_wait_time, standard_time)

    def send_cart_to_course(self, env, cart, group_num, wait_times):
        # Loop through all 18 holes
        for hole_number in range(1, 19):
            # Using env to process the holes hone by one in the simulation
            yield env.process(self.play_hole(env, cart, group_num, hole_number,
                                             wait_times[hole_number - 1]))  # Process each hole one by one

        # Showing when carts have finished 18 and the course
        print(f"Cart {cart} has completed the course at time {env.now}.")

        # Pops carts off of taken_carts list to show the carts now being unoccupied
        clubhouse.taken_carts.pop(taken_carts.index(cart))
        # Return gap to ensure no groups return their carts at the exact same time/ finish at the same time
        return_gap = 10
        # Using env to implement that return gap via timeout
        yield env.timeout(return_gap)

        # Adding cart back to list when unoccupied
        clubhouse.add_cart(cart)
        # Print return identifier
        print(f"Cart {cart} has returned to the cart barn at time {env.now}. Available carts: {clubhouse.carts}.")

    # Cart deployment function
    def cart_recieve(self, env):
        # 26 tee times
        tee_times = list(range(1, 27))
        # Time gap between group starts
        group_start_delay = 8  # Delay of 8 time units between each group

        # Iterating through tee times using groups to deploy two carts per group to 4 golfers
        for group_num in tee_times:
            # Individual wait times for the hole numbers in the 18 hole course
            wait_times = [self.get_par_wait_time(hole_number) for hole_number in range(1, 19)]

            # Identifiers to show when groups are sent off
            print(f"Group {group_num} has been sent off with their carts.")
            print(f"Group {group_num} is teeing off at time {env.now}...")
            carts_to_take = clubhouse.carts[:2]
            # Looping to deploy carts to course
            for cart in carts_to_take:
                clubhouse.remove_cart(cart)
                # Start each cart process concurrently
                env.process(self.send_cart_to_course(env, cart, group_num, wait_times))

            # Stagger group starts
            yield env.timeout(group_start_delay)

    # Cart return function
    def cart_return(self, env):
        # Showing time stamp when carts are being returned
        print(f"Carts are returning to the cart barn at time {env.now}...")

        # Looping through to return carts back to cart barn
        while clubhouse.taken_carts:
            cart_to_return = clubhouse.taken_carts.pop(0)
            clubhouse.add_cart(cart_to_return)

            if clubhouse.taken_carts:
                yield env.timeout(5)
            print(
                f"Returning cart {cart_to_return}. Available carts: {clubhouse.carts}. Taken carts: {clubhouse.taken_carts}")

if __name__ == "__main__":
    env = simpy.Environment()
    modsim = ModSim(env)
    modsim.main()

    env.process(modsim.cart_recieve(env))

    env.run(600)