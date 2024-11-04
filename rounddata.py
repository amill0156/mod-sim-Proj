from datetime import timedelta

file_paths = ['coursedata.txt', 'coursedata2.txt', 'coursedata3.txt', 'coursedata4.txt', 'coursedata5.txt',
              'coursedata6.txt', 'coursedata7.txt', 'coursedata8.txt', 'coursedata9.txt',
              'coursedata10.txt']

for file_path in file_paths:
    group_times = {}
    with open(file_path, 'r') as file:
        for line in file:
            if "Group" in line and "teeing off at time" in line:
                parts = line.split()
                group_id = parts[1]
                start_time = int(parts[-1].replace("...", ""))
                if group_id not in group_times:
                    group_times[group_id] = {'start': start_time, 'end_cart_1': None, 'end_cart_2': None}

            elif "Cart" in line and "finished hole 18" in line:
                parts = line.split()

                after_index = parts.index("after")
                end_time = int(parts[after_index - 1])

                cart_id = parts[1]
                group_id = str((int(cart_id) + 1) // 2)

                if group_id in group_times:
                    if group_times[group_id]['end_cart_1'] is None:
                        group_times[group_id]['end_cart_1'] = end_time
                    elif group_times[group_id]['end_cart_2'] is None:
                        group_times[group_id]['end_cart_2'] = end_time

    for group, times in group_times.items():
        if times['end_cart_1'] is not None and times['end_cart_2'] is not None and times['start'] is not None:
            finish_time = max(times['end_cart_1'], times['end_cart_2'])
            total_time = timedelta(minutes=finish_time - times['start'])
            print(f"Group {group} total time to complete the course: {total_time}")