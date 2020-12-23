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
            std.setTcNo(workSheet.cell_value(i, 1))
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
        crow = 2
        workbook = xlsxwriter.Workbook(ExcelWorkBookWritePath)
        # endregion
        if type(Data) == list:
            for infopack in Data:

                # region > Create Sheet
                sheet = workbook.add_worksheet(infopack["SheetName"])
                sheet.set_zoom(75)
                sheet.set_column(0, 1, 14)
                sheet.set_column(6, 21, 3)
                sheet.set_column(2, 2, 15)
                sheet.set_column(4, 4, 30)
                sheet.set_column(5, 5, 14)
                sheet.set_column(22, 22, 3.8)
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

                # endregion

                # region > Header

                sheet.write(0, 0, "YENİ KAYIT ÖĞRENCİ LİSTESİ")
                sheet.write(1, 0, "ÖĞRENCİ NO")
                sheet.write(1, 1, "T.C. KİMLİK NO")
                sheet.write(1, 2, "ADI")
                sheet.write(1, 3, "SOYADI")
                sheet.write(1, 4, "ALAN")
                sheet.write(1, 5, "KAYIT TARİHİ")

                rowndx = 5
                for lesson in infopack["Lessons"]:
                    rowndx += 1
                    sheet.write(1, rowndx, lesson["Name"], frmtRotate)
                    sheet.write(2, rowndx, lesson["Credit"], frmt_Bold_Center)

                sheet.write(1, rowndx + 1, "Toplam", frmtAlign_Rotate_Bold)
                sheet.write(2, rowndx + 1, infopack["TotalLCredits"], frmt_Bold_Center)

                # endregion

                # region > Loop on Students
                for student in infopack["Students"]:

                    crow += 1
                    sheet.write(crow, 0, student.getStudentNo())
                    sheet.write(crow, 1, student.getTcNo())
                    sheet.write(crow, 2, student.getFirstName())
                    sheet.write(crow, 3, student.getLastName())
                    sheet.write(crow, 4, infopack["SheetName"])
                    sheet.write(crow, 5, student.getRegisterDate())
                    calculateDegrees(student, infopack["Lessons"])
                    degrees = student.getDegrees()

                    for i in range(len(degrees)):
                        lessonName = degrees[i]["LessonName"]
                        rowndx = 5
                        for lesson in infopack["Lessons"]:
                            rowndx += 1
                            if lessonName == lesson["Name"]:
                                sheet.write(crow, rowndx, degrees[i]["Score"])
                    sheet.write(crow, 22, student.getSumCredits(), frmt_Bold_Center)
                # endregion

        # region > Check To Write
        if path.exists(ExcelWorkBookWritePath):
            os.remove(ExcelWorkBookWritePath)
            workbook.close()
        else:
            workbook.close()
        # endregion
