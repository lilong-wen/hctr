import os
import random
import math

random.seed(0)

def split_dataset(label_path):

    train_rate = 0.7
    val_rate = 0.2
    test_rate = 0.1

    if not os.path.exists(label_path):
        print('label path not exis!')
        return

    lines = open(label_path).read().splitlines()

    random.shuffle(lines)
    totle_num = len(lines)

    a = int(totle_num * train_rate)
    b = math.ceil(totle_num * val_rate)
    c = totle_num - a - b

    if not os.path.exists(os.path.join(os.path.dirname(label_path), 'cv1')):
        os.mkdir(os.path.join(os.path.dirname(label_path), 'cv1'))

    f_train = open(os.path.join(os.path.dirname(label_path), 'cv1','train.txt'), 'w')
    f_val = open(os.path.join(os.path.dirname(label_path),'cv1', 'valid.txt'), 'w')
    f_test = open(os.path.join(os.path.dirname(label_path), 'cv1', 'test.txt'), 'w')

    for i, line in enumerate(lines):
        i += 1
        print(f"{i}:{line}")
        if i <= a:
            f_train.write(line.split()[0] + "\n")
        elif i > a and i <= a+b:
            f_val.write(line.split()[0] + "\n")
        else:
            f_test.write(line.split()[0] + "\n")

