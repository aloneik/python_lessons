# -*- coding: utf-8 -*-
import os
import math
import cmath
import timeit


# first task
def my_exp(N, t):
    for num in xrange(N):
        print u"Экспонента в степени {0}: {1:.{2}f} # exp({0})".format(
            num + 1, math.exp(num + 1), t
            )


# second task
def chars_frequency(string):
    string = string.lower()
    return {char: string.count(char) for char in string}


# third task
def read_partially(filepath, part_len, method="r"):
    f = open(filepath, method)
    return (
        unicode(f.read(part_len)) 
        for part in xrange(os.path.getsize(filepath) / part_len)
        )


# fourth task
def find_word_with_3th_min_symbol(string):
    return min(string.split(), key=(lambda word: ord(word[2])))


def find_word_with_5th_max_symbol(string):
    return max(string.split(), key=(lambda word: ord(word[4])))


# fifth task
def print_fibs(n):
    print 0
    if n == 1:
        return
    for num in xrange(1, n):
        print (((1 + math.sqrt(5))/2)**num - ((1 - math.sqrt(5))/2)**num) / math.sqrt(5) 


# sixth task
def roots_array():
    def solve_quadratic_equation(a, b, c):
        d = b**2 - 4*a*c
        if d < 0:
            print complex(-b, cmath.sqrt(d)) / (2*a)
    solve_quadratic_equation


# tenth task
def my_map(func, *args):
    return [
        func(*[arg.pop(0) for arg in args])
        for i in xrange(len(min(args, key=len)))
    ]


def my_zip(*args):
    return [
        tuple([arg.pop(0) for arg in args])
        for i in xrange(len(min(args, key=len)))
    ]


def my_filter(func, sequence):
    if func is None:
        return sequence
    return [
        item for item in sequence if func(item)
    ]


def my_chain(*iterables):
    for iterator in iterables:
        for element in iterator:
            yield element


# eleventh task
def f11():
    map_time = timeit.timeit(
        "map(lambda x: x + 10, [1, 2, 3, 4])", 
        number=1000
        )
    my_map_time = timeit.timeit(
        "my_map(lambda x: x + 10, [1, 2, 3, 4])", 
        "from __main__ import my_map",
        number=1000
        )
    print "map:", map_time
    print "mymap", my_map_time

    list_gen_time = timeit.timeit(
        "[item + 10 for item in [1, 2, 3, 4, 5]]",
        number=1000
        )
    list_genexp_time = timeit.timeit(
        "list((item + 10 for item in [1, 2, 3, 4, 5]))",
        number=1000
        )
    print "list gen time", list_gen_time
    print "list genexp time", list_genexp_time


# twelveth task
class CopyMng():
    def __init__(self, src_path, dst_path):
        self.src_file_path = src_path
        self.dest_file_path = dst_path
    
    def __enter__(self):
        pass

    def __exit(self, type, value, traceback):
        pass


# fourteenth task
def min_and_max(lst):
    minimum = min(lst)
    maximum = ""
    max_gen = (str(lst.pop(lst.index(max(lst)))) for i in xrange(len(lst)))
    for i in max_gen:
        maximum += i
    return (minimum, int(maximum))


# fifteenth task
def prime_nums_to_n(N):
    prime_list = []
    for i in range(2, N+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, N+1, i):
                prime_list.append(j)


if __name__ == "__main__":
    my_exp(4, 3)

    print chars_frequency("Hello World!")

    reader = read_partially("f:/max/python/python_lessons-master/lesson_3/iterators and generators/main.py", 20, "rb")
    print next(reader)

    st = "abcrth flnafkle aanpz"
    print find_word_with_3th_min_symbol(st)
    print find_word_with_5th_max_symbol(st)

    print_fibs(10)

    print my_map((lambda x, y: x + y), [1,2,3], [2, 3, 4])
    print my_zip([1,2,3], [2, 3])
    print my_filter(len, [(), (1, 2, 3), "13342"])
    it = my_chain("abc", "dfg")
    for i in it:
        print i

    f11()

    print min_and_max([1, 2, 3, 4])

    prime_nums_to_n(11)