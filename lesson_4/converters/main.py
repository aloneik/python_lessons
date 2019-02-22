from converters import DecToRoman, RomanToDec, AnyBaseConvertor


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

    conv2 = DecToRoman()
    print conv2(101)
    conv3 = RomanToDec()
    print conv3(10, "roman")
    print conv3("MCXVI"), "\n"

    c4 = AnyBaseConvertor()
    print c4(10, "roman")
    print c4(bin(10), "roman")
    print c4(oct(10), "roman")
    print c4(hex(10), "roman")
    print c4("X", "roman"), "\n"

    print c4(12, "bin")
    print c4(bin(12), "bin")
    print c4(oct(12), "bin")
    print c4(hex(12), "bin")
    print c4("XII", "bin"), "\n"

    print c4(14, "oct")
    print c4(bin(14), "oct")
    print c4(oct(14), "oct")
    print c4(hex(14), "oct")
    print c4("XIV", "oct"), "\n"

    print c4(14, "oct")
    print c4(bin(14), "oct")
    print c4(oct(14), "oct")
    print c4(hex(14), "oct")
    print c4("XIV", "oct"), "\n"

    print c4(16, "hex")
    print c4(bin(16), "hex")
    print c4(oct(16), "hex")
    print c4(hex(16), "hex")
    print c4("XVI", "hex"), "\n"

    print c4(14, "dec")
    print c4(bin(14), "dec")
    print c4(oct(14), "dec")
    print c4(hex(14), "dec")
    print c4("XIV", "dec"), "\n"

    c1 = DecToRoman(4)
    c2 = DecToRoman(6)
    print c1 + c2
    print c2 - c1
    print c1 * c2
    print c2 / c1
    print c2 // c1, "\n"

    c3 = RomanToDec(4)
    c4 = RomanToDec("VI")
    print c3 + c4
    print c4 - c3
    print c3 * c4
    print c4 // c3, "\n"

    c5 = AnyBaseConvertor(4)
    c6 = AnyBaseConvertor("VI")
    print c6 + c5
    print c6 - c5
    print c5 * c6
    print c6 // c5, "\n"
    
    c7 = AnyBaseConvertor(bin(4))
    c8 = AnyBaseConvertor("VI")
    print c8 + c7
    print c8 - c7
    print c7 * c8
    print c8 // c7, "\n"

    c9 = AnyBaseConvertor("III")
    c10 = AnyBaseConvertor(5)
    print c9 > c10
    print c9 < c10
    print c9 == c10
    print c9 != c10
    print c9 >= c10
    print c9 <= c10