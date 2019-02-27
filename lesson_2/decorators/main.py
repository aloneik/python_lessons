import time


# first task
def formated_datetime(func):
    def wrapped(*args, **kwargs):
        datetime = func(*args, **kwargs)
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
    def wrapped(*args, **kwargs):
        return "Now it is {}".format(func(*args, **kwargs))
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
        arguments = (
            args,
            tuple(((key, kwargs[key]) for key in sorted(kwargs)))
            )
        if arguments not in cached:
            cached[arguments] = func(*args, **kwargs)
        return cached[arguments]
    return wrapped


@cache
def pow_3(x):
    return x * x * x


@cache
def w(a=0, b=0):
    return a + b * 2


if __name__ == "__main__":
    print get_time(), "\n"
    print get_time_2()
    print get_time_2(format="%Y-%m-%d %H:%M"), "\n"

    print pow_3(2)
    print pow_3(2)
    print pow_3(3)
    print pow_3(3)
    print w(a=1)
    print w(b=1)
    print w(a=1, b=1)
    print w(a=1, b=2)
    print w(a=2, b=1), "\n"

    phones = [
        "07895462130",
        "919875641230",
        "9195969878"
    ]
    phones_list(phones)
