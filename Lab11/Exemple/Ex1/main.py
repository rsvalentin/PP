import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time


def countdown():
    x = 100000000
    while x > 0:
        x -= 1      # decrementeaza x cat timp x > 100000000


def ver_1():                                        # se apeleaza functia in mod pseudoparalelism cu GIL
    thread_1 = threading.Thread(target=countdown)   # thread 1 cu tinta countdown
    thread_2 = threading.Thread(target=countdown)   # thread 2 cu tinta countdown
    thread_1.start()                                # ponreste thread 1
    thread_2.start()                                # porneste thread 2
    thread_1.join()                                 # opreste thread 1
    thread_2.join()                                 # opreste thread 2


def ver_2():     # se apeleaza functia in mod secvential
    countdown()
    countdown()


def ver_3():        # se apeleaza functia in mod paralel cu multiprocessing
    process_1 = multiprocessing.Process(target=countdown)       # crearea proces 1
    process_2 = multiprocessing.Process(target=countdown)       # crearea proces 2
    process_1.start()                                           # porneste procesele
    process_2.start()
    process_1.join()                                            # opreste procesele
    process_2.join()


def ver_4():
    with ThreadPoolExecutor(max_workers=2) as executor:     # definim executorul
        future = executor.submit(countdown())               # trimitem cele 2 futures in pool ul cu threaduri
        future = executor.submit(countdown())


if __name__ == '__main__':
    start = time.time()
    ver_1()
    end = time.time()
    print("\n Timp executie pseudoparalelism cu GIL")
    print(end - start)
    start = time.time()
    ver_2()
    end = time.time()
    print("\n Timp executie secvential")
    print(end - start)
    start = time.time()
    ver_3()
    end = time.time()
    print("\n Timp executie paralela cu multiprocessing")
    print(end - start)
    start = time.time()
    ver_4()
    end = time.time()
    print("\n Timp executie paralela cu concurrent.futures")
    print(end - start)