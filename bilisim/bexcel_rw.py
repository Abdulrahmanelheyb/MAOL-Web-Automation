import xlsxwriter
from bilisim.bstudent import BStudent
from models.excel import getWorkBook


def write_header(sheet: xlsxwriter.workbook.Worksheet):

    frmtRotate = getWorkBook().add_format()
    frmtRotate.set_rotation(90)

    frmt_Bold_Center = getWorkBook().add_format()
    frmt_Bold_Center.set_bold(True)
    frmt_Bold_Center.set_align('center')

    frmtAlign_Rotate_Bold = getWorkBook().add_format()
    frmtAlign_Rotate_Bold.set_rotation(90)
    frmtAlign_Rotate_Bold.set_bold(True)
    frmtAlign_Rotate_Bold.set_align('vcenter')

    sheet.write(0, 0, "YENİ KAYIT ÖĞRENCİ LİSTESİ")
    sheet.write(1, 0, "ÖĞRENCİ NO")
    sheet.write(1, 1, "T.C. KİMLİK NO")
    sheet.write(1, 2, "ADI")
    sheet.write(1, 3, "SOYADI")
    sheet.write(1, 4, "ALAN")
    sheet.write(1, 5, "KAYIT TARİHİ")

    sheet.set_column(6, 21, 3)

    rowndx = 5
    for lesson in BStudent.Lessons:
        rowndx += 1
        sheet.write(1, rowndx, lesson["Name"], frmtRotate)
        sheet.write(2, rowndx, lesson["Credit"], frmt_Bold_Center)
    sheet.set_column(22, 22, 3.8)
    sheet.write(1, 22, "Toplam", frmtAlign_Rotate_Bold)
    sheet.write(2, 22, BStudent.getTotalLessonsCredits(), frmt_Bold_Center)


def write_excel(crow: int, sheetname: str):
    sheet = getWorkBook().add_worksheet(sheetname)
    write_header(sheet)
    frmt_Bold_Center = getWorkBook().add_format()
    frmt_Bold_Center.set_align('center')
    frmt_Bold_Center.set_bold(True)
    sheet.set_zoom(75)

    for student in BStudent.Students:
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
            rowndx = 5
            for lesson in BStudent.Lessons:
                rowndx += 1
                if lessonName == lesson["Name"]:
                    sheet.write(crow, rowndx, degrees[i]["Score"])
        sheet.write(crow, 22, student.getTotalStudentCredits(), frmt_Bold_Center)
