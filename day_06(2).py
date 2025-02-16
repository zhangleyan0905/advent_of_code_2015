lights = [[0] * 1000 for _ in range(1000)]
with open('input/day_06.txt', 'r') as file_object:
    instructions = file_object.readlines()
for instruction in instructions:
    parts = instruction.strip().split(' ')
    if parts[0] == 'turn':
        action = parts[1]
        start = parts[2].split(',')
        end = parts[4].split(',')
        start_x, start_y = int(start[0]), int(start[1])
        end_x, end_y = int(end[0]), int(end[1])
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == 'on':
                    lights[x][y] += 1
                else:
                    lights[x][y] =max(0, lights[x][y] - 1)
    elif parts[0] == 'toggle':
        start = parts[1].split(',')
        end = parts[3].split(',')
        start_x, start_y = int(start[0]), int(start[1])
        end_x, end_y = int(end[0]), int(end[1])
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                lights[x][y] += 2
total_brightness = 0
for row in lights:
    for light in row:
        total_brightness += light
print(total_brightness)