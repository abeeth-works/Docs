# Docs

All of the reference notes from multiple projects/languages will be categorised in this directory.

> Main use: Mull over and break down necessary topics to build a solid understanding of the concepts/how to use

## Changelog | Point of Reference

### Python

- #### PySimpleGUI for interfaces

    - Installation and setup
    - **Base Unit Converter app** [[repo]](https://github.com/abeeth-works/Docs/tree/7e0565a26237c5609a6b788a0bfff8deb4b0df18/Python/PySimpleGUI/GUI_Converter)
    - **Calculator** app [[repo*]]()
      
      - Window setup _(init, window.read(), window.close())_
      
            import PySimpleGUI as psg
            #  window title goes as the first argument for .window()
            #  layout is [[]] => with each inner [] representing a row
            #  below window is 4 lines tall
            window = psg.Window("TaskMan v1.17",
               layout=[[time_label],
                       [task_list_box],
                       [type_task_label, input_task_box],
                       [add_task_button, edit_task_button, delete_task_button,
                       exit_button]],
                       font=('Helvetica', 20))
            while True:
                event, values = window.read()
                if event == psg.WIN_CLOSED:
                    break
            window.close()
      
      - Layouts
      
        - Generating through lists [**DISPLAY**] [[repo]](https://github.com/abeeth-works/Docs/blob/1da164f90e281afe707d38f207f8ac273fdf0f1a/Python/PySimpleGUI/Calculator/Calc.py)
                        
              button_labels = ['0', '1', '2', '3', '4']
              my_layout = []
              for label in button_labels:
                  my_layout.append([psg.Button(label, key=label)])
              
              layout = my_layout
        
        - Columns with **psg.Column(column_stuff)**
        
              import PySimpleGUI as sg

              # Prepare the widgets for the left column
              left_column_content = [[sg.Text('Left 1')],
                                     [sg.Text('Left 2')]]

              # Prepare the widgets for the right column
              right_column_content = [[sg.Text('Right 1')],
              [sg.Text('Right 2')]]

              # Construct the Column widgets
              left_column = sg.Column(left_column_content)
              right_column = sg.Column(right_column_content)

              # Construct the layout
              layout = [[left_column, right_column]]

              # Construct and display the window
              window = sg.Window('Columns', layout)
              window.read()
              window.close()
 
      - Events and Values
      - Theming **(psg.theme(), psg.set_options())**
    - **Task Manager App** for 60 Days [[repo]](https://github.com/abeeth-works/Task-Manager-GUI-App.git)
    - **Creating executables**
    >

- CSV Processing

    - Basics


- XLSX Processing

    - Openpyxl