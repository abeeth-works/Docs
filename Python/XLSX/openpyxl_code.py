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