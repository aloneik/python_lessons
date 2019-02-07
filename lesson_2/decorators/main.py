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

if __name__ == "__main__":
    print get_time(), "\n"
    print get_time_2()
