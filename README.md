# Docs

All of the reference notes from multiple projects/languages will be categorised in this directory.

> Main use: Mull over and break down necessary topics to build a solid understanding of the concepts/how to use

## Changelog | Point of Reference

### Python
- CSV Processing

    - Basics   


- XLSX Processing

    - Openpyxl


- PySimpleGUI for interfaces

    - Installation and setup
    - Base Unit Converter app [[repo]](https://github.com/abeeth-works/Docs/tree/7e0565a26237c5609a6b788a0bfff8deb4b0df18/Python/PySimpleGUI/GUI_Converter)
    - Calculator app [[repo*]]()
      
      - Window setup _(init, window.read(), window.close())_
      - Layouts
      
        - Generating through lists [**DISPLAY**] [[repo]](https://github.com/abeeth-works/Docs/blob/1da164f90e281afe707d38f207f8ac273fdf0f1a/Python/PySimpleGUI/Calculator/Calc.py)
                        
              button_labels = ['0', '1', '2', '3', '4']
              my_layout = []
              for label in button_labels:
                  my_layout.append([psg.Button(label, key=label)])
              
              layout = my_layout
        
      - Events and Values
      - Theming **(psg.theme(), psg.set_options())**
    - Task Manager app for 60 Days [[repo]](https://github.com/abeeth-works/Task-Manager-GUI-App.git)