
import random
import time

def roll_die():
    choice = random.choice([1, 2, 3, 4, 5, 6])
    return choice


def check_pascal(num_trials = 1000):
    successes = 0.0
    for trial in range(num_trials):
        for throwing in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                successes += 1
                break
    p_succ = successes / num_trials
    p_fail = 1 - p_succ
    print("Success: {} and Failure: {}".format(p_succ, p_fail))


# 1 million samples
start = time.time()
check_pascal(1000000)
end = time.time()
print("Took:", (end-start), "sec")
p_failure = (35.0 / 36.0) ** 24
print("Failure (by failure):", p_failure)

