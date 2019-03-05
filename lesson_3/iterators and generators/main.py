# -*- coding: utf-8 -*-
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
    with open(filepath, method) as f:
        while True:
            part = unicode(f.read(part_len))
            if part:
                yield part
            else:
                return


# fourth task
def find_word_with_3th_min_symbol(string):
    return min(string.split(), key=lambda word: ord(word[2]))


def find_word_with_5th_max_symbol(string):
    return max(string.split(), key=lambda word: ord(word[4]))


# fifth task
def print_fibs(n):
    print 0
    if n == 1:
        return
    for num in xrange(1, n):
        print (
            (((1 + math.sqrt(5))/2)**num - ((1 - math.sqrt(5))/2)**num)
            / math.sqrt(5)
            )


# sixth task
def roots_array():
    def solve_quadratic_equation(a, b, c):
        if a == 0:
            if b == 0:
                return None
            else:
                return -c / b
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
        if d == 0:
            x1 = -b / (2 * a)
            x2 = x1
        if d < 0:
            x1 = complex(-b, cmath.sqrt(d)) / (2 * a)
            x2 = complex(-b, -cmath.sqrt(d)) / (2 * a)
        return x1 + x2
    return [
        [
            [
                solve_quadratic_equation(a, b, c)
                for c in range(11)
            ]
            for b in range(11)
        ]
        for a in range(11)
    ]


# tenth task
def my_map(func, *args):
    return [func(*arg) for arg in my_zip(*args)]


def my_zip(*args):
    args = [tuple(arg) for arg in args]
    return [tuple(x[i] for x in args) for i in xrange(len(min(args, key=len)))]


def my_filter(func, sequence):
    if func is None:
        result = [
            item for item in sequence if item
        ]
    else:
        result = [
            item for item in sequence if func(item)
        ]
    if isinstance(sequence, str):
        return str(result)
    if isinstance(sequence, tuple):
        return tuple(result)
    return result


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


# fourteenth task
def min_and_max(lst):
    minimum = min(lst)
    maximum = ""
    lst = sorted(lst, reverse=True)
    for num in lst:
        maximum += str(num)
    return minimum, int(maximum)


# fifteenth task
def prime_nums_to_n(N):
    primes = set()
    for i in range(2, N + 1):
        if i not in primes:
            print (i)
            for j in range(i * i, N + 1, i):
                primes.add(j)


if __name__ == "__main__":
    my_exp(4, 3)

    print chars_frequency("Hello World!")

    reader = read_partially(
        "f:/max/python/python_lessons/lesson_3/"
        "iterators and generators/text.txt",
        20,
        "rb"
        )
    for part in reader:
        print part

    st = "abcrth flnafkle aanpz"
    print find_word_with_3th_min_symbol(st)
    print find_word_with_5th_max_symbol(st)

    print_fibs(10)

    print my_map((lambda x, y: x + y), [1, 2, 3], [2, 3, 4])
    print map((lambda x, y: x + y), [1, 2, 3], [2, 3, 4])
    print my_map(len, ["aa", "aaa", ""])
    print map(len, ["aa", "aaa", ""])
    print my_zip([1, 2, 3], [2, 3])
    print my_filter(len, [(), (1, 2, 3), "13342"])
    print filter(None, [(), (1, 2, 3), "13342"])
    print my_filter(None, [(), (1, 2, 3), "13342"])
    a = [1, 2, 3]
    b = [2, 3]
    print a
    print b
    print my_zip(a, b)
    print a
    print b, "\n"

    it = my_chain("abc", "dfg")
    for i in it:
        print i

    f11()

    print min_and_max([1, 2, 3, 4])

    prime_nums_to_n(11)
    print roots_array()[1][1][1]
