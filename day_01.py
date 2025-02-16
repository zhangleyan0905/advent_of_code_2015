with open('input/day_01.txt', 'r') as file_object:
    input_text = file_object.read()

floor = 0
for char in input_text:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print(floor)