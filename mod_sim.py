import simpy
import sched
import time
import random

import hole_queue
from golf_course import GolfCourse
from course_operator import CourseOperator
from clubhouse import Clubhouse
from hole_queue import HoleQueue

carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
taken_carts = []

clubhouse = Clubhouse(carts, taken_carts)
class ModSim:
    def main(self):
        print("Hello and welcome to Miller's Landing Golf and Country Club!")
        print("We're glad you're here!")
        golf_course = GolfCourse(20)
        print(golf_course.course_state)


    def cart_recieve(self):

        tee_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

        for group_num in tee_times:
            print("\nPlease type '+' to receive group " + str(group_num) + "'s carts:")
            user_input = input()
            if user_input == '+':
                # taken_carts = random.sample(list(carts), k=2)
                carts_to_take = clubhouse.carts[:2]
                print("Carts taken:")
                for cart in carts_to_take:
                    print(cart)
                    clubhouse.remove_cart(cart)
                print("Carts removed from barn:")
                print(clubhouse.taken_carts)
                print("Carts available:")
                print(clubhouse.carts)
                print("\nGroup " + str(group_num) + " has been sent off with their carts.")
                if group_num == 26:
                    print("\nAll groups have been sent off and are on the golf course.")
                    #queue_carts()
            else:
                print("Please return to pro shop for assistance.")
                break

    #hole_queue.HoleQueue()
    def cart_return(self):
        taken_carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                       28, 29,
                       30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
        carts = []
        clubhouse = Clubhouse(carts, taken_carts)
        tee_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

        for group_num in tee_times:
            clubhouse.add_cart(clubhouse.taken_carts[0])
            clubhouse.add_cart(clubhouse.taken_carts[0])

            print("Carts taken:")
            print(clubhouse.taken_carts)
            print("Carts available:")
            print(clubhouse.carts)


    if __name__ == "__main__":
        main()
        cart_recieve()
        # cart_return()
        # holes()
