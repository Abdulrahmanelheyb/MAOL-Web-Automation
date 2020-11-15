import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from colorit import *
import xlsxwriter
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located



class Student:
    _ID = None
    _firstName = None
    _lastName = None
    _studentNo = None
    _tcNO = None
    _degrees = dict()
    Students = []

    def setID(self, Id):
        self._ID = Id

    def getID(self):
        return self._ID

    def setFirstName(self, firstname):
        self._firstName = firstname

    def getFirstName(self):
        return self._firstName

    def setLastName(self, lastname):
        self._lastName = lastname

    def getLastName(self):
        return self._lastName

    def setStudentNo(self, studentno):
        self._studentNo = studentno

    def getStudentNo(self):
        return self._studentNo

    def setTcNo(self, tcno):
        self._tcNO = tcno

    def getTcNo(self):
        return self._tcNO

    def getAllInfo(self):
        return [self._studentNo, self._tcNO, self._firstName, self._lastName]

    def getStudents(self):
        return self.Students

    @staticmethod
    def BeginBrowser():
        bwr = webdriver.Edge("C:\\WebDrivers\\msedgedriver.exe")
        bwr.get(
            "https://mebbisssoyd.meb.gov.tr/ssologinBIDB.aspx?id=3&url=http://aolweb.aol.meb.gov.tr/kurum_giris.aspx")
        username = bwr.find_element(By.ID, "txtKullaniciAd")
        username.send_keys("13889656220")
        password = bwr.find_element(By.ID, "txtSifre")
        password.send_keys("Damlanur1")
        time.sleep(10)
        return bwr

    @staticmethod
    def EndBrowser(bwr: webdriver):
        bwr.quit()

    @staticmethod
    def loadStudents(workBookPath):
        workBook = xlrd.open_workbook(workBookPath)
        workSheet = workBook.sheet_by_index(2)
        ndx = 0
        for i in range(3, workSheet.nrows):
            std = Student()
            std.setID(ndx)
            std.setStudentNo(int(workSheet.cell_value(i, 0)))
            std.setTcNo(int(workSheet.cell_value(i, 1)))
            std.setFirstName(workSheet.cell_value(i, 2))
            std.setLastName(workSheet.cell_value(i, 3))
            Student.Students.append(std)
            ndx = ndx + 1


def insertStudents(workBookPath,std: Student):
    readWBook = xlrd.open_workbook(workBookPath)
    readWSheet = readWBook.get_sheet(0)
    nrow = readWSheet.nrows
    ncol = readWSheet.ncols


    workBook = xlsxwriter.Workbook(workBookPath)
    workSheet = workBook.get_worksheet_by_name("IT")
    workSheet.write_row()


def GetStudentDegrees(bwr: webdriver, student: Student):
    Degrees = []
    try:
        # this condition for no refresh page in first student scraping
        if student.getID() != 0:
            bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")

        tcno = bwr.find_element(By.ID, "txtTCNo")
        tcno.send_keys(student.getTcNo())

        listStdData = bwr.find_element(By.ID, "IMG1")
        listStdData.click()

        selectStd = bwr.find_element(By.XPATH, "//*[@id='grdAramaSonuclar']/tbody/tr[2]/td[1]/a/img")
        selectStd.click()

        degrees = bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[3]/a")
        degrees.click()

        time.sleep(2)
        bwr.switch_to.frame("webFrame")

        degreesTable = bwr.find_element(By.XPATH, "//*[@id='grdYuzYuze']")
        rowCount = len(bwr.find_elements(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr")) + 1
        cellCount = len(bwr.find_elements(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr[2]/td")) + 1
        for rowNdx in range(2, rowCount):
            row = degreesTable.find_element(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr[" + str(rowNdx) + "]")
            for cellNdx in range(1, cellCount):
                cell = row.find_element(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr[" + str(rowNdx) + "]/td[" + str(cellNdx) + "]")
                value = str.strip(cell.text)
                if bool(value):
                    Degrees.append(cell.text)
                    print(color_front(cell.text, 124, 252, 0))
                else:
                    print(color_front("---", 220, 20, 60))
            print(color_front(">>>>>>>>> BREAK", 30, 144, 255))
        print(color_front("==============================", 255, 102, 255))
    except NoSuchElementException:
        print("STUDENT DEGREES NOT FOUND !")
        print("STUDENT TCNO : %d" % (student.getTcNo()))
        print("STUDENT NAME : %s \n STUDENT SURNAME : %s" % (student.getFirstName(), student.getLastName()))
        print(color_front("==============================", 255, 102, 255))
    time.sleep(3)