# -*- coding: utf-8 -*-
import os
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import xlwt
date = ['0530','0609','0624','0725','0826','0925']
FileFolder = '.\\DATA\\sheet1\\'

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook('E:\pycharm project\movies.xls')
    # 获取所有sheet
    # print workbook.sheet_names() # [u'sheet1', u'sheet2']
    #获取sheet2
    sheet2_name= workbook.sheet_names()[1]
    # print sheet2_name
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_name('Sheet2')
    # sheet的名称，行数，列数
    # print sheet2.name,sheet2.nrows,sheet2.ncols
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(2) # 获取第三列内容
    # print rows
    # print cols
    # #获取单元格内容的三种方法
    # print sheet2.cell(1,0).value.encode('utf-8')
    # print sheet2.cell_value(1,0).encode('utf-8')
    # print sheet2.row(1)[0].value.encode('utf-8')
    # # 获取单元格内容的数据类型
    # print sheet2.cell(1,3).ctype

for datenow in date:
    
    # work_book=xlwt.Workbook(encoding='utf-8')
    
    # sheet=work_book.add_sheet('sheet表名')
    # work_book.save(''.join([FileFolder,datenow,'.xls']))
    workbook = xlrd.open_workbook(''.join([FileFolder,datenow,'.xls']))
    sheet = workbook.sheet_by_name('sheet表名')
