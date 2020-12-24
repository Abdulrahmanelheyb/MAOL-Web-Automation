import xlsxwriter
import xlrd
import os
from models.Student import *
from os import path


class ExcelRW:

    @staticmethod
    def read_excel(ExcelWorkBookReadPath, SheetNdx: int) -> list:

        # region > Setup
        Students = []
        workBook = xlrd.open_workbook(ExcelWorkBookReadPath)
        workSheet = workBook.sheet_by_index(SheetNdx)
        ndx = 0
        # endregion

        # region > Get Read Students
        for i in range(workSheet.nrows):
            std = Student()
            std.setID(ndx)
            std.setStudentNo(int(workSheet.cell_value(i, 0)))
            std.setTcNo(int(workSheet.cell_value(i, 1)))
            std.setFirstName(workSheet.cell_value(i, 2))
            std.setLastName(workSheet.cell_value(i, 3))
            std.setBranch(workSheet.cell_value(i, 8))
            Students.append(std)
            ndx += 1
        return Students
        # endregion

    @staticmethod
    def write_excel(ExcelWorkBookWritePath: str, Data: list):

        # region > Setup

        workbook = xlsxwriter.Workbook(ExcelWorkBookWritePath)
        # endregion
        if type(Data) == list:
            for infopack in Data:

                crow = 1  # Set Default Current Row
                ccol = 5  # Set Default Current Column

                # region > Create Sheet
                sheet = workbook.add_worksheet(infopack["SheetName"])
                # endregion

                # region > Cell Format
                frmtRotate = workbook.add_format()
                frmtRotate.set_rotation(90)

                frmt_Bold_Center = workbook.add_format()
                frmt_Bold_Center.set_bold(True)
                frmt_Bold_Center.set_align('center')

                frmtAlign_Rotate_Bold = workbook.add_format()
                frmtAlign_Rotate_Bold.set_rotation(90)
                frmtAlign_Rotate_Bold.set_bold(True)
                frmtAlign_Rotate_Bold.set_align('vcenter')

                frmtNotDegreesColored = workbook.add_format()
                frmtNotDegreesColored.set_font_color('red')
                # endregion

                # region > Header
                sheet.write(0, 0, "ÖĞRENCİ NO")
                sheet.write(0, 1, "T.C. KİMLİK NO")
                sheet.write(0, 2, "ADI")
                sheet.write(0, 3, "SOYADI")
                sheet.write(0, 4, "ALAN")
                sheet.write(0, 5, "KAYIT TARİHİ")

                # region > Write Lessons
                for lesson in infopack["Lessons"]:
                    ccol += 1
                    sheet.write(0, ccol, lesson["Name"], frmtRotate)
                    sheet.write(1, ccol, lesson["Credit"], frmt_Bold_Center)

                ccol += 1
                sheet.set_column(ccol, ccol, 5)
                sheet.write(0, ccol, "Toplam", frmtAlign_Rotate_Bold)
                sheet.write(1, ccol, infopack["TotalLCredits"], frmt_Bold_Center)
                # endregion

                # endregion

                # region > Loop on Students
                for student in infopack["Students"]:
                    crow += 1
                    sheet.write(crow, 0, student.getStudentNo())
                    sheet.write(crow, 1, student.getTcNo())
                    sheet.write(crow, 2, student.getFirstName())
                    sheet.write(crow, 3, student.getLastName())
                    sheet.write(crow, 4, student.getBranch())
                    sheet.write(crow, 5, student.getRegisterDate())
                    calculateDegrees(student, infopack["Lessons"])
                    degrees = student.getDegrees()

                    for degree in degrees:
                        lessonName = degree["LessonName"]
                        colndx = 5
                        for lesson in infopack["Lessons"]:
                            colndx += 1
                            if lessonName == lesson["Name"]:
                                sheet.write(crow, colndx, degree["Score"])
                                break

                    sheet.write(crow, ccol, student.getSumCredits(), frmt_Bold_Center)
                # endregion

                # region > Last Properties
                sheet.set_zoom(75)
                sheet.set_column(0, 1, 14)
                sheet.set_column(6, ccol, 3)
                sheet.set_column(2, 2, 20)
                sheet.set_column(3, 4, 30)
                sheet.set_column(5, 5, 14)
                # endregion

        # region > Check To Write
        if path.exists(ExcelWorkBookWritePath):
            os.remove(ExcelWorkBookWritePath)
            workbook.close()
        else:
            workbook.close()
        # endregion
