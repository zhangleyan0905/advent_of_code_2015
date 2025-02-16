with open('input/day_03.txt', 'r') as file_object:
    input_text = file_object.read()
x,y = 0,0
robo_x, robo_y = 0,0
visited_house=set()
visited_house.add((0,0))
for i, char in enumerate(input_text):
    if i % 2 == 0:
        if char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        elif char == '>':
            x += 1
        elif char == '<':
            x -= 1
        visited_house.add((x, y))
    else:
        if char == '^':
            robo_y += 1
        elif char == 'v':
            robo_y -= 1
        elif char == '>':
            robo_x += 1
        elif char == '<':
            robo_x -= 1
        visited_house.add((robo_x, robo_y))
print(len(visited_house))