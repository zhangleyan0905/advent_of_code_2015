with open('input/day_01.txt', 'r') as file_object:
    input_text = file_object.read()

floor = 0
position = 0

for i in range(len(input_text)):
    char = input_text[i]
    if char == '(':
        floor = floor + 1
    else:
        floor = floor - 1

    if floor == -1 and position == 0:
        position = i + 1
print(position)