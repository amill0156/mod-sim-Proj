import simpy
import random
from clubhouse import Clubhouse
from hole_par import HolePar
from golf_course import GolfCourse
from course_operator import CourseOperator

carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
taken_carts = []

clubhouse = Clubhouse(carts, taken_carts)
hole_par = HolePar()


class ModSim:
    def __init__(self, env):
        self.env = env
        self.course_operator = CourseOperator()

    def main(self):
        print("Hello and welcome to Miller's Landing Golf and Country Club!")
        print("We're glad you're here!")
        print("When you're ready, grab a cart and take off!")

    def get_par_wait_time(self, hole_number):
        if hole_number in [3, 6, 13, 16]:  # Par 3 holes
            return hole_par.par_3()
        elif hole_number in [2, 4, 5, 7, 9, 10, 11, 12, 14, 17]:  # Par 4 holes
            return hole_par.par_4()
        else:  # Par 5 holes (holes 1, 8, 15, 18)
            return hole_par.par_5()

    def get_standard_time(self, hole_number):
        if hole_number in [3, 6, 13, 16]:  # Par 3 holes
            return 12
        elif hole_number in [2, 4, 5, 7, 9, 10, 11, 12, 14, 17]:  # Par 4 holes
            return 14
        else:  # Par 5 holes (holes 1, 8, 15, 18)
            return 18

    def play_hole(self, env, cart, hole_number, wait_time):
        standard_time = self.get_standard_time(hole_number)
        print(f"Cart {cart} is starting hole {hole_number} at time {env.now}. Par wait time: {wait_time} minutes.")
        yield env.timeout(wait_time)  # Simulate time taken to complete the hole
        print(f"Cart {cart} has finished hole {hole_number} at time {env.now} after {wait_time} minutes.")

        actual_wait_time = wait_time
        self.course_operator.detect_slow(cart, hole_number, actual_wait_time, standard_time)

    def send_cart_to_course(self, env, cart, wait_times):
        for hole_number in range(1, 19):  # Loop through all 18 holes
            yield env.process(self.play_hole(env, cart, hole_number, wait_times[hole_number-1]))  # Process each hole one by one

        print(f"Group {cart} has completed the course at time {env.now}.")

    def cart_recieve(self, env):
        tee_times = list(range(1, 14))
        group_start_delay = 10  # Delay of 10 time units between each group

        for group_num in tee_times:
            wait_times = [self.get_par_wait_time(hole_number) for hole_number in range(1, 19)]
            print(f"\nGroup {group_num} is about to go off at time {env.now}...")
            carts_to_take = clubhouse.carts[:2]
            for cart in carts_to_take:
                clubhouse.remove_cart(cart)
                env.process(self.send_cart_to_course(env, cart, wait_times))  # Start each cart process concurrently

            yield env.timeout(group_start_delay)  # Stagger group starts

            #print(f"Group {group_num} has been sent off with their carts at time {env.now}.")

    def cart_return(self):
        print(f"\nCarts are returning to the clubhouse at time {self.env.now}...")
        while clubhouse.taken_carts:
            clubhouse.add_cart(clubhouse.taken_carts[0])  # Return the first cart
            print(f"Returning cart. Available carts: {clubhouse.carts}. Taken carts: {clubhouse.taken_carts}")


if __name__ == "__main__":
    env = simpy.Environment()
    modsim = ModSim(env)
    modsim.main()

    env.process(modsim.cart_recieve(env))

    env.run(until=500)