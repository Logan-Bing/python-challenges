
def is_colorful(num):
    nums_sets = set()

    # Add single number to nums_sets
    str_num = str(num)
    nums_sets.update(str_num)

    # Add first_sequence
    first_sequence = int(str_num[0]) * int(str_num[1])
    nums_sets.add(str(first_sequence))

    # Add second_sequence
    second_sequence = int(str_num[1]) * int(str_num[2])
    nums_sets.add(str(second_sequence))

    # Add third_sequence
    third_sequence = int(str_num[0]) * int(str_num[1]) * int(str_num[2])
    nums_sets.add(str(third_sequence))

    # Check if is colorful
    return "This is a colorful number" if len(nums_sets) == 6 else "This is not a colorful number"


print(is_colorful(263))
print(is_colorful(236))
