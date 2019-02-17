import time
from collections import namedtuple


# first task
def formated_datetime(func):
    def wrapped():
        datetime = func()
        return "It is {0}. Since {1} hours and {2} minutes.".format(
            datetime[0],
            datetime[1],
            datetime[2]
        )
    return wrapped


@formated_datetime
def get_time():
    date, loc_time = time.strftime("%c", time.localtime()).split()
    hour, minutes = loc_time.split(":")[:2]
    return [date, hour, minutes]


# second task
def formated_datetime_2(func):
    def wrapped(format="%Y/%m/%d %H:%M"):
        return "Now it is {}".format(func(format))
    return wrapped


@formated_datetime_2
def get_time_2(format="%Y/%m/%d %H:%M"):
    return time.strftime(format, time.localtime())


# third task
def print_formated_phones(func):
    def wrapped(phones):
        phones = func(phones)
        for phone in phones:
            print phone[:3], phone[3:8], phone[8:]
    return wrapped


@print_formated_phones
def phones_list(phones):
    phones = map(lambda number: "+91" + number[-10:], phones)
    return sorted(phones)


# fourth task
def cache(func):
    cached = {}

    def wrapped(*args, **kwargs):
        arguments = (args, namedtuple("FuncKwArgs", kwargs.keys())(**kwargs))
        if not arguments in cached:
            cached[arguments] = func(*args, **kwargs)
        return cached[arguments]
    return wrapped


@cache
def pow_3(x):
    return x * x * x


if __name__ == "__main__":
    print get_time(), "\n"
    print get_time_2()
    print get_time_2(format="%Y-%m-%d %H:%M"), "\n"

    print pow_3(2)
    print pow_3(2)
    print pow_3(3)
    print pow_3(3), "\n"

    phones = [
        "07895462130",
        "919875641230",
        "9195969878"
    ]
    phones_list(phones)
