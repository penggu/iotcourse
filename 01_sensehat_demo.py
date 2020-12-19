from sense_hat import SenseHat
from time import sleep
from random import randint

def show_digits(sense):
    for i in range(10):
        c = chr(ord('0') + i)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sense.show_letter(c, (r, g, b))
        sleep(1)

def show_lower(sense):
    for i in range(26):
        c = chr(ord('a') + i)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sense.show_letter(c, (r, g, b))
        sleep(1)

def show_upper(sense):
    for i in range(26):
        c = chr(ord('A') + i)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        sense.show_letter(c, (r, g, b))
        sleep(1)

def show_letters():
    sense = SenseHat()
    sense.clear()
    show_digits(sense)
    show_lower(sense)
    show_upper(sense)
    sense.clear()

def main():
    for i in range(1):
        show_letters()

if __name__ == "__main__":
    main()
