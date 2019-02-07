import time

# first task
class Timer():
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, type, value, traceback):
        print "excecution time: {}".format(time.time() - self.start_time)


with Timer() as timer:
    l = [val for val in xrange(1000000)]


# second task
class FileStringsCounter():
    def __init__(self, filepath):
        self.file = open(filepath)

    def __enter__(self):
        self.strings_count = 0
        for string in self.file:
            self.strings_count += 1
        return self.file

    def __exit__(self, type, value, traceback):
        print self.strings_count
        self.file.close()


#filepath = input("enter path to file")
filepath = "I:/python/lessons/lesson_2/context managers/tasks.txt"
with FileStringsCounter(filepath) as counter:
    pass
