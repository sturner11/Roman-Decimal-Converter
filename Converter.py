import sys

def readfile(filename):
    with open(filename) as file:
        return file.readlines()


def writefile(filename, old_lines, new_lines):
    with open(filename, "w") as file:
        for old, new in zip(old_lines, new_lines):
            file.write(f"{old.strip()} : {new}\n")



def decimal_single_conversion(number, version=0):
    """
    :param number: Decimal Number
    :param version: 0 = Single conversion, 1 = File Conversion
    :return:
    """
    decimals = {1: "I", 4: "IV", 5:"V", 9: "IX", 10: 'X', 40: "XL", 50: "L", 90: "XC", 100: "C",
                400:"CD", 500:"D", 900:"CM", 1000:"M"}
    numeral = ""
    number = int(number)
    while number > 0:
        biggest = 1
        for num in decimals.keys():
            if number >= num:
                biggest = num
        numeral += decimals[biggest]
        number -= biggest
    if version == 0:
        print(f"Your base 10 decimal number {number} in roman numerals is {numeral}")
    return numeral


def decimal_file_conversion(infile, outfile):
    lines = readfile(infile)
    new_lines = []
    for line in lines:
        numeral = decimal_single_conversion(line, 1)
        new_lines.append(numeral)
    writefile(outfile, lines, new_lines)


def decimalize(numeral, numerals):
    """
    :param numeral: Roman Numeral to convert
    :param numerals: Roman Numeral Value Dictionary
    :return:  Dictionary with Roman Numeral mapped to tuple of ("MMM", "C")
    """
    num_set = {} #Dictionary with roman numeral mapped to number of numerals and the subtrative
    num_left = numeral
    for roman_num in numerals: # For each Roman Numeral
        decimal_place = ""
        subtractive = ""
        while roman_num in num_left: # Grab all the numerals of the type
            if num_left[0] == roman_num:
                decimal_place += num_left[0] #Group all the number together
            else:
                subtractive += num_left[0] #Keep the subtractive by itself
            num_left = num_left[1:]
        if decimal_place != "":
            num_set[roman_num] = (decimal_place, subtractive)
    return num_set


def roman_convert(num_set, numerals):
    """
    :param num_set: A Dictionary of roman numerals based on decimal places
    :param numerals: Roman Numeral value dictionary
    :return: Decimal place value
    """
    dec_val = 0
    for set in num_set.values():
        dec_val += int(len(set[0]) * numerals[set[0][0]]) #Add Roman Numeral value * the number of times it appears
        if set[1] != "":
            dec_val -= int(numerals[set[1]]) # Remove the subtractor
    return dec_val



def roman_single_conversion(numeral, version):
    """
    :param numeral: Roman Numeral to Convert
    :param version: 0 = Normal 1 = File
    :return: Decimal Value
    """
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    num_set = decimalize(numeral, numerals) #Take numeral a break it up in a list based on decimal places
    dec_val = roman_convert(num_set, numerals) # Take num_list and use computations to turn it into a decimal
    if version == 0:
        print(f"Your roman numeral {numeral} is {dec_val} in the base 10 Decimal System")
    return dec_val


def roman_file_conversion(input, output):
    lines = readfile(input)
    new_lines = []
    for line in lines:
        decimal = roman_single_conversion(line, 1)
        new_lines.append(decimal)
    writefile(output, lines, new_lines)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[2].lower() == "r":
            roman_single_conversion(sys.argv[1], 0)
        else:
            decimal_single_conversion(sys.argv[1], 0)
    elif len(sys.argv) == 4:
        if sys.argv[3].lower() == "r":
            roman_file_conversion(sys.argv[1], sys.argv[2])
        else:
            decimal_file_conversion(sys.argv[1], sys.argv[2])
    else:
        print("Please do either:")
        print("\t Run the program with 2 arguments:"
              "\t\t1) The number to convert "
              "\t\t2) R/r (roman to decimal) or D/d (decimal to roman)")
        print("\tOr run the program with 3 arguments: "
              "\t\t1) The filename to convert"
              "\t\t2) The output file name"
              "\t\t3)R/r (roman to decimal) or D/d (decimal to roman)")

