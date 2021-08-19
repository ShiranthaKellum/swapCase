
# a 97 A 65  z 122 Z 90
# ord () gives the ASCII value of a character/s
# chr () geives the particular character of a given ASCII value

def converter (text) :
    for i in text :
        if 64 < ord (i) < 91 :                       # if capital
            i = chr (ord (i) + 32)                  # convert it in to simple
            print (i, end="")

        elif 96 < ord (i) < 123 :                    # if simple
            i = chr (ord (i) - 32)                  # convert it into capital
            print (i, end="")

        else :
            print (i, end="")                       # if anything else no change

s = input ()

converter (s)