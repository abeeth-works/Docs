import PySimpleGUI as psg

# each [] list represents its own line/row
layout = [[psg.Text('String of text'), psg.Spin(['item 1', 'item 2'])],  # top row
          [psg.Button('Button of click')],
          [psg.Input()],
          [psg.Text('Test'), psg.Button('Test Button')]]

this_window = psg.Window('Converter', layout)

while True:
    event, values = this_window.read()
    print(f"\n1 . Window event is: {event}")
    print(f"2 . Window values are: {values}")

    if event == psg.WINDOW_CLOSED:
        print(f"## This triggers termination! ##")
        break

    if event == 'Button of click':
        print(f"## This triggers {event}/event and captures {values}/values ##")

this_window.close()