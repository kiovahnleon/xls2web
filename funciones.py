import xlrd

# punto 1
def num_hojas(pagina):
    book = xlrd.open_workbook(pagina)
    return book.nsheets

# punto 2
def count_row_col(pagina, num_hoja):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    num_rows = sheet.nrows
    num_cols = sheet.ncols
    return (num_rows, num_cols)

# punto 3
def get_cell_value(pagina, num_hoja, row, col):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    cell_value = sheet.cell_value(row, col)
    return cell_value

# punto 4
def get_col(pagina, num_hoja, col):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    col_values = sheet.col_values(col)
    return col_values

# punto 5
def verify_col(pagina, num_hoja, col, cabecera):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    cabecera_col = sheet.cell_value(0, col)
    return cabecera_col == cabecera

# punto 6
def get_multiple_cols(pagina, num_hoja, cols):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    cols_content = []
    for col in cols:
        col_content = sheet.col_values(col)
        cols_content.append(col_content)
    return cols_content

# punto 7
def ord_matrix(pagina, num_hoja):
    book = xlrd.open_workbook(pagina)
    sheet = book.sheet_by_index(num_hoja)
    data = []
    for row in range(sheet.nrows):
        row_data = []
        for col in range(sheet.ncols):
            row_data.append(sheet.cell_value(row, col))
        data.append(row_data)
    return data
