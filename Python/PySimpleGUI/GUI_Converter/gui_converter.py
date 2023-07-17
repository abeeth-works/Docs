import PySimpleGUI as psg

textbox_input = psg.Input(key='-INPUT-')
spinner_units = psg.Spin(['KM -> M', 'M -> CM', 'CM -> MM'], key='-SPINNER-')
button_convert = psg.Button('Convert', key='-BUTTON-')
label_output = psg.Text('Output: ')
label_result = psg.Text(' ', key='-LABEL-')

layout = [[textbox_input, spinner_units, button_convert],
          [label_output, label_result]]

converter_window = psg.Window('Basic Unit Converter1.0', layout)

while True:
    event, values = converter_window.read()

    if event == '-SPINNER-':
        print(values['-SPINNER-'])

    if event == '-BUTTON-':
        grab_value = values['-INPUT-']
        print(grab_value)

    if event == psg.WINDOW_CLOSED:
        print('terminate called')
        break

converter_window.close()