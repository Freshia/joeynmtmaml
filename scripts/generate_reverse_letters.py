import random
import string
import numpy as np

np.random.seed(42)

def generate_samples(n=10000, maxlen=10):
    #generate random string made up of lowercase letters
    samples = []
    for i in range(n):
        size = np.random.randint(1, maxlen + 1)
        sample = ''.join((random.choice(string.ascii_lowercase) for x in range(size)))
        samples.append(sample)
    return samples

def reverse_text(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((97+25) - (ord(char) - 97))
    return result

def sample_to_str(sample):
    return " ".join(map(str, sample))


def save_samples(samples, prefix="train", ext="src", reverse=False):
    with open(prefix + "." + ext, mode="w") as f:
        for sample in samples:
            sample = reverse_text(sample) if reverse else sample
            f.write(sample_to_str(sample) + "\n")


def generate_task(train="train", dev="dev", test="test", src="src", trg="trg"):

    # train
    samples = generate_samples(50000, maxlen=25)
    save_samples(samples, prefix=train, ext=src, reverse=False)
    save_samples(samples, prefix=train, ext=trg, reverse=True)

    # dev
    samples = generate_samples(1000, maxlen=30)
    save_samples(samples, prefix=dev, ext=src, reverse=False)
    save_samples(samples, prefix=dev, ext=trg, reverse=True)

    # test
    samples = generate_samples(1000, maxlen=30)
    save_samples(samples, prefix=test, ext=src, reverse=False)
    save_samples(samples, prefix=test, ext=trg, reverse=True)


if __name__ == "__main__":
    generate_task()