
from re import match
from typing import Match, ValuesView


Horazontal = 0
Depth = 0
aim = 0

with open('C:\projects\Advent_of_code\Day_Two\input.txt') as f:
    file = f.readlines()
    for line in file:
        values  = line.split(' ')
        direction = values[0]
        ammount = int(values[1])
        if direction == "forward":
            Horazontal += ammount
            Depth += aim*ammount
        elif direction == "down":
            aim += ammount
        else:
            aim -= ammount
print(Horazontal*Depth)