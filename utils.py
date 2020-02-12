__author__ = 'lee'
#coding=utf-8
import xlrd
import unittest
#读xlsx
def read(filename):
    data_list=[]
    workbook=xlrd.open_workbook(filename)
    sheetnames=workbook.sheet_names()
    for sheetname in sheetnames:
        data=workbook.sheet_by_name(sheetname)
        rows=data.nrows
        for i in range(0,rows):
            data_list.append(data.row_values(i))
    return data_list

#转json
def element_tojson(element):
    elements={}
    for e in element:
        elements[e[0]]={'method':e[1],'url':e[2],'data':e[3],'except':e[4]}
    return elements

if __name__ == '__main__':
    print(read('./case1.xlsx'))
    print(element_tojson(read('./case1.xlsx')))
    print(element_tojson(read('./case1.xlsx'))[ '获取初中，高中默认科目'])