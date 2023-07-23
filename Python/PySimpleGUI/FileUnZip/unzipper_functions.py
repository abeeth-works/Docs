import PySimpleGUI as psg
import zipfile
import time

def test_logger(event, values, win_name):
    """ Logs events/values on app screen + console """
    win_name['-LABEL-'].update(value=f"event:: {event}\nValues:: {values}")
    print(f"event:: {event}\nValues:: {values}")

def setup_gui(name, theme):
    """ Sets up in following layout\n\n

    layout = [[psg.Text('', key='-LABEL-')],
              [psg.Text('Select zip file to unzip:'),
               psg.Input(key='-BROWSE_WIN-'),
               psg.FileBrowse('Browse File', key='-BROWSEFL-', initial_folder='/')],
              [psg.Text('Select destination folder:'),
               psg.Input(key='-BROWSE-DEST-'),
               psg.FolderBrowse('Browse Dest', key='-BROWSEFD-')],
              [psg.Button('Unzip', key='-UNZIP-'),
               psg.Button('Reset', key='-RESET-'),
               psg.Button('Exit', key='-EXIT-')]]
     """
    psg.theme(theme)
    psg.set_options(font='Franklin 15',
                    button_element_size=(2,1))
    layout = [[psg.Text('', key='-LABEL-')],
              [psg.Text('Select zip file to unzip:'),
               psg.Input(key='-BROWSE_WIN-'),
               psg.FileBrowse('Browse File', key='-BROWSEFL-', initial_folder='/')],
              [psg.Text('Select destination folder:'),
               psg.Input(key='-BROWSE-DEST-'),
               psg.FolderBrowse('Browse Dest', key='-BROWSEFD-')],
              [psg.Button('Unzip', key='-UNZIP-'),
               psg.Button('Reset', key='-RESET-'),
               psg.Button('Exit', key='-EXIT-')]]
    return psg.Window(name, layout)


def run_unzip(filepath_to_unzip, destination_to_unzip):

    with zipfile.ZipFile(filepath_to_unzip, 'r') as arch:
        arch.extractall(destination_to_unzip)


def give_time(window):
    window['-LABEL-'].update(value=time.strftime('%b %d, %Y %H:%M'))

