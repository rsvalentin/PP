import random


class A:
    pass


if __name__ == '__main__':
    all([True, True, False, True])  # False
    all([A(), A(), None])  # False
    all([A(), A()])  # True
    all([True] * 4)  # True
    any([False, True, False, False])  # True
    any([False] * 4)  # False

    min([5, 84, 17, 2, 20, 3, -9, 11, 7])  # -9
    max([5, 84, 17, 2, 20, 3, -9, 11, 7])  # 84

    list(reversed([1, 2, 3, 4]))  # [4, 3, 2, 1]
    ''.join(list(reversed('abcd')))  # dcba

    sum([1, 2, 3, 4])  # 10

    ''' sort vs sorted:
    sort modifica variabila
    sorted returneaza o noua colectie sortata'''
    my_list = [-9, 2, 3, 5, 7, 11, 17, 20, 84]
    my_dict = {1: (1, 43), 2: (5, 12), 3: (3, 36)}
    sorted(my_list)  # [-9, 2, 3, 5, 7, 11, 17, 20, 84]
    my_list.sort()  # my_list = [-9, 2, 3, 5, 7, 11, 17, 20, 84]
    sorted(my_list, reverse=True)  # [84, 20, 17, 11, 7, 5, 3, 2, -9]

    # sortare dictionar dupa valoare:
    {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    # sortare dictionar dupa primul element din tupla (valoare)
    {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1][0])}

    list0 = list(range(5))
    list1 = list('abcdefghi')
    for item in zip(list0, list1):
        print(item)  # (0, 'a'), (1, 'b'), (2, 'c'), (4, 'd')
    # sau:
    for first, second in zip(list0, list1):
        print(first, second)  # 0 a, 1 b, 2 c, 4 d

    # slice(start, end, step) -> implicit, step=1
    print(list0[0:4])  # sau print(list0[:4])  # sau print(list0[slice(0, 4)])
    print(list0[-1])  # ultimul element

    # set comprehension:
    {random.randint(1, 10) for _ in range(15)}  # set de numere intregi distincte

    # list comprehension:
    [item for item in range(15) if item % 2 == 0]  # [0, 2, 4, ..., 14]

    # dict comprehension:
    {n: n ** 2 for n in range(10)}  # dictionar cu patratele perfecte pana la 81

    # generator comprehension:
    (n ** 2 for n in range(10))  # generator([0, 1, 4, 9, ..., 81])

    # filter
    filter(lambda x: x % 2 == 0 and x > 5, range(20))  # 6, 8, 10, 12, 14, 16, 18

    # map
    map(lambda x: (x + 1) * (x + 1), range(10))  # (x+1)^2 for x in range(10)