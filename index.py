import random
array = []
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

obj = input("Objects: ")
length = input("Length: ")
if (obj.isnumeric() == True):
    if (length.isnumeric() == True):
        for a in range(int(obj)):
            string = ""
            for b in range(int(length)):
                index = random.randint(0, len(letter) - 1)
                string = string + letter[index]
            array.append(string)

        print(array)
    else:
        print("Length Input isn't a number.")
else:
    print("Objects Input isn't a number.")
