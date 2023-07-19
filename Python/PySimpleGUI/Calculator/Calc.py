import PySimpleGUI as psg
import Calc_functions as cf

# got carried away - tried to automate creating the buttons: throws below
# AttributeError: 'str' object has no attribute 'ParentContainer'
# def b_dropper(face):
#     return f"psg.Button('{face}', key={face})"

menu = ['menu', ['LightGrey1', 'DarkGray8', 'random']]
calc_window = cf.create_calc('LightGrey1', menu)

display_num = []
operator_order = []

while True:
    event, values = calc_window.read()

    # REMOVE AFTER TESTING
    # cf.test_function(event, values, calc_window)
    # REMOVE AFTER TESTING

    # Theme settings
    if event in menu[1]:
        calc_window.close()  # close current window
        calc_window = cf.create_calc(event, menu)  # reopen with theme

    # close program
    if event == psg.WINDOW_CLOSED:
        break

    # display
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        display_num.append(event)
        num_string = ''.join(display_num)  # explore
        calc_window['calc_display'].update(num_string)

    # operators
    if event in ['+', '-', '*', '/']:
        operator_order.append(''.join(display_num))
        # reset display number
        display_num = []
        operator_order.append(event)
        calc_window['calc_display'].update('')
        calc_window['log'].update(operator_order)

    # reset
    if event == 'CE':
        display_num = []
        operator_order = []
        calc_window['calc_display'].update('0')
        calc_window['log'].update('0')

    # enter
    if event == '=':
        operator_order.append(''.join(display_num))
        result = eval(''.join(operator_order))
        calc_window['calc_display'].update(result)

        operator_order = []

calc_window.close()
