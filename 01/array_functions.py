import random

def is_ordered(l, function=lambda x, y: x <= y):
    collection = list(l)
    return all(function(collection[i], collection[i + 1]) for i in range(len(collection) - 1))


def ordered_insertion(elements, element, function=lambda x, y: x <= y):
    for i in range(len(elements)):
        if not function(elements[i], element):
            elements.insert(i, element)
            return
    elements.append(element)

def insertion_sort(elements, function=lambda x, y: x <= y):
    inner_list = list();
    for e in elements:
        ordered_insertion(inner_list, e, function)
    return inner_list


comparer = lambda x, y: x >= y

l = list()
[l.append(random.randint(0,100000)) for _ in range(2000000000)]

for x in insertion_sort(l):
    print(x)

#print(merge_sort(range(1,10)))