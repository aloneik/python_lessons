class DecToRoman():
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )
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


if __name__ == "__main__":
    conv = DecToRoman()
    rev_conv = RomanToDec()
    print conv.dec_to_roman(39)
    print rev_conv.roman_to_dec(conv.dec_to_roman(39))
    print conv.dec_to_roman(421)
    print rev_conv.roman_to_dec(conv.dec_to_roman(421))
    print conv.dec_to_roman(1066)
    print rev_conv.roman_to_dec(conv.dec_to_roman(1066))
    print conv.dec_to_roman(2014)
    print rev_conv.roman_to_dec(conv.dec_to_roman(2014))

    # two side conversions
    conv1 = AnyBaseConvertor()
    print conv1.dec_to_bin(8)
    print conv1.bin_to_dec(conv1.dec_to_bin(8))
    print conv1.dec_to_oct(8)
    print conv1.oct_to_dec(conv1.dec_to_oct(8))
    print conv1.dec_to_hex(8)
    print conv1.hex_to_dec(conv1.dec_to_hex(8))

    print conv1.roman_to_oct(conv1.dec_to_roman(8))
    print conv1.oct_to_roman(conv1.roman_to_oct(conv1.dec_to_roman(8)))
    print conv1.roman_to_bin(conv1.dec_to_roman(8))
    print conv1.bin_to_roman(conv1.roman_to_bin(conv1.dec_to_roman(8)))
    print conv1.roman_to_hex(conv1.dec_to_roman(8))
    print conv1.hex_to_roman(conv1.roman_to_hex(conv1.dec_to_roman(8)))

