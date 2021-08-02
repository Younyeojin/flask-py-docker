import random

import matplotlib.pyplot as plt

# 모두의 데이터 분석 p.77~82

def hist_show():
    plt.hist([1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 10])
    plt.show()


def random_dice():
    dice = []
    [dice.append(random.randint(1, 6)) for i in range(10000)]
    print(dice)
    return dice
    # print(random.randint(1, 6))


def hist_dice(dice):
    plt.hist(dice, bins=6)
    plt.show()


if __name__ == '__main__':
    hist_show()
    hist_dice(random_dice())