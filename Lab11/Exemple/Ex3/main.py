import multiprocessing


class ProcesTest(multiprocessing.Process):      # functia de crearea unui proces intr-o subclasa
    def run(self):
        print(f'am apelat metoda run() in procesul: {self.name}')
        return


if __name__ == '__main__':
    jobs = []               # array unde vor fi adaugate procesele
    for i in range(5):
        p = ProcesTest()   # se creeaza 5 procese apelandu-se functia de mai sus afisandu-se mesajul coresp.
        jobs.append(p)     # se adauga in array apoi se inchid procesele
        p.start()
        p.join()