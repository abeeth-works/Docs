import zipfile

import PySimpleGUI as psg


def lets_check(event, values):
    output = f"\nEvent is {event} // Values are {values}"
    return output


def then_there_was_zip(name, theme):
    psg.theme(theme)  # random works but not best practice
    psg.set_options(font='Franklin 15',
                    button_element_size=(2,1))

    layout=[[psg.Text('', key='-LABEL-')],
            [psg.Text('Select files to compress:'),
             psg.Input(key='-BROWSE_WIN-'),
             psg.FilesBrowse('Browse',
                          key='-BROWSE-')],
            [psg.Text('Select destination folder:'),
             psg.Input(key='-DEST_WIN-'),
             psg.FolderBrowse('Set',
                              key='-DEST-')],
            [psg.Button('Zip!', key='-ZIP-')]]

    return psg.Window(name, layout)


def zip_me(filepaths_to_zip, destination_filepath):
    openfile_arg = f"{destination_filepath}/zippo.zip"

    with zipfile.ZipFile(openfile_arg, 'w') as archive:
        for filepath in filepaths_to_zip:
            archive.write(filepath)
