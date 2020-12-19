from sense_hat import SenseHat
from time import sleep
from random import randint

def do_rotate(sense):
    angles = [0, 90, 180, 270, 0, 270, 180, 90, 0]
    sense.show_letter("J")
    for r in angles:
        sense.set_rotation(r)
        sleep(1)

def show_rotation():
    sense = SenseHat()
    sense.clear()
    do_rotate(sense)
    sense.clear()

def main():
    for i in range(1):
        show_rotation()

if __name__ == "__main__":
    main()
