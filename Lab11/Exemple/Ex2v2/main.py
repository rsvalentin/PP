from threading import Thread, Condition
import time
elemente = []
conditie = Condition()


class Consumator(Thread):
    def __init__(self):           # se initializeaza theadul
        Thread.__init__(self)

    def consumator(self):
        global conditie
        global elemente
        conditie.acquire()        # se incearca indeplinirea conditiei
        if len(elemente) == 0:    # daca nu sunt elemente prezente conditia e pusa pe wait si se afiseaza mesaj
            conditie.wait()
            print('mesaj de la consumator: nu am nimic disponibil')
        elemente.pop()            # altfel dam pop elementului si afisam mesaj
        print('mesaj de la consumator : am utlizat un element')
        print('mesaj de la consumator : mai am disponibil', len(elemente),
              'elemente')
        conditie.notify()
        conditie.release()      #  eliberam conditia

    def run(self):
        for i in range(5):
            self.consumator()      # o bucla de consumatori care incearca sa atinga conditia


class Producator(Thread):
    def __init__(self):
        Thread.__init__(self)       # apelarea constructorului pt thread

    def producator(self):
        global conditie
        global elemente
        conditie.acquire()        # se incearca indeplinirea conditiei
        if len(elemente) == 10:
            conditie.wait()
            print('mesaj de la producator : am disponibile', len(elemente),
                  'elemente')
            print('mesaj de la producator : am oprit productia')
        elemente.append(1)      # dupa indeplinirea conditiei se adauga elementul in array
        print('mesaj de la producator : am produs', len(elemente), 'elemente')
        conditie.notify()
        conditie.release()       # se elibereaza conditia

    def run(self):
        for i in range(5):
            self.producator()     # functia intra intr un loop cand e invocata


if __name__ == '__main__':
    producator = Producator()
    consumator = Consumator()
    producator.start()
    consumator.start()
    producator.join()
    consumator.join()