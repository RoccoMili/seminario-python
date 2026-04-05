import random

def randomizer(friends):
    seen = set()
    shuffled = []

    for raw in friends:
        name = " ".join(raw.strip().split())
        if not name:
            continue
        key = name.lower()
        if key in seen:
            return None
        seen.add(key)
        shuffled.append(name)

    if len(shuffled) < 3:
        return None

    random.shuffle(shuffled)
    assigned = {}
    n = len(shuffled)
    for i in range(n):
        assigned[shuffled[i]] = shuffled[(i+1) % n]
    return assigned
