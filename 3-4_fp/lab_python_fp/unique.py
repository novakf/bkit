# Итератор для удаления дубликатов
'''
class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        copy_items = [item for item in items]

        if ignore_case:
            lower_items = [item.lower() for item in copy_items]
            self.uniq_items = set(lower_items)
        else:
            self.uniq_items = set(copy_items)

    def __iter__(self):
        return (item for item in self.uniq_items)

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

for item in Unique(data1, True):
    print(item)
'''


class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        if ignore_case == True:
            copy_items = [item for item in items]
            lower_items = [item.lower() for item in copy_items]
            self.all_items = iter(lower_items)
        else: 
            self.all_items = iter(items)

        self.uniq_items = set()
        self.ignore_case = ignore_case

    def __next__(self):
        while True:
            next_item = next(self.all_items)
            if next_item not in self.uniq_items:
                self.uniq_items.add(next_item)
                return next_item

    def __iter__(self):
        return self

'''
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

for item in Unique(data):
    print(item)

for item in Unique(data1, True):
    print(item)
'''
