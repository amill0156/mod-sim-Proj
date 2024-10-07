from itertools import count

import golf_course
#import mod_sim
class CourseOperator:
    def __init__(self, cart_condition, group_status):
        self.cart_condition = cart_condition
        self.group_status = group_status

    def get_par_wait_time(self, hole_number):
        pass

    def detect_slow(self, wait_time):
        par_3_standard = 12
        par_4_standard = 14
        par_5_standard = 18
        p3_wait_time = mod_sim.ModSim.get_par_wait_time(hole_number=3)
        p4_wait_time = mod_sim.ModSim.get_par_wait_time(hole_number=2)
        p5_wait_time = mod_sim.ModSim.get_par_wait_time(hole_number=1)
        if p3_wait_time > par_3_standard:
            wait_extra = wait_time - par_3_standard
            count(wait_extra)
        if p4_wait_time > par_4_standard:
            wait_extra = wait_time - par_4_standard
            count(wait_extra)
        if p5_wait_time > par_5_standard:
            wait_extra = wait_time - par_5_standard
            count(wait_extra)
        return count

    def send_marshall(self, count):
        period_limit = 5
        if count > period_limit:
            for ind_min in period_limit:
                period_limit -= ind_min
            return ind_min