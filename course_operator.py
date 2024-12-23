class CourseOperator:
    def __init__(self):
        self.group_over_limit = {}

    # Function to detect when groups are playing slow and to deploy marshal
    def detect_slow(self, group_id, hole_number, actual_wait_time, par_standard_time):
        if group_id not in self.group_over_limit:
            self.group_over_limit[group_id] = 0

        # Time difference calculation to figure how many minutes over limit the groups are
        time_over_limit = actual_wait_time - par_standard_time
        if time_over_limit > 0:
            self.group_over_limit[group_id] += 1
            print(f"Group {group_id} is over pace by {time_over_limit} minute(s) and are behind pace.")
        elif time_over_limit == 0:
            print(f"Group {group_id} stayed within the time limit of the hole.")
        else:
            self.group_over_limit[group_id] = max(0, self.group_over_limit[group_id] - 1)
            print(f"Group {group_id} has gone under the time limit and are "
                  f"ahead of pace.")

        if self.group_over_limit[group_id] >= 5:
            self.send_marshal(group_id)

    # Function to determine when a marshal is needed
    def send_marshal(self, group_id):
        self.group_over_limit[group_id] = 0
        print(f"Marshal sent to group {group_id} for slow play.")