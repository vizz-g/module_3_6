data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure, nums=0, strings=0):

    for item in structure:

        if isinstance(item, str):
            nums += len(item)
        elif isinstance(item, int):
            nums += item
        elif isinstance(item, list):

            for lst in item:
                if isinstance(lst, int):
                    nums += lst
                elif isinstance(lst, str):
                    nums += len(lst)
                else:
                    nums, strings = calculate_structure_sum([lst], nums, strings)


        elif isinstance(item, dict):

            for key in item:
                value = item[key]

                if isinstance(key, str):
                    nums += len(key)
                if isinstance(value, int):
                    nums += value
                elif isinstance(value, str):
                    nums += len(value)

        elif isinstance(item, set):

            for st in item:

                if isinstance(st, int):
                    nums += st
                elif isinstance(st, str):
                    nums += len(st)
                else:
                    nums, strings = calculate_structure_sum([st], nums, strings)

        elif isinstance(item, tuple):

            for tup in item:

                if isinstance(tup, int):
                    nums += tup
                elif isinstance(tup, str):
                    nums += len(tup)
                else:
                    nums, strings = calculate_structure_sum([tup], nums, strings)

            strings += 1

        else:
            continue

    return nums, strings


nums, strings = calculate_structure_sum(data_structure)
print(f"Всего цифр: {nums}",f"Всего строк: {strings}")