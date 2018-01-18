def longestWord(ua_string):

    ua_string= ua_string.split()

    longestLength = ""

    for x in range (len(ua_string)):

        if len(ua_string[x]) > len(longestLength):

            longestLength = ua_string[x]

    print(longestLength)


longestWord(str(input("Enter String: ")))