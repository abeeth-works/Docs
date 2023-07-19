import PySimpleGUI as psg
import FileZip_App_functions as fzf

fz_window = fzf.then_there_was_zip('FileZip v1.9', 'Reddit')

while True:
    event, values = fz_window.read()

    # REMOVE ONCE TESTING CONCLUDES
    fz_window['-LABEL-'].update(value=fzf.lets_check(event, values))

    if event == psg.WINDOW_CLOSED:
        break

    if event == '-HI':
        fz_window['-LABEL-'].update(value=event)

fz_window.close()
