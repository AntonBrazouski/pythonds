from queue import Queue
import test

class TestCase:
    def __init__(self):
        self.q = Queue()

    def simple_test(self):
        test.testEqual(isinstance(self.q, Queue), True)

    
