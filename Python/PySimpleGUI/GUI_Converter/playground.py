import PySimpleGUI as psg

# each [] list represents its own line/row

text_this_is = psg.Text('This is a string', enable_events=True, key='-TEXT_1-')
spinner_pick_one = psg.Spin(['first', 'second', 'third'], key='-SPINNER_1-')
button_of_click = psg.Button('Button of Click', key='-BUTTON_1-')
input_blank = psg.Input(key='-INPUT_1-')
text_ending = psg.Text('Ending text')
button_ending = psg.Button('Ending button', key='-BUTTON_2-')

layout = [[text_this_is, spinner_pick_one],
          [button_of_click],
          [input_blank],
          [text_ending, button_ending]]

this_window = psg.Window('Converter', layout)

while True:
    event, values = this_window.read()
    print(f"\n1 . Window event is: {event}")
    print(f"2 . Window values are: {values}")

    if event == psg.WINDOW_CLOSED:
        print(f"## This triggers termination! ##")
        break

    if event == '-BUTTON_1-':
        print(f"## This triggers {event}/event and captures {values}/values ##")

    if event == '-BUTTON_2-':
        print(f"## This triggers {event}/event and captures {values}/values ##")

    if event == '-TEXT_1-':
        print(f"## This triggers {event}/event and captures {values}/values ##")
this_window.close()