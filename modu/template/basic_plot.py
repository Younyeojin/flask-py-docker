import matplotlib.pyplot as plt

from common.menu import print_menu

"""
list 값은 y축 이고, x축은 0부터 1까지 자동으로 증가한다.
"""


def plot_show():
    plt.title('plotting')
    plt.plot([10, 20, 30, 40])
    plt.show()


"""
첫번째 list 가 x축 이고, 두번째 list 가 y축 이다.
"""


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


def plot_legend():
    plt.title('legend')
    plt.plot([10, 20, 30, 40], label='asc')
    plt.plot([40, 30, 20, 10], label='desc')
    plt.legend()
    plt.show()


def plot_change_color():
    plt.title('color')
    plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
    plt.plot([40, 30, 20, 10], 'pink', label='pink')
    plt.legend()
    plt.show()


def plot_line_style():
    plt.title('linestyle')
    plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
    plt.plot([40, 30, 20, 10], color='g', ls=':', label='dotted')
    plt.legend()
    plt.show()


def scatter():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()



