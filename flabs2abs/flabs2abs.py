from csv import reader
from threading import Thread
from time import sleep

from configparser import ConfigParser
from pyttsx3 import init

from time_object import Time  # There must be a library out there that already does this.

SETTINGS_FILE = 'flabs2abs/settings.ini'

Config = ConfigParser()
Config.read(SETTINGS_FILE)


WORKOUT_FILE = Config.get('General', 'WORKOUT_FILE')
READY_TIME = Config.get('Workout', 'READY_TIME')
WORKOUT_LOOPS = Config.get('Workout', 'WORKOUT_LOOPS')
DEFAULT_WORKOUT_DURATION = Config.get('Workout', 'DEFAULT_WORKOUT_DURATION')
DEFAULT_BREAK_DURATION = Config.get('Workout', 'DEFAULT_BREAK_DURATION')


def timer(duration):
    for i in range(int(duration)):
        sleep(1)
        print(i+1)


engine = init()
engine.say(f"Workout starting in {READY_TIME} seconds")
voice_thread = Thread(target=engine.runAndWait())
timer_thread = Thread(target=timer(READY_TIME))
voice_thread.start()
timer_thread.start()
loop = 0
while loop != WORKOUT_LOOPS:
    with open(WORKOUT_FILE) as workout_file:
        print(f"loop {loop+1}/{WORKOUT_LOOPS}")
        csv_reader = reader(workout_file, delimiter=',')
        for row in csv_reader:
            if row[1]:
                workout_duration = Time(row[1])
            else:
                workout_duration = Time(DEFAULT_WORKOUT_DURATION)
            if row[2]:
                break_duration = Time(row[2])
            else:
                break_duration = Time(DEFAULT_BREAK_DURATION)

            engine.say(f"{row[0]} for {workout_duration.spoken_time}")

            voice_thread = Thread(target=engine.runAndWait())
            timer_thread = Thread(target=timer(workout_duration.total_seconds))
            voice_thread.start()
            timer_thread.start()
            engine.say(f"{break_duration.spoken_time} break")
            voice_thread = Thread(target=engine.runAndWait())
            timer_thread = Thread(target=timer(break_duration.total_seconds))
            voice_thread.start()
            timer_thread.start()
        loop = loop+1

engine.say('workout complete')
engine.runAndWait()
workout_file.close()
