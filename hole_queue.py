import queue
import time
import clubhouse
from hole_par import HolePar
import threading

carts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

class HoleQueue:
    holes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


    def __init__(self):
        self.hole_q = queue.Queue()

    def start_hole(self, cart, wait):
        def next_hole_wait():
            time.sleep(wait)
            self.hole_q.put(cart)
            print(f"Cart {cart} sent to next hole. It took them {wait} minutes to get there.")

    def show_group(self):
        return self.hole_q.get()

time_nh = HoleQueue()

# for loop looping through carts, run time_nh.start_hole on each cart
for cart in carts:
    time_nh.start_hole(cart)
    while not time_nh.hole_q.empty():

# while loop checking time_nh.hole_queue not empty


