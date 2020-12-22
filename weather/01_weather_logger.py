from sense_hat import SenseHat
from time import sleep, asctime
from random import randint

def do_log_weather(sense):
    t = round(sense.get_temperature() * 1.8 + 32, 1)
    p = round(sense.get_pressure(), 1)
    h = round(sense.get_humidity(), 1)
    message = f" T={t}F, H={h}, P={p} "
    print(message)
    sense.show_message(message,
                       scroll_speed=0.08,
                       text_colour=(200, 200, 200),
                       back_colour=(0, 0, 0))
    with open('weather.txt', 'a') as log:
        now = str(asctime())
        log.write(now + ' ' + message + '\n')

def log_weather():
    sense = SenseHat()
    sense.clear()
    do_log_weather(sense)
    sleep(5)
    sense.clear()

def main():
    for i in range(1):
        log_weather()

if __name__ == "__main__":
    main()
