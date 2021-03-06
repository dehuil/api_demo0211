__author__ = 'lee'
#coding=utf-8
import requests as rs
import unittest
import json
import sys
from utils import read as rd,element_tojson as etj

headers={"Content-Type":"application/json;charset=utf-8","Accept":"application/json"}
case='./cases/case1.xlsx'
shuju=etj(rd(case))
url1=shuju['baseUrl']['url']

class Test(unittest.TestCase):

    def test01(self):
        #获取初中，高中默认科目,正向用例
        case01=shuju['获取初中，高中默认科目']
        url=url1+case01['url']
        data=case01['data']
        rp=rs.post(url,data,headers=headers)
        self.assertEqual(rp.status_code,case01['except'])#校验状态码

    def test02(self):
        #根据学段和科目获取基础题型
        case02=shuju['根据学段和科目获取基础题型']
        url=url1+case02['url']
        data=case02['data']
        rp=rs.post(url,data,headers=headers)
        self.assertEqual(rp.status_code,case02['except'])#校验状态码


    def test03(self):
        #获取文体信息
        case03=shuju['根据学段和科目获取基础题型']
        url=url1+case03['url']
        data=case03['data']
        rp=rs.post(url,data,headers=headers)
        self.assertEqual(rp.status_code,case03['except'])#校验状态码

if __name__ == '__main__':
    unittest.main()

