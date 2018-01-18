def denary_to_hexadecimal(num, remainder=None):  # default reaminder value so can be carried over during recursion

    if remainder == None:  # Sets the default remainder to a list type

        remainder = []

    quotient = int(num / 16)

    tmpRemainder = num % 16  # Temporary remainder, this allows us to append it to a list of remainders

    remainder.insert(0, tmpRemainder)  # Remainder list is used in calculating Hexadecimal

    if quotient > 0:  # Continues dividing quotient until no longer divisble, after this there are no more remainders

        return denary_to_hexadecimal(quotient, remainder)  # if still divisible it the function will recur

    for x in range(len(remainder)):  # sets any remainder > 9 and < 16 to its Hexadecimal equivelant

        hexcode = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }
        if remainder[x] in hexcode:
            remainder[x] = hexcode[remainder[x]]

        print(remainder[x], end="")




