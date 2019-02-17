import itertools


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
def adder():
    result = list()
    even_step = False
    try:
        while True:
            if even_step:
                result.append((yield result))
                even_step = False
            else:
                result.insert((yield result))
                even_step = True
    except GeneratorExit:
        return
    except Exception as ex:
        print ex.message


if __name__ == "__main__":
    print find_strings((s for s in "abcdefghij"))
    print  is_palindromable("aannb")

    g = adder()
    g.next()
    g.send(7)
    g.send(9)
    print g.close()