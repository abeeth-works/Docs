import openpyxl

path = 'openpyxl_data.xlsx'  # 1. specify filepath(s)
workbook_object = openpyxl.load_workbook(path)  # 2. create workbook object using .load_workbook(path)
active_sheet_object = workbook_object.active  # 3. get active sheet from workbook object
selected_cell_object = active_sheet_object.cell(row=1, column=1)  # 4. cell object has row, column and coordinate attributes

cell_value = f"Values extracted from the select cell object are: {selected_cell_object.value}"
# print(cell_value)

rows_value = f"Number of rows in the sheet at {path} : {active_sheet_object.max_row}"
# print(rows_value)

columns_value = f"Number of columns in the sheet at {path} : {active_sheet_object.max_column}"
# print(columns_value)

number_of_columns = active_sheet_object.max_column  # 4. cell object has row, column and coordinate attributes
# for col_num in range(1, number_of_columns + 1):
#     cell_object = active_sheet_object.cell(row=1, column=col_num)
#     print(cell_object)

for row in active_sheet_object.iter_rows():
    for cell in row:
        print(f'{row}/{cell.value}')