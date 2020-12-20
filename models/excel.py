import xlsxwriter
import xlrd
import os
from os import path

_workbook: xlsxwriter.workbook.Workbook = None
_wpath: str = None


def read_excel(workBookPath, SheetNdx: int) -> list:
    Students = []
    workBook = xlrd.open_workbook(workBookPath)
    workSheet = workBook.sheet_by_index(SheetNdx)
    ndx = 0
    for i in range(workSheet.nrows):
        std = dict(
            ID=ndx,
            studentNo=int(workSheet.cell_value(i, 0)),
            tcNO=int(workSheet.cell_value(i, 1)),
            firstName=workSheet.cell_value(i, 2),
            lastName=workSheet.cell_value(i, 3)
        )
        Students.append(std)
        ndx = ndx + 1
    return Students


def getWorkBook():
    global _workbook
    wk = _workbook
    return wk


def e_begin(workBookPath) -> xlsxwriter.workbook.Workbook:
    global _wpath
    global _workbook
    _wpath = workBookPath
    _workbook = xlsxwriter.Workbook(workBookPath)
    return _workbook


def e_end():
    global _workbook
    if path.exists(_wpath):
        os.remove(_wpath)
        _workbook.close()
    else:
        _workbook.close()
