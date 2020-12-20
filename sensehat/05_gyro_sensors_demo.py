from sense_hat import SenseHat
from time import sleep
from random import randint

def do_readings(sense):
        orientation = sense.get_orientation()
        pitch = round(orientation['pitch'], 0)
        roll = round(orientation['roll'], 0)
        yaw = round(orientation['yaw'], 0)
        acceleration = sense.get_accelerometer_raw()
        x = round(acceleration['x'], 0)
        y = round(acceleration['y'], 0)
        z = round(acceleration['z'], 0)
        msg = f"pitch = {pitch}, roll = {roll}, yaw = {yaw}, x = {x}, y = {y}, z={z}"
        print(msg)

def show_sensor_readings():
    sense = SenseHat()
    sense.clear()
    do_readings(sense)
    sense.clear()

def main():
    for i in range(100):
        show_sensor_readings()

if __name__ == "__main__":
    main()
