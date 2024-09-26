class GolfCourse:
    def __init__(self,num_holes):
        self.num_holes = num_holes
        self.course_state = [0 for hole in range(num_holes)]

    def progress_group(self, group_num):
        current_hole = self.course_state.index(group_num)
        if current_hole == self.num_holes - 1:
            self.course_state[current_hole] = 0

        if self.course_state[current_hole+1] == 0:
            self.course_state[current_hole + 1] = group_num
            self.course_state[current_hole] = 0

