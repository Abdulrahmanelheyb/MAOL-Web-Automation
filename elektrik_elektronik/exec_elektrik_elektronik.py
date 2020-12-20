from elektrik_elektronik.eexcel_rw import *
from models.excel import *
from elektrik_elektronik.estudent import *
from models.web_io import *


def e_execute(excelFilePath):
    EStudent.Students = read_excel(excelFilePath, 1)
    read_web(EStudent.Students)
    write_excel(2, "elektrik elektronik")