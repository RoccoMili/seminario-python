def to_seconds(mss):
    minutes, seconds = mss.split(":")
    return int(minutes) * 60 + int(seconds)

def format_seconds(total):
    formatted = f"{total // 60}m {total % 60:02d}s"
    return formatted

def analyze(playlist):
    total = 0
    ordered = sorted(playlist, key=lambda song: to_seconds(song["duration"]))

    for song in ordered:
        total += to_seconds(song["duration"])
    format_seconds(total)

    return format_seconds(total), ordered[-1], ordered[0]