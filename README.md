# flabs2abs

*A simple script that speaks aloud your exercises with duration and break timers.*

Do you just want a simple timer to help you exercise?
Do you get sick that everything on the market either wants you to pay them or watch ads?
I do.

There's probably a million other solutions out there just like this but here's my take.
I rushed this messy solution out, so I could get my fat ass exercising ASAP.
I'll be adding onto this over time and turning it into a pip module.

## Usage

This script only expects one thing on the user's part and that's to have `WORKOUT_FILE` in CSV format (see *Environment variables* below).
The CSV is read in the following format:

| workout name | workout duration | break duration |
| ------------ | ---------------- | -------------- |
| crunches | 40 | 20 |
| scissors | 0:40 | 0:20 |
| plank | 0:0:40 | 0:0:20 |

All three of those entries would work fine with the script to set 40 and 20 seconds respectively.

It should be noted that durations are not mandatory - my file looks as so:

```
crunches,,
scissors,,
plank,,
oblique toe taps,,
knee to elbow crunches,,
leg wipers,,
```

Any time value that is not filled will use the `DEFAULT_[WORKOUT|BREAK]_DURATION` values set in `flabs2abs.py`.

## Environment variables

At the moment these values are hard-coded inside `flabs2abs.py`.
With the pip module integration will come a CLI interface where these values can be more easily edited.
Furthermore, I also plan to move said values to an INI file for even easier use from others.

| Environment variable     | Description | Default value | Type |
| ------------------------ | ----------- | ------------- | ---- |
| READY_TIME               | How long the user has in seconds before the workout starts | 10 | Integer |
| WORKOUT_FILE             | Relative/absolute path to the workout file. The file could be named something else so long as it is in CSV format. | workout.csv | String |
| WORKOUT_LOOPS            | How many times the script will repeat the exercises in the file. | 3 | Integer |
| DEFAULT_WORKOUT_DURATION | How long the workout will last in seconds | 40 | String |
| DEFAULT_BREAK_DURATION   | How long a break the user has after the exercise in seconds | 20 | String |
