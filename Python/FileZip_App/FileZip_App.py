import PySimpleGUI as psg
import FileZip_App_functions as fzf
from zipfile import ZipFile

fz_window = fzf.then_there_was_zip('FileZip v1.9', 'Reddit')

while True:
    event, values = fz_window.read()
    # REMOVE POST TESTING
    fz_window['-LABEL-'].update(value=fzf.lets_check(event, values))
    print(f"EVENT: {event} || VALUES: {values}")

    if event == psg.WINDOW_CLOSED:
        break

    if event == '-ZIP-':
        print(values)
        filestring_to_zip = values['-BROWSE_WIN-']
        filepaths_to_zip = filestring_to_zip.split(';')
        destination_filepath = values['-DEST_WIN-']

        # REMOVE POST TESTING
        fz_window['-LABEL-'].update(value=filepaths_to_zip)

        fzf.zip_me(filepaths_to_zip, destination_filepath)

        output = f"Zippo now lives at {destination_filepath}"
        fz_window['-LABEL-'].update(value=output)
        # fz_window['-']
fz_window.close()
