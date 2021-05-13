import time
import os

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "§", "$", "%", "6", "/", "(", ")", "=", "?", "ß", "²", "³", "{", "[", "]", "}"]

length = len(letter) - 1
done = 0

clear = lambda: os.system('cls')

for i in letter:
    progress = length - done
    time.sleep(0.10)

    done += 1
    clear()
    print("[" + "■" * done + "□" * progress + "]")
