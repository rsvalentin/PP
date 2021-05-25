import functools
import operator


def log(message, subsystem):
    print("{}: {}".format(subsystem, message))


class Cell:
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = functools.partialmethod(set_state, True)
    set_dead = functools.partialmethod(set_state, True)


if __name__ == '__main__':
    ''' functools.partial(func, *args, **kwargs) -> returneaza un nou obiect
    partial care se va comporta ca o functie cand va fi apelat. Functia permite
    adaugarea unor argumente cu o valoare implicita'''
    server_log = functools.partial(log, subsystem='server')
    server_log("whatever")

    ''' functools.partialmethod(func, *args, **kwargs) -> similar cu functia partial, doar
    ca e specifica pentru metodele dintr-o clasa'''
    cell = Cell()
    cell.set_alive()
    print(cell.alive)  # @property -> nu mai trebuie apelata (e proprietate)

    ''' functools.reduce(func, iter, [initial_value]) -> efectueaza cumulativ o operatie
    pe toate elementele din iterabil (nu poate fi aplicat pe iteratori infiniti)
    Argumentul func este o functie care primeste doua elemente si calculeaza func(A, B)'''
    functools.reduce(operator.concat, ['A', 'BC', 'DEF', 'G'])  # ABCDEFG
    # exemplu echivalent cu: ''.join(['A', 'BC', 'DEF', 'G'])
    functools.reduce(operator.mul, [1, 2, 3], 1)  # 6 (factorial)
    functools.reduce(operator.add, [1, 2, 3, 4], 0)  # 10