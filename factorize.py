from multiprocessing import Process
import logging
import time


def factorize(*number):
    result = []
    for num in number:
        result.append(divide(num))
    return result
    # raise NotImplementedError()  # Remove after implementation


def divide(number) -> list:
    result = []
    for el in range(number):
        if el == 0:
            continue
        if number % el == 0:
            result.append(el)
        el += 1
    result.append(number)
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    start = time.time()
    logging.info(f"Start program (sinho): {start}")

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    end = time.time()
    logging.info(f"End program (sinho): {end}")
    logging.info(f"===========Time working (sinho): {end - start} seconds")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start_p = time.time()
    logging.info(f"Start program (proces): {start_p}")

    processes = []
    arg = (128, 255, 99999, 10651060)
    for i in range(len(arg)):
        pr = Process(target=factorize, args=(arg[i],))
        pr.start()
        processes.append(pr)

    [el.join() for el in processes]

    end_p = time.time()
    logging.info(f"end program (proces): {end_p}")
    logging.info(f"===========Time working (proces): {end_p - start_p} seconds")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
