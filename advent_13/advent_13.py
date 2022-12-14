from itertools import zip_longest
from random import randint

with open("input_13.txt", "r") as file:
    input = file.read()


def compare_lists(l1: list | int, l2: list | int) -> bool:
    both = [l1, l2]
    if all(isinstance(item, int) for item in both):
        if l1 < l2:
            return True
        else:
            return False

    l1, l2 = tuple([l] if isinstance(l, int) else l for l in both)

    for l1_v, l2_v in zip_longest(l1, l2):

        # right list run out before left
        if l1_v is not None and l2_v is None:
            return False

        # left list run out before right
        elif l1_v is None and l2_v is not None:
            return True

        # one element is still a list, recurse
        elif isinstance(l1_v, list) or isinstance(l2_v, list):
            is_correct = compare_lists(l1_v, l2_v)
            if is_correct is None:
                continue
            else:
                return is_correct
        elif l1_v is not None and l2_v is not None and l1_v < l2_v:
            return True
        elif l1_v is not None and l2_v is not None and l1_v > l2_v:
            return False


def part_1(input: str) -> int:
    total_sum = 0
    for line_index, line in enumerate(input.split("\n\n")):
        l1, l2 = line.split("\n")
        # dangerous territory
        l1 = eval(l1)
        l2 = eval(l2)
        if compare_lists(l1, l2):
            total_sum += line_index + 1

    return total_sum


def quicksort(all_lines: list) -> list:
    if len(all_lines) < 2:
        return all_lines

    low, same, high = [], [], []
    raw_pivot_line = all_lines[randint(0, len(all_lines) - 1)]

    # eval is dangerous territory!
    pivot_line = eval(raw_pivot_line)
    for line in all_lines:
        # eval is dangerous territory!
        line_parse = eval(line)

        if line_parse == pivot_line:
            same.append(line)
        elif compare_lists(line_parse, pivot_line):
            low.append(line)
        else:
            high.append(line)

    return quicksort(low) + same + quicksort(high)


def part_2(input: str) -> int:
    all_lines = input.replace("\n\n", "\n").split("\n")
    all_lines.extend(["[[2]]", "[[6]]"])
    res = quicksort(all_lines)
    return (res.index("[[2]]") + 1) * (res.index("[[6]]") + 1)


print(f"Part 1: {part_1(input)}")
print(f"Part 2: {part_2(input)}")
