# coding=utf-8
# @Time    : 2019/8/30 17:07
# @Author  : Mandy
import json

import xlrd
from xlutils.copy import copy

import conftest
from testcases.test_method import RunMain


class Sheet:
    def __init__(self):
        self.filename = conftest.sheet_dir
        self.workbook = xlrd.open_workbook(self.filename)

    """获取表单"""
    def get_sheet(self, i=0):
        sheet = self.workbook.sheets()[i]
        return sheet

    """获取有效行数"""
    def get_rows(self):
        rows = self.get_sheet().nrows
        return rows

    """获取有效列数"""
    def get_cols(self):
        cols = self.get_sheet().ncols
        return cols

    """获取单元格"""
    def get_cell(self, row_num, col_num):
        cell = self.get_sheet().cell_value(row_num, col_num)
        return cell

    """写入数据"""
    def write_data(self, row_num, write_data):
        wb = copy(self.workbook)
        ws = wb.get_sheet(0)
        ws.write(row_num, 10, write_data)
        wb.save(self.filename)

    """发起请求"""
    def get_result(self, row_num):
        id = self.get_cell(row_num, 0)
        module = self.get_cell(row_num, 1)
        url = self.get_cell(row_num, 2)
        method = self.get_cell(row_num, 3)
        header = self.get_cell(row_num, 4)
        is_depend = self.get_cell(row_num, 5)
        depend_data = self.get_cell(row_num, 6)
        depend_param = self.get_cell(row_num, 7)
        request_data = self.get_cell(row_num, 8)
        expect = self.get_cell(row_num, 9)
        actual = self.get_cell(row_num, 10)
        result = None
        if method == 'get':
            run = RunMain('GET', url, None)
            result = json.loads(run.res)
        elif method == 'post':
            run = RunMain('POST', url, request_data)
            result = json.loads(run.res)
        else:
            print("没有执行")
        # assert len(expect) == len(actual)
        print(result)
        self.write_data(row_num, str(result))


if __name__ == '__main__':
    sheet = Sheet()
    print(sheet.get_result(1))



