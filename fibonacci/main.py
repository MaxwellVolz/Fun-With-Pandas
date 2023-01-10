import matplotlib.pyplot as plt


def make_sequence(amt):
    sequence = [0, 1]

    for x in range(amt):
        sequence.append(sequence[x] + sequence[x + 1])

    return sequence


z = make_sequence(20)
print(z)

plt.plot(z)
plt.show(block=True)
