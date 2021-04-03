from csv import reader
import logging
from threading import Thread
from time import sleep

from configparser import ConfigParser
from pyttsx3 import init

from time_object import (
    Time,
)  # There must be a library out there that already does this.

logging.basicConfig(format="%(message)s", level=logging.DEBUG)


class Flabs2Abs:
    def __init__(
        self,
        settings_file="flabs2abs/settings.ini",
        workout_file=None,
        ready_time=None,
        workout_loops=None,
        workout_duration=None,
        break_duration=None,
    ):
        self.SETTINGS_FILE = settings_file

        config = ConfigParser()
        config.read(self.SETTINGS_FILE)

        self.WORKOUT_FILE = workout_file or config.get("General", "WORKOUT_FILE")
        self.READY_TIME = ready_time or config.get("Workout", "READY_TIME")
        self.WORKOUT_LOOPS = workout_loops or config.get("Workout", "WORKOUT_LOOPS")
        self.DEFAULT_WORKOUT_DURATION = workout_duration or config.get(
            "Workout", "DEFAULT_WORKOUT_DURATION"
        )
        self.DEFAULT_BREAK_DURATION = break_duration or config.get(
            "Workout", "DEFAULT_BREAK_DURATION"
        )
        self.engine = init()
        self.operation = str()

    def timer(self, duration):
        for i in range(int(duration)):
            logging.debug("%s: %s/%s", self.operation, i + 1, duration)
            sleep(1)

    def converted_countdown(self, operation, duration, context="for"):
        self.operation = operation
        sentence = f"{operation} {context} {duration.spoken_time}"
        if operation == "break":
            sentence = f"{duration.spoken_time} {operation}"
        logging.debug(sentence)
        self.engine.say(sentence)
        voice_thread = Thread(target=self.engine.runAndWait())
        timer_thread = Thread(target=self.timer(duration.total_seconds))
        timer_thread.start()
        voice_thread.start()

    def start_workout(self):
        self.converted_countdown("workout starting", Time(self.READY_TIME), "in")
        loop = 0
        while loop < int(self.WORKOUT_LOOPS):
            with open(self.WORKOUT_FILE) as workout_file:
                logging.debug("loop %s/%s", loop + 1, self.WORKOUT_LOOPS)
                csv_reader = reader(workout_file, delimiter=",")
                for row in csv_reader:
                    if row[1]:
                        workout_duration = Time(row[1])
                    else:
                        workout_duration = Time(self.DEFAULT_WORKOUT_DURATION)
                    if row[2]:
                        break_duration = Time(row[2])
                    else:
                        break_duration = Time(self.DEFAULT_BREAK_DURATION)
                    self.converted_countdown(row[0], workout_duration)
                    if break_duration.total_seconds:
                        self.converted_countdown("break", break_duration)
                loop = loop + 1

        self.engine.say("workout complete")
        self.engine.runAndWait()
        workout_file.close()
