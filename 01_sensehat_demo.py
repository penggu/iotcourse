from sense_hat import SenseHat
from time import sleep
from random import randint


def show_letter():
    sense = SenseHat()
    for i in range(10):
        c = chr(ord('0') + i)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sense.show_letter(c, (r, g, b))
        sleep(1)
    for i in range(26):
        c = chr(ord('a') + i)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sense.show_letter(c, (r, g, b))
        sleep(1)
    for i in range(26):
        c = chr(ord('A') + i)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sense.show_letter(c, (r, g, b))
        sleep(1)
    sense.clear()

def main():
    for i in range(1):
        show_letter()

if __name__ == "__main__":
    main()
