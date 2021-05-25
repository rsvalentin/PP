import os
import operator
import itertools
from collections import namedtuple

City = namedtuple('City', ['city_name', 'country_code', 'city_zip_code'])

if __name__ == '__main__':
    ''' itertools.count(start, step) -> returneaza un flux de date infinit '''
    itertools.count()  # 0, 1, 2, 3, 4, ...
    itertools.count(10)  # 10, 11, 12, 13, 14, ...
    itertools.count(10, 5)  # 10, 15, 20, 25, 30, ...

    ''' itertools.cycle(iter) -> repeta la infinit iterabilul primit'''
    itertools.cycle([1, 2, 3])  # 1, 2, 3, 1, 2, 3, 1, 2, 3, ...

    ''' itertools.repeat(elem, [n]) -> returneaza elementul primit de n ori
    (sau infinit daca n lipseste) '''
    itertools.repeat('abc')  # abc, abc, abc, abc, ...
    itertools.repeat('abc', 3)  # abc, abc, abc

    ''' itertools.accumulate(iterable[, func, *, initial=None) -> creeaza un iterator
    care returneaza sumele acumulate, sau rezultatul acumularii altor functii binare
    specificate prin argumentul func'''
    itertools.accumulate([1, 2, 3, 4, 5])  # 1, 3, 6, 10, 15
    itertools.accumulate([1, 2, 3, 4, 5], operator.mul)  # 1, 2, 6, 24, 120

    ''' itertools.chain(iterA, iterB, ...) -> primeste un numar oarecare de iteratori
    si returneaza pe rand, toate elementele iteratorilor primiti'''
    itertools.chain(['a', 'b', 'c'], (1, 2, 3))  # a, b, c, 1, 2, 3
    ''' de asemenea, se poate folosi si operatorul de despachetare:'''
    [*['a', 'b', 'c'], *(1, 2, 3)]  # ['a', 'b', 'c', 1, 2, 3]

    ''' itertools.islice(iter, [start], stop, [step]) -> returneaza un stream
    (flux de date) compus dintr-o portiune a iteratorului initial'''
    itertools.islice(range(10), 8)  # 0, 1, 2, 3, 4, 5, 6, 7
    itertools.islice(range(10), 2, 8)  # 2, 3, 4, 5, 6, 7
    itertools.islice(range(10), 2, 8, 2)  # 2, 4, 6

    ''' itertools.tee(iter, [n]) -> replica iteratorul initial in n iteratori
    independenti; implicit, n=2 (daca nu este precizat)'''
    itertools.tee(itertools.repeat('abc', 5))  # (iter1, iter2)
    itertools.tee(itertools.repeat('abc', 5), 3)  # (iter1, iter2, iter3)

    ''' itertools.zip_longest(*iterables, fillvalue=None) -> creeaza un iterator
    compus din tuple cu cate un element din fiecare iterabil'''
    itertools.zip_longest('ABCD', 'xy', fillvalue='-')
    # ('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')

    ''' itertools.starmap(func, iter) -> primeste un iterator care va fi un stream
    de tuple si apeleaza func folosind elementele din tupla ca argumente'''
    itertools.starmap(os.path.join, [('/bin', 'python'),
                                     ('/usr', 'bin', 'java'),
                                     ('/usr', 'bin', 'perl'),
                                     ('/usr', 'bin', 'ruby')])
    # /bin/python, /usr/bin/java, /usr/bin/perl, /usr/bin/ruby
    itertools.starmap(operator.add, zip([1, 2, 3], [4, 5, 6]))  # 5, 7, 9

    ''' itertools.filterfalse(predicate, iter) -> opusul functiei filter, returneaza
    elementele pentru care predicatul returneaza False'''
    itertools.filterfalse(lambda x: x % 2 == 0, list(range(10)))  # 1, 3, 5, 7, 9
    # echivalent cu:
    filter(lambda x: x % 2 != 0, list(range(10)))

    ''' itertools.takewhile(predicate, iter) -> returneaza elemente cat timp predicatul
    returneaza True'''
    itertools.takewhile(lambda x: x < 5, itertools.count())  # 0, 1, 2, 3, 4
    itertools.takewhile(lambda x: x % 2 == 0, itertools.count())  # 0

    ''' itertools.dropwhile(predicate, iter) -> elimina elemente cat timp predicatul
    returneaza True, dupa care returneaza restul iteratorului'''
    itertools.dropwhile(lambda x: x < 10, itertools.count())  # 10, 11, 12, ...
    itertools.dropwhile(lambda x: x % 2 == 0, itertools.count())  # 1, 2, 3, ...

    ''' itertools.compress(data, selectors) -> primeste 2 iteratori si returneaza doar
    elementele din primul iterator pentru care elementul corespunzator din al doilea
    este True'''
    itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True])  # 1, 2, 5

    # Functii combinatorice
    ''' itertools.combinations(iterable, r) -> returneaza un iterator care da
    toate tuplele de lungime r combinatii ale elementelor din iterator'''
    itertools.combinations([1, 2, 3, 4], 2)  # combinari de 4 luate cate 2
    '''(1, 2), (1, 3), (1, 4),
       (2, 3), (2, 4),
       (3, 4)'''
    itertools.combinations([1, 2, 3, 4], 3)  # combinari de 4 luate cate 3
    '''(1, 2, 3), (1, 2, 4), (1, 3, 4),
       (2, 3, 4)'''

    ''' itertools.combinations_with_replacement(iterable, r) -> spre deosebire de
    functia itertools.combinations. elementele se pot repeta in aceeasi tupla'''
    itertools.combinations_with_replacement([1, 2, 3, 4], 2)
    '''(1, 1), (1, 2), (1, 3), (1, 4),
       (2, 2), (2, 3), (2, 4),
       (3, 3), (3, 4),
       (4, 4)'''

    ''' itertools.permutations(iterable, r=None) -> returneaza toate aranjamentele
    de lungime r'''
    itertools.permutations([1, 2, 3, 4], 2)  # aranjamente de 4 luate cate 2
    '''(1, 2), (1, 3), (1, 4),
       (2, 1), (2, 3), (2, 4),
       (3, 1), (3, 2), (3, 4),
       (4, 1), (4, 2), (4, 3)'''
    itertools.permutations(([1, 2, 3]))
    # (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

    # Gruparea elementelor
    City = namedtuple('City', ['city_name', 'country_code', 'city_zip_code'])
    city_list = [City(city_name='Iasi', country_code='RO', city_zip_code=100),
                 City('Bucuresti', 'RO', 200),
                 City('Cluj', 'RO', 300),
                 City('Paris', 'FR', 1100),
                 City('Lyon', 'FR', 1200),
                 City('Copenhagen', 'DK', 2100)]

    ''' itertools.groupby(iter, key_func=None) -> colecteaza toate elementele consecutive
    din iterator care au aceeasi cheie si returneaza un stream de tuple cu 2 elemente:
    cheia si un iterator cu elementele corespunzatoare cheii'''
    itertools.groupby(city_list, lambda city: city.country_code)
    # echivalent cu:
    itertools.groupby(city_list, lambda city: city[1])
    ''' ('RO', iterator-1), unde iterator-1 este:
                City(city_name='Iasi', country_code='RO', city_zip_code=100)
                City(city_name='Bucuresti', country_code='RO', city_zip_code=200)
                City(city_name='Cluj', country_code='RO', city_zip_code=300)
        ('FR', iterator-2), unde iterator-2 este:
                City(city_name='Paris', country_code='FR', city_zip_code=1100)
                City(city_name='Lyon', country_code='FR', city_zip_code=1200)
        ('DK', iterator-3), unde iterator-3 este:
                City(city_name='Copenhagen', country_code='DK', city_zip_code=2100)'''