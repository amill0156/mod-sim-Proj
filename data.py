import pandas as pd

#data = []

#with open('coursedata.txt', 'r') as file:
#    for line in file:
#        processed_line = line.strip().split()
#        data.append(processed_line)
#df = pd.DataFrame(data)
#print(df)

#def parse_line(line):
#    return line.strip().split()

#with open('coursedata.txt', 'r') as file:
#    data = [parse_line(line) for line in file]

#df = pd.DataFrame(data)
#print(df)

search_word = 'marshal'

matching_lines = []

with open('coursedata.txt', 'r') as file:
    for line in file:
        if search_word in line:
            matching_lines.append(line.strip())

df = pd.DataFrame(matching_lines, columns=['Line'])
print(df)