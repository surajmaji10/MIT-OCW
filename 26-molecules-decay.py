import matplotlib
import pylab

def molecules_decay(num_molec, prob_decay, num_steps):
    molecules_count = []
    for step in range(0, num_steps + 1):
        molecules_count.append(num_molec * (1 - prob_decay) ** step)
    print(molecules_count)
    pylab.plot(molecules_count, "ro")

molecules_decay(100000, 0.05, 100)

