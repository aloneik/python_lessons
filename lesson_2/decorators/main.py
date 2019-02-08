import time

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
    def wrapped(format_string="%Y/%m/%d %H:%M"):
        return "Now it is {}".format(func(format_string))
    return wrapped


@formated_datetime_2
def get_time_2(format="%Y/%m/%d %H:%M"):
    return time.strftime(format, time.localtime())


# third task
def print_formated_phones(func):
    def wrapped(phones):
        phones = func(phones)
        for phone in phones:
            print phone[:3], phone[3:7], phone[7:]
    return wrapped


@print_formated_phones
def phones_list(phones):
    for index in xrange(len(phones)):
        if len(phones[index]) == 13:
            continue
        if len(phones[index]) == 12:
            phones[index] = "+" + phones[index]
        if len(phones[index]) == 11:
            phones[index] = "+91" + phones[index][1:]
        if len(phones[index]) == 10:
            phones[index] = "+91" + phones[index]
    return sorted(phones)


# fourth task
def cache(func):
    cached = [None]

    def wrapped(*args, **kwargs):
        if cached[0] is None:
            cached[0] = func(*args, **kwargs)
        return cached[0]
    return wrapped


@cache
def some_calc(x):
    return x * x * x


if __name__ == "__main__":
    print get_time(), "\n"
    print get_time_2(), "\n"

    print some_calc(2)
    print some_calc(3), "\n"

    phones = [
        "07895462130",
        "919875641230",
        "9195969878"
    ]
    phones_list(phones)
