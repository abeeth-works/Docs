## Using Openpyxl for excel ops

> Links to Grocery POS App found in [this repo](https://github.com/abeeth-works/Grocery-POS-inventory/blob/ed6ab2013e4e80fc9b9eb644a8008b618e944aae/README.md)

1. Install and setup Openpyxl: [instructions here](#)
2. Where native xlsx app is not available - use Google or similar 
online office platform to generate the excel files and manually place
them in the app directory

### Reading Excel sheets
    import openpyxl

    # 1. specify filepath(s)
    path = 'openpyxl_data.xlsx'

    # 2. create workbook object using .load_workbook(path)
    workbook_object = openpyxl.load_workbook(path)

    # 3. get active sheet from workbook object
    active_sheet_object = workbook_object.active

    # 4. cell object has row, column and coordinate attributes
    selected_cell_object = active_sheet_object.cell(row = 1, column = 1)

    print(selected_cell_object.value)

returns
> Item_Code

