from bilisim.bexcel_rw import *
from models.excel import *
from models.web_io import *


def b_execute(excelFilePath):
    BStudent.setStudents(read_excel(excelFilePath, 0))
    read_web(BStudent.Students)
    write_excel(2, "Bilisim")
