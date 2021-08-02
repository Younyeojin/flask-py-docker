import random

import matplotlib.pyplot as plt
# random.randint(1,6)
# range(5)
from modu.template import ChangedTemperaturesOnMyBirthday


def random_dice():
    ls = []
    # [ls.append(i for i in [])]
    [ls.append(random.randint(1, 6)) for i in range(5)]
    return ls


def show_hist(ls):
    plt.hist(ls, bins=6)
    plt.show()


def highest_temperature(month: str):
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    # [print(i) for i in birth.data]
    arr = []
    [arr.append(float(i[-1])) for i in birth.data if i[-1] !='' if i[0].split('-')[1] == month]
    return arr


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='skyblue', label=f'{month}월')
    plt.rc('font', family='Malgun Gothic')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # ls = random_dice(100000)
    # print(ls)
    # show_hist()
    show_hist_about(highest_temperature('11'), month='01')