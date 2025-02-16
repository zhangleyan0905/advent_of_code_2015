with open('input/day_03.txt', 'r') as file_object:
    input_text = file_object.read()
x,y = 0,0
visited_house=set()
visited_house.add((x,y))

for char in input_text:
    if char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    elif char == '>':
        x += 1
    elif char == '<':
        x -= 1
    visited_house.add((x,y))

print(len(visited_house))
