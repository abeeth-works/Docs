import PySimpleGUI as psg


def test_function(event, values, window_name):
    window_name['log'].update(f"Event - {event} || Values - {values}")
    print(f"Event - {event} ||| Values - {values}")


def create_calc(theme, menu):
    psg.theme(theme)  # do this before elements are created
    psg.set_options(font='Franklin 15', button_element_size=(3, 2))

    # psg.Push() will do it in a simpler way [[psg.Push(), calc_display]...]... vs pad=(x,y)

    layout = [[psg.Text('0',
                        enable_events=True,
                        font='Roboto 40',
                        justification='right',
                        expand_x=True,
                        pad=(10, 20),
                        key='calc_display',
                        right_click_menu=menu)],
              # [psg.Spin(['light', 'dark'],
              #           key='toggle',
              #           enable_events=True,
              #           expand_x=True),
              [psg.Text('', key='log')],
              [psg.Button('=', key='=', expand_x=True), psg.Button('CE', key='CE', button_color='red')],
              [psg.Button('7', key='7'), psg.Button('8', key='8'), psg.Button('9', key='9'), psg.Button('/', key='/')],
              [psg.Button('4', key='4'), psg.Button('5', key='5'), psg.Button('6', key='6'), psg.Button('*', key='*')],
              [psg.Button('1', key='1'), psg.Button('2', key='2'), psg.Button('3', key='3'), psg.Button('-', key='-')],
              [psg.Button('0', key='0'), psg.Button('.', key='.'), psg.Button('+', key='+', expand_x=True)]]
    return psg.Window('Calc v1.0', layout)