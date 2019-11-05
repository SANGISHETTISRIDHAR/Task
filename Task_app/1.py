from os.path import isfile

import xlrd
from datetime import datetime,date

def import_xls_to_db(filepath):
    """ Imports data from .xls to db"""
    first_row = 1
    if isfile(filepath):
        book = xlrd.open_workbook(filepath, encoding_override='cp1252')
        sheet = book.sheet_by_index(1)
        nr_rows = sheet.nrows
        for row in range(first_row, nr_rows):
            row_value_list = [cell.value for cell in sheet.row(row)]
            a,b,c,d,e,f,g,h,i,j,k=tuple(row_value_list)
            a_dt=date.fromordinal(date(1900,1,1).toordinal()+int(a)-2)
            b_dt=date.fromordinal(date(1900,1,1).toordinal()+int(b)-2)
            print(a_dt,b_dt)
import_xls_to_db('C:\\Users\\sangishetti sridhar\\Downloads\\template.xlsx')

            # if (type(model_mapping) == dict):
            #     da = zip(model_mapping.keys(), row_value_list)
            #     data = dict([(i[0], model_mapping[i[0]](i[1])) for i in da])
            # else:
            #     data = dict(zip(model_mapping, row_value_list))
            # print(data)
            # obj = model(**data)
            # obj.save()
            # msg = "imported %s" % data
            # # logger.info(msg)

# wb = xlrd.open_workbook('C:\\Users\\sangishetti sridhar\\Downloads\\template.xlsx')
# # sh = wb.sheet_by_index(1)
# # for i in range(10):
# #     cell_value_class = sh.cell(i,2).value
# #     cell_value_id = sh.cell(i,0).value
# #     print(cell_value_class)
# #     print(cell_value_id)
# d = {}
# wb = xlrd.open_workbook('C:\\Users\\sangishetti sridhar\\Downloads\\template.xlsx')
# sh = wb.sheet_by_index(1)
# r=sh.nrows
# for row in range(1,r):
#     St_Date=(sh.cell(row,0).value)
#     print((St_Date))

# for i in range(11):
#     cell_value_col = sh.cell(i,0).value
#     cell_value_row = sh.cell(i,1).value
#     d[cell_value_class] = cell_value_id
# print(d)