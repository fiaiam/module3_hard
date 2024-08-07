data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def count_all(data_structure):
    sum_ = 0
    if isinstance(data_structure, str):
        sum_ += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        sum_ += data_structure
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            sum_ += count_all(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_ += count_all(key)
            sum_ += count_all(value)
    return sum_

final = count_all(data_structure)
print(final)