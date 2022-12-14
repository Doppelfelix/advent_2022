import numpy as np
from typing import List, Tuple

with open("input_14.txt", "r") as file:
    input = file.read()


def parse_map(input: str) -> List[list]:
    sand_start = (0, 500)

    waterfall_map = np.full([200, 700], ".")
    waterfall_map[sand_start] = "+"

    for line in input.split("\n"):
        points_in_line = line.split(" -> ")
        for start, stop in zip(points_in_line, points_in_line[1:]):
            start_y, start_x = eval(start)
            stop_y, stop_x = eval(stop)

            if start_x == stop_x:
                params = sorted((start_y, stop_y))
                tmp_slice = slice(params[0], params[1] + 1)
                draw_ags = (start_x, tmp_slice)
            else:
                params = sorted((start_x, stop_x))
                tmp_slice = slice(params[0], params[1] + 1)
                draw_ags = (tmp_slice, start_y)

            waterfall_map[draw_ags] = "X"
    return waterfall_map


def insert_sand(
    waterfall_map: np.array, start_sand: Tuple[int]
) -> Tuple[np.array, bool]:
    max_fall = 199
    current_y, current_x = start_sand

    for i in range(max_fall):
        # directly down
        if waterfall_map[current_y + 1, current_x] == ".":
            current_y += 1

        # diagonal left
        elif waterfall_map[current_y + 1, current_x - 1] == ".":
            current_x -= 1
            current_y += 1

        # diagonal right

        elif (
            waterfall_map[
                current_y + 1,
                current_x + 1,
            ]
            == "."
        ):
            current_x += 1
            current_y += 1

        # nowhere to go
        else:
            waterfall_map[current_y, current_x] = "o"
            return waterfall_map, False

    return waterfall_map, True


def part_1(input: str):
    waterfall_map = parse_map(input=input)
    for i in range(5000):
        waterfall_map, keeps_falling = insert_sand(waterfall_map, (0, 500))
        if keeps_falling:
            print(i)
            break


def part_2(input: str):
    waterfall_map = parse_map(input=input)
    max_row = 0
    for row_index, row in enumerate(waterfall_map):
        if "X" in row:
            max_row = row_index
    waterfall_map[max_row + 2, :] = "X"

    for i in range(50000):
        waterfall_map, keeps_falling = insert_sand(waterfall_map, (0, 500))
        if waterfall_map[0, 500] == "o":
            print(i + 1)
            break


part_1(input)
part_2(input)
