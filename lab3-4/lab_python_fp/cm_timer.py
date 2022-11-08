from time import sleep, time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start = -1
        self.stop = -1
        self.diff = -1

    def __enter__(self):
        self.start = time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time()
        self.diff = self.stop - self.start

        print('time:', self.diff)

@contextmanager
def cm_timer_2():
    start = time()

    yield

    print('time:', time() - start)

with cm_timer_1():
    sleep(1.5)

with cm_timer_2():
    sleep(1.5)
