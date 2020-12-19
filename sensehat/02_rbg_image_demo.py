from sense_hat import SenseHat
from time import sleep
from random import randint

def do_show_image(sense):
    r = (255, 0, 0)
    o = (255, 127, 0)
    y = (255, 255, 0)
    g = (0, 255, 0)
    b = (0, 0,255)
    i = (75, 0, 130)
    v = (159, 0, 255)
    e = (0, 0, 0)
    image = [
        e,e,e,e,e,e,e,e,
        e,e,e,r,r,e,e,e,
        e,r,r,o,o,r,r,e,
        r,o,o,y,y,o,o,r,
        o,y,y,g,g,y,y,o,
        y,g,g,b,b,g,g,y,
        b,b,b,i,i,b,b,b,
        b,i,i,v,v,i,i,b
        ]
    sense.set_pixels(image)

def show_image():
    sense = SenseHat()
    sense.clear()
    do_show_image(sense)
    sleep(3)
    sense.clear()

def main():
    for i in range(1):
        show_image()

if __name__ == "__main__":
    main()
