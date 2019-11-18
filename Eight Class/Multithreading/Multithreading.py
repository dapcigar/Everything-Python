import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, ThreadId, name, counter):
        threading.Thread.__init__(self)
        self.ThreadId = ThreadId
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}")
        print_time(self.name, self.counter, 10)
        print("Exiting " + self.name)


def print_time(ThreadName, delay, counter):
    while counter:
        if exitFlag:
            ThreadName.exit()
        time.sleep(delay)
        print("%s: %s" % (ThreadName, time.ctime(time.time())))
        counter -= 1


obj = MyThread(1, "First Thread", 1)
obj2 = MyThread(2, "Second Thread", 2)

obj.start()
obj2.start()

obj.join()
obj2.join()

print("Existing Main Thread")
