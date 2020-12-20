from bilisim.exec_bilisim import *
# from makina.exec_makina import *
from elektrik_elektronik.exec_elektrik_elektronik import *
from models.web_io import *
from models.excel import *
import os

# region Globals
excelFilePath = "C:\\Users\\abdul\\Desktop\\2020-2021-yeni-kayıt-listesi-yeni2.xlsx"
workBookWritePath = "C:\\Users\\abdul\\Desktop\\Students-Data.xlsx"
# endregion


try:
    os.system('taskkill /f /im msedgedriver.exe')
except Exception as ex:
    print(ex)

e_begin(workBookWritePath)
w_begin()

b_execute(excelFilePath)
# e_execute(excelFilePath)

w_end()
e_end()
