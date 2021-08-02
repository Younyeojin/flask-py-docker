from common.menu import print_menu
from modu.template.basic_plot import plot_show, plot_two_list_show, plot_legend, plot_change_color, plot_line_style,  scatter
from modu.template.changed_temperatures_on_my_birthday import ChangedTemperaturesOnMyBirthday

if __name__ == '__main__':
    while 1:
        menu = print_menu(['Exit', 'plot Show', 'plot_two_list_show', 'plot_legend', 'plot_change_color', 'plot_line_style',
                           'scatter', 'Dataframe to CSV', 'ChangedTemperaturesOnMyBirthday'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_legend()
        elif menu == 4:
            plot_change_color()
        elif menu == 5:
            plot_line_style()
        elif menu == 6:
            scatter()
        elif menu == 7:
            ChangedTemperaturesOnMyBirthday().processing()
