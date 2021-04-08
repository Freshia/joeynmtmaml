import random
import string
import numpy as np

np.random.seed(42)

def generate_samples(n=10000, maxlen=10):
    #generate random string made up of lowercase letters
    samples = []
    chars = list(string.ascii_lowercase)
    chars = chars[:9]
    for i in range(n):
        size = np.random.randint(1, maxlen + 1)
        sample = ''.join((random.choice(chars) for x in range(size)))
        samples.append(sample)
    return samples

def ordinal_text(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += str(ord(char) - 97)
    return result

def sample_to_str(sample):
    return " ".join(map(str, sample))


def save_samples(samples, prefix="train", ext="src", ordinal=False):
    with open(prefix + "." + ext, mode="w") as f:
        for sample in samples:
            sample = ordinal_text(sample) if ordinal else sample
            f.write(sample_to_str(sample) + "\n")


def generate_task(train="train", dev="dev", test="test", src="src", trg="trg"):

    # train
    samples = generate_samples(50000, maxlen=25)
    save_samples(samples, prefix=train, ext=src, ordinal=False)
    save_samples(samples, prefix=train, ext=trg, ordinal=True)

    # dev
    samples = generate_samples(1000, maxlen=30)
    save_samples(samples, prefix=dev, ext=src, ordinal=False)
    save_samples(samples, prefix=dev, ext=trg, ordinal=True)

    # test
    samples = generate_samples(1000, maxlen=30)
    save_samples(samples, prefix=test, ext=src, ordinal=False)
    save_samples(samples, prefix=test, ext=trg, ordinal=True)


if __name__ == "__main__":
    generate_task()