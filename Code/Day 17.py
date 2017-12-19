def spin_lock(steps, length):
    lock = [0]
    reps = 0
    pos = 0
    while reps < length:
        reps += 1
        pos = (pos + steps) % len(lock)
        pos += 1
        lock.insert(pos, reps)
    return lock[pos + 1]

# print(spin_lock(359, 2017))

def angry_spin_lock(steps, length):
    val = 0
    reps = 0
    pos = 0
    while reps < length:
        reps += 1
        pos = (pos + steps) % (reps)
        pos += 1
        if pos == 1:
            val = reps
    return val

print(angry_spin_lock(359, 50000000))