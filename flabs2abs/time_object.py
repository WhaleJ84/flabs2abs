class Time:
    def __init__(self, input):
        self.input = str(input)
        self.spoken_time = None
        self.total_seconds = int()
        self.seconds = int(self.input.split(':')[-1])
        try:
            self.minutes = int(self.input.split(':')[-2])
        except IndexError:
            self.minutes = 0
        try:
            self.hours = int(self.input.split(':')[-3])
        except IndexError:
            self.hours = 0
        self.spoken_time = self._get_spoken_time()
        self.total_seconds = self._get_total_seconds()

    def _get_spoken_time(self):
        spoken_time = list()
        spoken_hours = None
        spoken_minutes = None
        spoken_seconds = None

        if self.hours > 0:
            if self.hours > 1:
                spoken_hours = f"{self.hours} hours"
            else:
                spoken_hours = f"{self.hours} hour"
        if self.minutes > 0:
            if self.minutes > 1:
                spoken_minutes = f"{self.minutes} minutes"
            else:
                spoken_minutes = f"{self.minutes} minute"
        if self.seconds > 0:
            if self.seconds > 1:
                spoken_seconds = f"{self.seconds} seconds"
            else:
                spoken_seconds = f"{self.seconds} second"

        if spoken_hours:
            spoken_time.append(spoken_hours)
            if spoken_minutes:
                spoken_time.append(spoken_minutes)
            if spoken_seconds:
                spoken_time.append(spoken_seconds)

        elif spoken_minutes:
            spoken_time.append(spoken_minutes)
            if spoken_seconds:
                spoken_time.append(spoken_seconds)

        elif spoken_seconds:
            spoken_time.append(spoken_seconds)

        if len(spoken_time) == 3:
            self.spoken_time = f"{spoken_time[0]}, {spoken_time[1]} and {spoken_time[2]}"
        elif len(spoken_time) == 2:
            self.spoken_time = f"{spoken_time[0]} and {spoken_time[1]}"
        elif len(spoken_time) == 1:
            self.spoken_time = f"{spoken_time[0]}"

        return self.spoken_time

    def _get_total_seconds(self):
        time = f"{self.hours}:{self.minutes}:{self.seconds}"
        self.total_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))
        return self.total_seconds
