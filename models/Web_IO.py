from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
import time


# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

class WebIO:

    bwr: webdriver.Edge = None
    webIsBegined = False

    @staticmethod
    def Start(DriverPath: str):
        WebIO.bwr = webdriver.Edge(DriverPath)
        WebIO.bwr.get(
            "https://mebbisssoyd.meb.gov.tr/ssologinBIDB.aspx?id=3&url=http://aolweb.aol.meb.gov.tr/kurum_giris.aspx")
        username = WebIO.bwr.find_element(By.ID, "txtKullaniciAd")
        username.send_keys("13889656220")
        password = WebIO.bwr.find_element(By.ID, "txtSifre")
        password.send_keys("Damlanur1")
        time.sleep(10)
        WebIO.webIsBegined = True

    @staticmethod
    def read_web(students: list):

        for student in students:
            Degrees = []
            try:
                # this condition for no refresh page in first student scraping
                if student.getID() != 0:
                    WebIO.bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")
                else:
                    if bool(WebIO.webIsBegined):
                        WebIO.bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")

                tcno = WebIO.bwr.find_element(By.ID, "txtOgrenciNo")
                tcno.clear()
                tcno.send_keys(student.getStudentNo())

                listStdData = WebIO.bwr.find_element(By.ID, "IMG1")
                listStdData.click()

                selectStd = WebIO.bwr.find_element(By.XPATH, "//*[@id='grdAramaSonuclar']/tbody/tr[2]/td[1]/a/img")
                selectStd.click()

                goto_register_date_menu = WebIO.bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[9]/a")
                goto_register_date_menu.click()

                register_date = WebIO.bwr.find_element(By.XPATH, "//*[@id='lblKayitTarihi']")
                student.setRegisterDate(register_date.text)

                degreesMenu = WebIO.bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[3]/a")
                degreesMenu.click()

                time.sleep(2)

                WebIO.bwr.switch_to.frame("webFrame")

                degreesTable = WebIO.bwr.find_element(By.XPATH, "//*[@id='grdYuzYuze']")
                rowCount = len(WebIO.bwr.find_elements(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr")) + 1

                for rowNdx in range(2, rowCount):
                    row = degreesTable.find_element(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr[" + str(rowNdx) + "]")

                    def getCell(cellIndex):
                        cell = row.find_element(By.XPATH,
                                                "//*[@id='grdYuzYuze']/tbody/tr[" + str(rowNdx) + "]/td[" + str(
                                                    cellIndex) + "]")
                        value = str.strip(cell.text)
                        if bool(value):
                            value = value.replace(",", ".")
                            return value
                        else:
                            return "-"

                    Degrees.append(dict(
                        LessonName=getCell(2),
                        Score=getCell(5)
                    ))

            except NoSuchElementException:
                print("STUDENT DEGREES NOT FOUND !")
                print(f'STUDENT ID {student.getStudentNo()}')
                print(f'STUDENT TCNO : {student.getTcNo()}')
                print(f'STUDENT FULLNAME : {student.getFirstName()} {student.getLastName()}')
                print("==============================")
            except UnexpectedAlertPresentException as e:
                print("Alert By Web site Alert Text :")
                print(e.msg)
                print("==============================")
            student.setDegrees(Degrees)
            time.sleep(3)

    @staticmethod
    def close():
        WebIO.bwr.quit()
