from unittest import TestCase

from flabs2abs.flabs2abs import Flabs2Abs


class Flabs2AbsTestCase(TestCase):
    def setUp(self) -> None:
        self.test = Flabs2Abs()

    def test_settings_file_flag_overrides_default(self):
        self.test = Flabs2Abs(settings_file="tests/settings.ini")
        self.assertEqual(self.test.SETTINGS_FILE, "tests/settings.ini")

    def test_workout_file_flag_overrides_default(self):
        self.test = Flabs2Abs(workout_file="tests/workout.csv")
        self.assertEqual(self.test.WORKOUT_FILE, "tests/workout.csv")

    def test_ready_time_flag_overrides_default(self):
        self.test = Flabs2Abs(ready_time=1)
        self.assertEqual(self.test.READY_TIME, 1)

    def test_workout_loops_flag_overrides_default(self):
        self.test = Flabs2Abs(workout_loops=1)
        self.assertEqual(self.test.WORKOUT_LOOPS, 1)

    def test_workout_duration_flag_overrides_default(self):
        self.test = Flabs2Abs(workout_duration='1.2.3')
        self.assertEqual(self.test.DEFAULT_WORKOUT_DURATION, '1.2.3')

    def test_break_duration_flag_overrides_default(self):
        self.test = Flabs2Abs(break_duration='0.40')
        self.assertEqual(self.test.DEFAULT_BREAK_DURATION, '0.40')
