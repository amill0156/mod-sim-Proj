import threading
import queue
import time
import clubhouse
from hole_par import HolePar
from mod_sim import ModSim


class HoleQueue:
    holes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    def __init__(self):
        self.hole_q = queue.Queue()
        self.hole_end = threading.Lock()

    def start_hole(self, cart, wait):
        def next_hole_wait():
            time.sleep(wait)
            with self.hole_end:
                self.hole_q.put(cart)
                print(f"Cart {cart} sent to next hole. It took them {wait} minutes to get there.")

        threading.Thread(target=next_hole_wait()).start()

    def show_group(self):
        return self.hole_q.get()


time_nh = HoleQueue()

# Starting the holes by their numbers and using their par numbers from hole_par to queue them in
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_5(HoleQueue.holes[1]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[2]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_3(HoleQueue.holes[3]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[4]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[5]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_3(HoleQueue.holes[6]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[7]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_5(HoleQueue.holes[8]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[9]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[10]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[11]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[12]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_3(HoleQueue.holes[13]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[14]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_5(HoleQueue.holes[15]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_3(HoleQueue.holes[16]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_4(HoleQueue.holes[17]))
time_nh.start_hole(ModSim.cart_recieve(clubhouse), HolePar.par_5(HoleQueue.holes[18]))

