import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from colorit import *
import xlsxwriter
import os
from os import path


# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Student:
    Students = []

    def __init__(self):
        self._ID = None
        self._firstName = None
        self._lastName = None
        self._studentNo = None
        self._tcNO = None
        self._degrees = dict()

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

    def setDegrees(self, degrees):
        self._degrees = degrees

    def getDegrees(self):
        return self._degrees

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
        workSheet = workBook.sheet_by_index(0)
        ndx = 0
        for i in range(workSheet.nrows):
            std = Student()
            std.setID(ndx)
            std.setStudentNo(int(workSheet.cell_value(i, 0)))
            std.setTcNo(int(workSheet.cell_value(i, 1)))
            std.setFirstName(workSheet.cell_value(i, 2))
            std.setLastName(workSheet.cell_value(i, 3))
            Student.Students.append(std)
            ndx = ndx + 1


def insertStudents(workBookPath):
    workbook = xlsxwriter.Workbook(workBookPath)
    sheet = workbook.add_worksheet("IT")

    for stdNdx in range(len(Student.Students)):
        student = Student.Students[stdNdx]
        sheet.set_column(0, 1, 12)
        sheet.write(stdNdx, 0, Student.Students[stdNdx].getStudentNo())
        sheet.write(stdNdx, 1, Student.Students[stdNdx].getTcNo())
        sheet.write(stdNdx, 2, Student.Students[stdNdx].getFirstName())
        sheet.write(stdNdx, 3, Student.Students[stdNdx].getLastName())
        sheet.write(stdNdx, 4, "BİLİŞİM TEKNOLOJİLERİ ALANI")
        sheet.write(stdNdx, 5, "")
        degrees = student.getDegrees()
        for i in range(len(degrees[0])):

            lessonID = degrees[0][i]
            # BT077 / MESLEKİ GELİŞİM ATÖLYESİ 1
            if lessonID == "BT077":
                sheet.write(i, 8, degrees[4][i])

            # BT049 / PROGRAMLAMA TEMELLERİ 1
            elif lessonID == "BT049":
                sheet.write(i, 8, degrees[4][i])

            # BT079 / PROGRAMLAMA TEMELLERİ 1 (*)
            elif lessonID == "BT079":
                sheet.write(i, 9, degrees[4][i])

            # BT079 / PROGRAMLAMA TEMELLERİ 1 (*)
            elif lessonID == "BT049":
                sheet.write(i, 11, degrees[4][i])

            # BT081 / BİLİŞİM TEKNOLOJİLERİNİN TEMELLERİ 1
            elif lessonID == "BT081":
                sheet.write(i, 10, degrees[4][i])

    if path.exists(workBookPath):
        os.remove(workBookPath)
        workbook.close()
    else:
        workbook.close()


def GetStudentDegrees(bwr: webdriver, student: Student):
    Degrees = [[], [], [], [], [], [], [], [], [], []]
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

        # //*[@id="lblKayitTarihi"] this for get student register date .

        bwr.switch_to.frame("webFrame")

        degreesTable = bwr.find_element(By.XPATH, "//*[@id='grdYuzYuze']")
        rowCount = len(bwr.find_elements(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr")) + 1
        for rowNdx in range(2, rowCount):
            row = degreesTable.find_element(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr[" + str(rowNdx) + "]")

            def getCell(cellIndex):
                cell = row.find_element(By.XPATH,
                                        "//*[@id='grdYuzYuze']/tbody/tr[" + str(rowNdx) + "]/td[" + str(
                                            cellIndex) + "]")
                value = str.strip(cell.text)
                if bool(value):
                    Degrees[cellIndex - 1].append(cell.text)
                    print(color_front(cell.text, 124, 252, 0))
                else:
                    Degrees[cellIndex - 1].append("-")
                    print(color_front("---", 220, 20, 60))

            for i in range(1, 11):
                getCell(i)

            print(color_front(">>>>>>>>> BREAK", 30, 144, 255))
        print(color_front("==============================", 255, 102, 255))
    except NoSuchElementException:
        print("STUDENT DEGREES NOT FOUND !")
        print("STUDENT TCNO : %d" % (student.getTcNo()))
        print("STUDENT NAME : %s \n STUDENT SURNAME : %s" % (student.getFirstName(), student.getLastName()))
        print(color_front("==============================", 255, 102, 255))
    student.setDegrees(Degrees)
    time.sleep(3)
