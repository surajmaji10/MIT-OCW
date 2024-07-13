
import random
import pylab


def coin_toss():
    return random.choice([0, 1])


def coin_flip_trials(min_exp, max_exp):
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    ratios = []
    diffs = []
    print(x_axis)
    for num_throws in x_axis:
        heads = 0
        for throwing in range(num_throws):
            # if coin_toss() == 1:
            if random.random() < 0.5:
                heads += 1
        tails = num_throws - heads
        tails = max(1, tails)
        ratio = float(heads)/float(tails)
        diff = abs(heads-tails)
        ratios.append(ratio)
        diffs.append(diff)

    pylab.figure("figure-1")
    pylab.title("Ratios of heads to tails")
    pylab.xlabel("Ratio")
    pylab.ylabel("Num of throws")
    pylab.plot(x_axis, ratios, "bo")
    # pylab.semilogx()
    # pylab.semilogy()

    pylab.figure("figure-2")
    pylab.title("Diffs of heads to tails")
    pylab.xlabel("Difference")
    pylab.ylabel("Num of throws")
    pylab.plot(x_axis, diffs, "ro")
    # pylab.semilogx()
    # pylab.semilogy()

    pylab.show()


coin_flip_trials(10, 20)

