# part 1

# first task
def reverse_string(string):
    return string[::-1]

# second task
def triangle_type(a, b, c):
    if a == b and b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"


# third task
def weird_func(number):
    if number % 2 == 0:
        if 2 <= number <= 5:
            print "Not Weird"
        elif 6 <= number <= 20:
            print "Weird"
        else:
            print "Not Weird"
    else:
        print "Weird"

# part 2

# frist task
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# second task
def is_pangram(string):
    string = string.lower()
    letters_frequency = [
        (chr(alpha), string.count(chr(alpha)))
        for alpha in xrange(ord("a"), ord("z"))
        ]
    return bool(len(filter(lambda x: x[1] > 1, letters_frequency)))

# third task
def my_zip(*args):
    result = []
    for i in xrange(len(min(args, key=len))):
        temp_res = []
        for arg in args:
            temp_res.append(arg[i])
        result.append(tuple(temp_res))
    return result


if __name__ == "__main__":
    s = "abcdefgh"
    print s
    print reverse_string(s), "\n"

    print triangle_type(3, 3, 3)
    print triangle_type(2, 1, 2)
    print triangle_type(1, 2, 3), "\n"

    weird_func(2)
    weird_func(4)
    weird_func(6)
    weird_func(20)
    weird_func(21)
    weird_func(22)

    print "\n", fib(10)
    print fib(0)
    print fib(2), "\n"

    print is_pangram("abcgfe")
    print is_pangram("Jackdaws love my big sphinx of quartz"), "\n"

    print my_zip(xrange(3), xrange(3, 6))
