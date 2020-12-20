from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
import time

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

bwr: webdriver.Edge = None
webIsBegined = False


def w_begin():
    global bwr
    global webIsBegined
    bwr = webdriver.Edge("C:\\WebDrivers\\msedgedriver.exe")
    bwr.get(
        "https://mebbisssoyd.meb.gov.tr/ssologinBIDB.aspx?id=3&url=http://aolweb.aol.meb.gov.tr/kurum_giris.aspx")
    username = bwr.find_element(By.ID, "txtKullaniciAd")
    username.send_keys("13889656220")
    password = bwr.find_element(By.ID, "txtSifre")
    password.send_keys("Damlanur1")
    time.sleep(10)
    webIsBegined = True


def read_web(students: list):
    global bwr
    global webIsBegined

    for student in students:
        Degrees = []
        try:
            # this condition for no refresh page in first student scraping
            if student.getID() != 0:
                bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")
            else:
                if bool(webIsBegined):
                    bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")

            tcno = bwr.find_element(By.ID, "txtOgrenciNo")
            tcno.clear()
            tcno.send_keys(student.getStudentNo())
            # time.sleep(1)

            listStdData = bwr.find_element(By.ID, "IMG1")
            listStdData.click()
            # time.sleep(1)

            selectStd = bwr.find_element(By.XPATH, "//*[@id='grdAramaSonuclar']/tbody/tr[2]/td[1]/a/img")
            selectStd.click()
            # time.sleep(1)

            goto_register_date_menu = bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[9]/a")
            goto_register_date_menu.click()
            # time.sleep(1)

            register_date = bwr.find_element(By.XPATH, "//*[@id='lblKayitTarihi']")
            student.setRegisterDate(register_date.text)

            degreesMenu = bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[3]/a")
            degreesMenu.click()

            time.sleep(2)

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
        student.calculateDegrees()


def w_end():
    global bwr
    bwr.quit()
