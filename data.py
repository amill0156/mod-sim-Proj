import pandas as pd
import re

file_paths = ['coursedata.txt', 'coursedata2.txt', 'coursedata3.txt', 'coursedata4.txt', 'coursedata5.txt', 'coursedata6.txt', 'coursedata7.txt', 'coursedata8.txt', 'coursedata9.txt', 'coursedata10.txt']

marshal_count = 0
ahead_count = 0
behind_count = 0

for file_path in file_paths:
    with open(file_path, 'r') as file:
        content = file.read()
        marshal_count += len(re.findall(r"Marshal sent", content))
        ahead_count += len(re.findall(r"ahead of pace", content))
        behind_count += len(re.findall(r"behind pace", content))
        print(marshal_count)
        print(ahead_count)
        print(behind_count)