import openpyxl

# 1. specify filepath(s)
path = 'openpyxl_data.xlsx'

# 2. create workbook object using .load_workbook(path)
workbook_object = openpyxl.load_workbook(path)

# 3. get active sheet from workbook object
active_sheet_object = workbook_object.active

# 4. cell object has row, column and coordinate attributes
selected_cell_object = active_sheet_object.cell(row=1, column=1)

cell_value = f"Values extracted from the select cell object are: {selected_cell_object.value}"
print(cell_value)

rows_value = f"Number of rows in the sheet at {path} : {active_sheet_object.max_row}"
print(rows_value)

columns_value = f"Number of columns in the sheet at {path} : {active_sheet_object.max_column}"
print(columns_value)

# Get all column names
number_of_columns = active_sheet_object.max_column
for col_num in range(1, number_of_columns + 1):
    cell_object = active_sheet_object.cell(row=1, column=col_num)
    print(cell_object)