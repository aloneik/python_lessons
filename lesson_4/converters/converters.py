from abc import abstractmethod


class Callable():
    @abstractmethod
    def __call__(self):
        raise NotImplementedError("Please implement this method")


class DecToRoman(Callable):
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )
    def __init__(self, number=None):
        self.number = number

    def __add__(self, other):
        if isinstance(self.number, int):
            return self.number + other.number

    def __sub__(self, other):
        if isinstance(self.number, int):
            return self.number - other.number

    def __mul__(self, other):
        if isinstance(self.number, int):
            return self.number * other.number

    def __div__(self, other):
        if isinstance(self.number, int):
            return self.number / other.number

    def __floordiv__(self, other):
        if isinstance(self.number, int):
            return self.number // other.number

    def __call__(self, number):
        return self.dec_to_roman(number)

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def dec_to_roman(self, number):
        if number <= 0 or number >= 4000 or int(number) != number:
            raise ValueError('Input should be an integer between 1 and 3999')
        result = []
        for dec, roman in DecToRoman.coding:
            while number >= dec:
                result.append(roman)
                number -= dec
        return ''.join(result)


class RomanToDec(DecToRoman):
    base_coding = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
        }
    def __init__(self, number=None):
        self.number = number

    def __add__(self, other):
        if isinstance(self.number, int):
            if isinstance(other.number, str):
                return self.number + self.roman_to_dec(other.number)
            else:
                return self.number + other.number
        else:
            if isinstance(other.number, str):
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       + other.roman_to_dec(other.number))
            else:
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       + other.number)

    def __sub__(self, other):
        if isinstance(self.number, int):
            if isinstance(other.number, str):
                return self.number - self.roman_to_dec(other.number)
            else:
                return self.number - other.number
        else:
            if isinstance(other.number, str):
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       - other.roman_to_dec(other.number))
            else:
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       - other.number)

    def __mul__(self, other):
        if isinstance(self.number, int):
            if isinstance(other.number, str):
                return self.number * self.roman_to_dec(other.number)
            else:
                return self.number * other.number
        else:
            if isinstance(other.number, str):
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       * other.roman_to_dec(other.number))
            else:
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       * other.number)

    def __floordiv__(self, other):
        if isinstance(self.number, int):
            if isinstance(other.number, str):
                return self.number // self.roman_to_dec(other.number)
            else:
                return self.number // other.number
        else:
            if isinstance(other.number, str):
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       // other.roman_to_dec(other.number))
            else:
                return self.dec_to_roman(self.roman_to_dec(self.number)
                       // other.number)

    def __call__(self, number, target_base="dec"):
        """Number - int or str, target_base - dec or roman"""
        if target_base == "roman":
            if isinstance(number, str):
                return number
            return self.dec_to_roman(number)
        elif target_base == "dec":
            if isinstance(number, int):
                return number
            return self.roman_to_dec(number)

    def __lt__(self, other):
        return self(self.number) < other(other.number)

    def __le__(self, other):
        return self(self.number) <= other(other.number)

    def __eq__(self, other):
        return self(self.number) == other(other.number)

    def __ne__(self, other):
        return self(self.number) != other(other.number)

    def __gt__(self, other):
        return self(self.number) > other(other.number)

    def __ge__(self, other):
        return self(self.number) >= other(other.number)

    def roman_to_dec(self, roman_num):
        decimal = 0
        for index, symb in enumerate(roman_num):
            if (
                index + 1 == len(roman_num) 
                or RomanToDec.base_coding[symb] 
                    >= RomanToDec.base_coding[roman_num[index+1]]):
                decimal += RomanToDec.base_coding[symb]
            else:
                decimal -= RomanToDec.base_coding[symb]
        return decimal


class AnyBaseConvertor(RomanToDec):
    def __init__(self, number=None):
        self.number = number

    def __add__(self, other):
        if isinstance(self.number, int):
            return self.number + other(other.number, "dec")
        elif self.number.count("b"):
            return self.dec_to_bin(
                self.bin_to_dec(self.number) 
                + other(other.number, "dec")
                )
        elif self.number[0] in self.base_coding:
            return self.dec_to_roman(
                self.roman_to_dec(self.number)
                + other(other.number, "dec")
                )
        elif "x" in self.number:
            return self.dec_to_hex(
                self.hex_to_dec(self.number)
                + other(other.number, "dec")
                )
        elif self.number.isdigit():
            return self.dec_to_oct(
                self.oct_to_dec(self.number)
                + other(other.number, "dec")
                )

    def __sub__(self, other):
        # Not implemented for numbers < 0
        if isinstance(self.number, int):
            return self.number - other(other.number, "dec")
        elif self.number.count("b"):
            return self.dec_to_bin(
                self.bin_to_dec(self.number) 
                - other(other.number, "dec")
                )
        elif self.number[0] in self.base_coding:
            return self.dec_to_roman(
                self.roman_to_dec(self.number)
                - other(other.number, "dec")
                )
        elif "x" in self.number:
            return self.dec_to_hex(
                self.hex_to_dec(self.number)
                - other(other.number, "dec")
                )
        elif self.number.isdigit():
            return self.dec_to_oct(
                self.oct_to_dec(self.number)
                - other(other.number, "dec")
                )

    def __mul__(self, other):
        if isinstance(self.number, int):
            return self.number * other(other.number, "dec")
        elif self.number.count("b"):
            return self.dec_to_bin(
                self.bin_to_dec(self.number) 
            * other(other.number, "dec")
                )
        elif self.number[0] in self.base_coding:
            return self.dec_to_roman(
                self.roman_to_dec(self.number)
            * other(other.number, "dec")
                )
        elif "x" in self.number:
            return self.dec_to_hex(
                self.hex_to_dec(self.number)
            * other(other.number, "dec")
                )
        elif self.number.isdigit():
            return self.dec_to_oct(
                self.oct_to_dec(self.number)
            * other(other.number, "dec")
                )

    def __floordiv__(self, other):   
        if isinstance(self.number, int):
            return self.number // other(other.number, "dec")
        elif self.number.count("b"):
            return self.dec_to_bin(
                self.bin_to_dec(self.number) 
            // other(other.number, "dec")
                )
        elif self.number[0] in self.base_coding:
            return self.dec_to_roman(
                self.roman_to_dec(self.number)
            // other(other.number, "dec")
                )
        elif "x" in self.number:
            return self.dec_to_hex(
                self.hex_to_dec(self.number)
            // other(other.number, "dec")
                )
        elif self.number.isdigit():
            return self.dec_to_oct(
                self.oct_to_dec(self.number)
            // other(other.number, "dec")
                )

    def __call__(self, number, target_base="dec"):
        """Number - int or str; 
        target_base - bin, dec, oct, hex, roman""" 
        if target_base == "bin":
            if isinstance(number, int):
                return bin(number)
            elif number.count("b"):
                return number
            elif number[0] in self.base_coding:
                return self.roman_to_bin(number)
            elif "x" in number:
                return self.dec_to_bin(self.hex_to_dec(number))
            elif number.isdigit():
                return self.dec_to_bin(self.oct_to_dec(number))
        elif target_base == "dec":
            if isinstance(number, int):
                return number
            elif number.count("b"):
                return int(number, 2)
            elif number[0] in self.base_coding:
                return self.roman_to_dec(number)
            elif "x" in number:
                return self.hex_to_dec(number)
            elif number.isdigit():
                return self.oct_to_dec(number)
        elif target_base == "oct":
            if isinstance(number, int):
                return self.dec_to_oct(number)
            elif number.count("b"):
                return self.dec_to_oct(self.bin_to_dec(number))
            elif number[0] in self.base_coding:
                return self.roman_to_oct(number)
            elif "x" in number:
                return self.dec_to_oct(self.hex_to_dec(number))
            elif number.isdigit():
                return number
        elif target_base == "hex":
            if isinstance(number, int):
                return self.dec_to_hex(number)
            elif number.count("b"):
                return self.dec_to_hex(self.bin_to_dec(number))
            elif number[0] in self.base_coding:
                return self.roman_to_hex(number)
            elif "x" in number:
                return number
            elif number.isdigit():
                return self.dec_to_hex(self.oct_to_dec(number))
        if target_base == "roman":
            if isinstance(number, int):
                return self.dec_to_roman(number)
            elif number.count("b"):
                return self.bin_to_roman(number)
            elif number[0] in self.base_coding:
                return number
            elif "x" in number:
                return self.dec_to_roman(self.hex_to_dec(number))
            elif number.isdigit():
                return self.dec_to_roman(self.oct_to_dec(number))

    def __lt__(self, other):
        return self(self.number) < other(other.number)

    def __le__(self, other):
        return self(self.number) <= other(other.number)

    def __eq__(self, other):
        return self(self.number) == other(other.number)

    def __ne__(self, other):
        return self(self.number) != other(other.number)

    def __gt__(self, other):
        return self(self.number) > other(other.number)

    def __ge__(self, other):
        return self(self.number) >= other(other.number)

    def dec_to_bin(self, number):
        return bin(number)

    def bin_to_dec(self, number_bin):
        return int(number_bin, 2)

    def roman_to_bin(self, roman_num):
        return bin(self.roman_to_dec(roman_num))

    def bin_to_roman(self, number_bin):
        return self.dec_to_roman(int(number_bin, 2))

    def dec_to_oct(self, number):
        return oct(number)

    def oct_to_dec(self, number_oct):
        return int(number_oct, 8)

    def oct_to_roman(self, number_oct):
        return self.dec_to_roman(int(number_oct, 8))

    def roman_to_oct(self, roman_num):
        return oct(self.roman_to_dec(roman_num))

    def dec_to_hex(self, number):
        return hex(number)

    def hex_to_dec(self, hex_num):
        return int(hex_num, 16)

    def roman_to_hex(self, roman_num):
        return hex(self.roman_to_dec(roman_num))

    def hex_to_roman(self, hex_num):
        return self.dec_to_roman(int(hex_num, 16))
