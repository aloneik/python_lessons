import itertools
import pickle
import math
import copy
import scipy.integrate as integrate
import time
import re
import string
from collections import Counter
import requests
from pandas import read_csv


# first task
def bits_permutations(number):
    bits = bin(number)[2:]
    bits_permutations = itertools.permutations(bits)
    # to save memory duplicate values are not filtered
    for permut in bits_permutations:
        yield int("0b{}".format("".join(permut)), 2)


# second task
def c_n_k(n, k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def studens_combinations():
    students = range(1, 21)
    first_group_comb = set(itertools.combinations(students, 3))
    second_group_comb = set(itertools.combinations(students, 5))
    third_group_comb = set(itertools.combinations(students, 12))
    all_comb = c_n_k(20, 3) * c_n_k(17, 5) * c_n_k(12, 12)
    return (
        first_group_comb,
        second_group_comb,
        third_group_comb,
        all_comb
    )


# fourth task
def find_strings(generator):
    result = []
    for element in itertools.islice(generator, 2, 8, 2):
        if isinstance(element, str):
            result.append(element)
    return result


# fifth task
def is_palindromable(string):
    char_freq = {
        (char, string.count(char))
        for char in string
        if char.isalpha()
    }
    if len(filter(lambda x: not x[1] % 2 == 0, char_freq)) > 1:
        return False
    else:
        return True


# sixth task
# not work
# i dont'n understand this task
def adder():
    result = list()
    even_step = False
    try:
        while True:
            if even_step:
                result.append((yield))
                even_step = False
            else:
                result.insert(0, (yield))
                even_step = True
    except GeneratorExit:
        yield result
        return
    except Exception as ex:
        print ex.message


# seventh task
def my_deepcopy(iterable):
    return copy.deepcopy(iterable)


# eighth task
def partial(func, *args, **kwargs):
    def new_func(*fargs, **fkwargs):
        kwargs.update(fkwargs)
        return func(*(args + fargs), **kwargs)
    return new_func


# nineth task
def serialize_to_file(filename):
    def real_decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "wb") as file:
                pickle.dump(result, file)
            return result
        return wrapped
    return real_decorator


# tenth task
def shape_area(func, xmin, xmax):
    return integrate.quad(func, xmin, xmax)[0]


# eleventh task
def print_dates(dates, format=None):
    if format is not None:
        if format == "eu":
            format = "%m/%d/%Y"
        elif format == "monthname":
            format = "%d/%B/%Y"
        dates = map(
            lambda date: time.strftime(
                format,
                time.strptime(date, "%d/%m/%Y")
                ),
            dates
            )
    for date in dates:
        print date


# twelveth task
def remove_nonalpha(string):
    return re.sub("[^a-zA-Z ]", "", string)


# fourteenth task
def words_count(filename):
    with open(filename) as file:
        text = "".join(file)
        text = text.translate(None, string.punctuation).lower()
        return dict(Counter(text.split()))


# fifteenth task
def download_file(url, filename):
    responce = requests.get(url)
    if responce.status_code == 200:
        with open(filename, "wb") as file:
            file.write(responce.content)


def fetch_top_ten_inspection_results(dataframe):
    return Counter(dataframe["Results"])


def group_by_results(dataframe):
    inspection_results = dict(fetch_top_ten_inspection_results(dataframe))
    res_dict = {}
    for res in inspection_results:
        res_dict[res] = dataframe[
            ["DBA Name", "Results"]
            ][dataframe.Results == res].to_dict()
    return res_dict


if __name__ == "__main__":
    print set(bits_permutations(6))
    print bin(6)

    print len(studens_combinations()[0])
    print len(studens_combinations()[1])
    print len(studens_combinations()[2])
    print studens_combinations()[3]

    print find_strings((s for s in "abcdefghij"))
    print is_palindromable("aannb")

    # g = adder()
    # g.next()
    # g.send(7)
    # g.send(9)
    # print g.close()

    @serialize_to_file("i:/python/lessons/lesson_3/python libraries/s.pickle")
    def square(*args):
        return map(lambda x: x**2, args)

    print square(2, 3, 4)
    with open(
        "i:/python/lessons/lesson_3/python libraries/s.pickle",
        "rb"
            ) as file:
        print pickle.load(file)

    print my_deepcopy([1, {2: (3, 4), (5, 6): [7, 8]}])
    print copy.deepcopy([1, {2: (3, 4), (5, 6): [7, 8]}])

    def add(x, y, typ):
        if typ == "plus":
            return x + y
        if typ == "minus":
            return x - y

    p_add = partial(add, 2, typ="minus")
    print p_add(4)
    print p_add(4, typ="plus")  # 6

    print shape_area(lambda x: 2*x, 0, 10)

    dates = [
        "01/02/2099",
        "02/10/2011",
        "23/12/2019"
    ]
    print_dates(dates)
    print_dates(dates, format="eu")
    print_dates(dates, format="monthname")

    print remove_nonalpha("a!@#$%^&*()ccs956")

    print words_count(
        "f:/max/python/python_lessons-master/lesson_3/"
        "python libraries/text.txt"
        )

    url = "https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv"
    download_file(
        url,
        "f:/max/python/python_lessons-master/lesson_3/python libraries/row.csv"
        )

    data = read_csv(
        "f:/max/python/python_lessons-master/lesson_3/"
        "python libraries/row-reduced.csv"
        )
    print fetch_top_ten_inspection_results(data)
    print group_by_results(data)
