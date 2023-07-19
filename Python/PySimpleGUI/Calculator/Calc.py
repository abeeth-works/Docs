import PySimpleGUI as psg
import Calc_functions as cf

# got carried away - tried to automate creating the buttons: throws below
# AttributeError: 'str' object has no attribute 'ParentContainer'
# def b_dropper(face):
#     return f"psg.Button('{face}', key={face})"

menu = ['menu', ['LightGrey1', 'DarkGray8', 'random']]
calc_window = cf.create_calc('LightGrey1', menu)

while True:
    event, values = calc_window.read()

    # REMOVE AFTER TESTING
    cf.test_function(event, values, calc_window)
    # REMOVE AFTER TESTING

    # Theme settings
    if event in menu[1]:
        print(event)

    if event == psg.WINDOW_CLOSED:
        break
    if event == '7':
        continue

calc_window.close()
