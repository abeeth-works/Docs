import PySimpleGUI as psg

# got carried away - tried to automate creating the buttons: throws below
# AttributeError: 'str' object has no attribute 'ParentContainer'
# def b_dropper(face):
#     return f"psg.Button('{face}', key={face})"

psg.theme('LightGrey1')  # do this before elements are created
psg.set_options(font='Franklin 15', button_element_size=(3,2))

# psg.Push() will do it in a simpler way [[psg.Push(), calc_display]...]...
calc_display = psg.Text('0', enable_events=True, font='Roboto 40', justification='right', expand_x=True,
                        pad=(10, 20), key='calc_display')

zero = psg.Button('0', key='0')
one = psg.Button('1', key='1')
two = psg.Button('2', key='2')
three = psg.Button('3', key='3')
four = psg.Button('4', key='4')
five = psg.Button('5', key='5')
six = psg.Button('6', key='6')
seven = psg.Button('7', key='7')
eight = psg.Button('8', key='8')
nine = psg.Button('9', key='9')

plus = psg.Button('+', key='+', expand_x=True)
minus = psg.Button('-', key='-')
multip = psg.Button('*', key='*')
div = psg.Button('/', key='/')

equals = psg.Button('=', key='=', expand_x=True)
clear = psg.Button('CE', key='CE', button_color='red')
dec = psg.Button('.', key='.')
toggle = psg.Spin(['light', 'dark'], key='toggle', enable_events=True, expand_x=True)
humble_brag = psg.Text(':: Calc v1.0 ::')

layout = [[calc_display],
          [toggle, humble_brag],
          [equals, clear],
          [seven, eight, nine, div],
          [four, five, six, multip],
          [one, two, three, minus],
          [zero, dec, plus]]

calc_window = psg.Window('Calculator1.0', layout)

while True:
    event, values = calc_window.read()

    # remove after testing
    print(f"\n{event} ::: Events logged"
          f"\n{values} ::: Values captured"
          f"\n --- --- --- ---")
    # remove after testing

    if event == psg.WINDOW_CLOSED:
        break
    if event == '7':
        # grab existing box value and store it
        # what_was = values['calc_display']
        # print(what_was)
        # START HERE 
        continue
calc_window.close()