from csv import reader
from os import environ
from threading import Thread
from time import sleep

from pyttsx3 import init

from time_object import Time  # There must be a library out there that already does this.


READY_TIME = environ.get('READY_TIME') or 10
WORKOUT_FILE = environ.get('WORKOUT_FILE') or 'workout.csv'
WORKOUT_LOOPS = environ.get('WORKOUT_LOOPS') or 3
DEFAULT_WORKOUT_DURATION = environ.get('WORKOUT_DURATION') or '40'
DEFAULT_BREAK_DURATION = environ.get('BREAK_DURATION') or '20'


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
