from elektrik_elektronik.estudent import EStudent
from models.excel import *

Lessons = [
    dict(Credit=2, LessonName="BİLGİSAYAR DESTEKLİ UYGULAMALAR 1"),
    dict(Credit=3, LessonName="DİJİTAL ELEKTRONİK 1"),
    dict(Credit=2, LessonName="ELEKTRİK-ELEKTRONİK TEKNİK RESMİ 1"),
    dict(Credit=2, LessonName="ELEKTRİK-ELEKTRONİK TEKNİK RESMİ 2"),
    dict(Credit=9, LessonName="ELEKTRİK-ELEKTRONİK VE ÖLÇME 1 (*)"),
    dict(Credit=9, LessonName="ELEKTRİK-ELEKTRONİK VE ÖLÇME 2 (*)"),
    dict(Credit=3, LessonName="ELEKTRİK ELEKTRONİK ESASLARI 1"),
    dict(Credit=3, LessonName="ELEKTRİK ELEKTRONİK ESASLARI 2"),
    dict(Credit=6, LessonName="ELEKTRİK MAKİNELERİ VE KONTROL SİSTEMLERİ 1 (*)"),
    dict(Credit=0, LessonName="ENDÜSTRİYEL ELEKTRİK SİSTEMLERİ 1"),
    dict(Credit=4, LessonName="ENDÜSTRİYEL KONTROL SİSTEMLERİ 1"),
    dict(Credit=5, LessonName="ENDÜSTRİYEL KONTROL VE ARIZA ANALİZ 1"),
    dict(Credit=2, LessonName="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, LessonName="MESLEKİ GELİŞİM 2"),
    dict(Credit=2, LessonName="MİKROKONTROL DEVRELERİ 1"),
    dict(Credit=9, LessonName="TEMEL ELEKTRİK-ELEKTRONİK ATÖLYESİ 1 (*)")]


def write_header(sheet: xlsxwriter.workbook.Worksheet):
    global Lessons
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

    rowndx = 5
    for l_ndx in Lessons:
        rowndx += 1
        sheet.write(1, rowndx, l_ndx["LessonName"], frmt)

    frmt = getWorkBook().add_format({'bold': True})

    rowndx = 5
    for c_ndx in Lessons:
        rowndx += 1
        sheet.write(2, rowndx, c_ndx["Credit"], frmt)


def write_excel(crow: int, sheetname: str):
    sheet = getWorkBook().add_worksheet(sheetname)

    write_header(sheet)
    sheet.set_zoom(75)

    for student in EStudent.Students:
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
            for l_ndx in Lessons:
                rowndx += 1
                if lessonName == l_ndx["LessonName"]:
                    sheet.write(crow, rowndx, degrees[i]["Score"])