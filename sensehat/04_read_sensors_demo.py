from sense_hat import SenseHat
from time import sleep
from random import randint

def do_readings(sense):
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)
        if t > 18.3 and t < 26.7:
            bg = (0, 100, 0) # green
            tc = (255, 255, 255) # white
        else:
            bg = (100, 0, 0) # red
            tc = (200, 200, 0) # yellow
        msg = f"Temperature = {t}, Pressure = {p}, Humidity = {h}"
        msg2 = f"温度 = {t}, 气压 = {p}, 湿度 = {h}"
        sense.show_message(msg, scroll_speed=0.08, back_colour=bg, text_colour=tc)
        print(msg2)

def show_sensor_readings():
    sense = SenseHat()
    sense.clear()
    do_readings(sense)
    sense.clear()

def main():
    for i in range(1):
        show_sensor_readings()

if __name__ == "__main__":
    main()
