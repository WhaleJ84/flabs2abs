from sys import argv

from argparse import ArgumentParser

from flabs2abs import Flabs2Abs


def cli(args=None):
    parser = ArgumentParser(
        description="A simple script that speaks aloud your exercises with duration and break timers."
    )
    parser.add_argument("-b", "--bdur", help="break duration between workouts.")
    parser.add_argument(
        "-c",
        "--conf",
        type=str,
        default="flabs2abs/settings.ini",
        help="points to configuration file.",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="points to workout file. Overrides configuration file.",
    )
    parser.add_argument(
        "-l", "--loop", type=int, help="times workout will loop before completion."
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        metavar="SECS",
        help="time in seconds before the workout starts.",
    )
    parser.add_argument("-w", "--wdur", help="workout duration per workout.")

    if args is not None:
        return parser.parse_args(args)
    return parser.parse_args()


if __name__ == "__main__":
    arg = cli(argv[1:])
    print(arg)
    program = Flabs2Abs(
        settings_file=arg.conf,
        workout_file=arg.file,
        ready_time=arg.time,
        workout_loops=arg.loop,
        workout_duration=arg.wdur,
        break_duration=arg.bdur,
    )
    program.start_workout()
