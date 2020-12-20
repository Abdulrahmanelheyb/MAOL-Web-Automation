from makina.mstudent import MStudent
from models.excel import *


def write_header(sheet: xlsxwriter.workbook.Worksheet):
    frmt = getWorkBook().add_format()
    frmt.set_rotation(90)
    sheet.write(0, 0, "YENİ KAYIT ÖĞRENCİ LİSTESİ")
    sheet.write(1, 0, "ÖĞRENCİ NO")
    sheet.write(1, 1, "T.C. KİMLİK NO")
    sheet.write(1, 2, "ADI")
    sheet.write(1, 3, "SOYADI")
    sheet.write(1, 4, "ALAN")
    sheet.write(1, 5, "KAYIT TARİHİ")

    sheet.set_column(6, 21, 3)
    sheet.write(1, 6, "", frmt)
    sheet.write(1, 7, "", frmt)
    sheet.write(1, 8, "", frmt)
    sheet.write(1, 9, "", frmt)
    sheet.write(1, 10, "", frmt)
    sheet.write(1, 11, "", frmt)
    sheet.write(1, 12, "", frmt)
    sheet.write(1, 13, "", frmt)
    sheet.write(1, 14, "", frmt)
    sheet.write(1, 15, "", frmt)
    sheet.write(1, 16, "", frmt)
    sheet.write(1, 17, "", frmt)
    sheet.write(1, 18, "", frmt)
    sheet.write(1, 19, "", frmt)
    sheet.write(1, 20, "", frmt)
    sheet.write(1, 21, "", frmt)

    frmt = getWorkBook().add_format({'bold': True})
    sheet.write(2, 6, 2, frmt)
    sheet.write(2, 7, 3, frmt)
    sheet.write(2, 8, 3, frmt)
    sheet.write(2, 9, 2, frmt)
    sheet.write(2, 10, 2, frmt)
    sheet.write(2, 11, 2, frmt)
    sheet.write(2, 12, 8, frmt)
    sheet.write(2, 13, 7, frmt)
    sheet.write(2, 14, 2, frmt)
    sheet.write(2, 15, 2, frmt)
    sheet.write(2, 16, 2, frmt)
    sheet.write(2, 17, 2, frmt)
    sheet.write(2, 18, 2, frmt)
    sheet.write(2, 19, 4, frmt)
    sheet.write(2, 20, 4, frmt)
    sheet.write(2, 21, 4, frmt)


def write_excel(crow: int, sheetname: str):
    sheet = getWorkBook().add_worksheet(sheetname)
    write_header(sheet)
    sheet.set_zoom(75)

    for student in MStudent.Students:
        crow += 1
        sheet.set_column(0, 1, 14)
        sheet.write(crow, 0, student.getStudentNo())
        sheet.write(crow, 1, student.getTcNo())
        sheet.set_column(2, 2, 15)
        sheet.write(crow, 2, student.getFirstName())
        sheet.write(crow, 3, student.getLastName())
        sheet.set_column(4, 4, 30)
        sheet.write(crow, 4, sheetname)
        sheet.set_column(5, 5, 14)
        sheet.write(crow, 5, student.getRegisterDate())

        degrees = student.getDegrees()
        for i in range(len(degrees)):

            lessonName = degrees[i]["LessonName"]

            if lessonName == "":
                sheet.write(crow, 6, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 7, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 8, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 9, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 10, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 11, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 12, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 13, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 14, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 15, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 16, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 17, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 18, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 19, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 20, degrees[i]["Score"])

            elif lessonName == "":
                sheet.write(crow, 21, degrees[i]["Score"])
