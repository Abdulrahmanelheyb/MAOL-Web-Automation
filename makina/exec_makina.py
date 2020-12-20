from makina.mexcel_rw import *
from models.excel import *
from makina.mstudent import *
from models.web_io import *


def m_execute(excelFilePath):
    MStudent.Students = read_excel(excelFilePath)
    read_web(MStudent.Students)
    write_excel(2, "makina")