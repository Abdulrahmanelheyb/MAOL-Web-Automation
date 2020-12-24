from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import time


# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

class WebIO:

    # region > Class Variables
    bwr: webdriver.Edge = None
    webIsBegined = False
    # endregion

    @staticmethod
    def Start(DriverPath: str):
        # region > Setup
        WebIO.bwr = webdriver.Edge(DriverPath)
        # endregion

        # region > Load / Initialize
        WebIO.bwr.get(
            "https://mebbisssoyd.meb.gov.tr/ssologinBIDB.aspx?id=3&url=http://aolweb.aol.meb.gov.tr/kurum_giris.aspx")
        username = WebIO.bwr.find_element(By.ID, "txtKullaniciAd")
        username.send_keys("13889656220")
        password = WebIO.bwr.find_element(By.ID, "txtSifre")
        password.send_keys("Damlanur1")
        time.sleep(10)
        WebIO.webIsBegined = True
        # endregion

    @staticmethod
    def read_web(students: list):
        """
        The Method Read Student Degrees from web based on students list

        :param students: Students List
        :return: None
        """
        for student in students:
            Degrees = []
            try:
                # region > Check For Go to main page
                if student.getID() != 0:  # this condition for no refresh page in first student scraping
                    WebIO.bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")
                else:
                    if bool(WebIO.webIsBegined):
                        WebIO.bwr.get("http://aolweb.aol.meb.gov.tr/AOL01001.aspx#!")
                # endregion

                # region Input Student No
                tcno = WebIO.bwr.find_element(By.ID, "txtOgrenciNo")
                tcno.clear()
                tcno.send_keys(student.getStudentNo())
                # endregion

                # region > Click button to list students
                listStdData = WebIO.bwr.find_element(By.ID, "IMG1")
                listStdData.click()
                # endregion

                # region > Catch Alert here
                try:
                    # region > Click to get Student Info
                    selectStd = WebIO.bwr.find_element(By.XPATH, "//*[@id='grdAramaSonuclar']/tbody/tr[2]/td[1]/a/img")
                    selectStd.click()
                    # endregion

                    # region > Check Alert
                    alert = Alert(WebIO.bwr)
                    alert.accept()
                    # endregion

                    print("Alert Accepted .")
                except NoAlertPresentException:
                    pass
                # endregion

                # region > Click to goto public
                goto_register_date_menu = WebIO.bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[9]/a")
                goto_register_date_menu.click()
                # endregion

                # region > Get Register Date
                register_date = WebIO.bwr.find_element(By.XPATH, "//*[@id='lblKayitTarihi']")
                student.setRegisterDate(register_date.text)
                # endregion

                # region > Get to degrees page
                degreesMenu = WebIO.bwr.find_element(By.XPATH, "//*[@id='cssmenu']/ul/li[2]/ul/li[3]/a")
                degreesMenu.click()
                # endregion

                time.sleep(2)

                WebIO.bwr.switch_to.frame("webFrame")  # > Switch to frame

                degreesTable = WebIO.bwr.find_element(By.XPATH, "//*[@id='grdYuzYuze']")  # Get Degrees Table
                rowCount = len(WebIO.bwr.find_elements(By.XPATH, "//*[@id='grdYuzYuze']/tbody/tr")) + 1  # Get Rows lens

                # region > Loop on rows to get degrees
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
                            return 0

                    Degrees.append(dict(
                        LessonName=getCell(2),
                        Score=getCell(5)
                    ))
                # endregion

                student.setDegrees(Degrees)  # Set Degrees in student instance

            except NoSuchElementException:
                print("STUDENT DEGREES NOT FOUND !")
                print(f'STUDENT ID {student.getStudentNo()}')
                print(f'STUDENT TCNO : {student.getTcNo()}')
                print(f'STUDENT FULLNAME : {student.getFirstName()} {student.getLastName()}')
                print("==============================")

            time.sleep(1)

    @staticmethod
    def close():
        WebIO.bwr.quit()
