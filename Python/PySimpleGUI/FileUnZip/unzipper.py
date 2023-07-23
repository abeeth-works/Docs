import  PySimpleGUI as psg
import unzipper_functions as uzf

unzip_window = uzf.setup_gui('Unzipper v1.0', 'Reddit')

while 1:
    # set to refresh every 0.5 min
    event, values = unzip_window.read(timeout=3000)
    uzf.give_time(unzip_window)
    uzf.test_logger(event, values, unzip_window)

    if event == '-UNZIP-':
        filepath_to_unzip = values['-BROWSE_WIN-']
        destination = values['-BROWSE-DEST-']
        uzf.run_unzip(filepath_to_unzip, destination)

    if event == '-RESET-':
        unzip_window['-LABEL-'].update(value='')
        unzip_window['-BROWSE-DEST-'].update(value='')

    if event == psg.WINDOW_CLOSED:
        break

    if event == '-EXIT-':
        break
    else:
        continue

unzip_window.close()