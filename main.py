from models.Web_IO import *
from models.Excel_RW import *
import os

# region Globals
excelFilePath = "C:\\Users\\abdul\\Desktop\\2020-2021-yeni-kayıt-listesi-yeni2.xlsx"
workBookWritePath = "C:\\Users\\abdul\\Desktop\\Students-Data.xlsx"
DriverPath = "C:\\WebDrivers\\msedgedriver.exe"
# endregion


try:
    os.system('taskkill /f /im msedgedriver.exe')
except Exception as ex:
    print(ex)


# region > Departments Lessons
BLessons = [
    dict(Credit=2, Name="AÇIK KAYNAK İŞLETİM SİSTEMLERİ 1"),
    dict(Credit=2, Name="BİLGİSAYARLI TASARIM UYGULAMALARI 1"),
    dict(Credit=2, Name="BİLGİSAYARLI TASARIM UYGULAMALARI 2"),
    dict(Credit=2, Name="BİLİŞİM TEKNİK RESMİ 1"),
    dict(Credit=3, Name="BİLİŞİM TEKNOLOJİLERİNİN TEMELLER 1"),
    dict(Credit=3, Name="BİLİŞİM TEKNOLOJİLERİNİN TEMELLERİ 2"),
    dict(Credit=8, Name="GRAFİK VE ANİMASYON 1"),
    dict(Credit=7, Name="İNTERNET PROGRAMCILIĞI 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 2"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM ATÖLYESİ 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM ATÖLYESİ 2"),
    dict(Credit=2, Name="OFİS PROGRAMLARI 1"),
    dict(Credit=4, Name="PROGRAMLAMA TEMELLERİ 1"),
    dict(Credit=4, Name="PROGRAMLAMA TEMELLERİ 2"),
    dict(Credit=4, Name="WEB TASARIMI VE PROGRAMLAMA 1 (*)"),
]
ELessons = [
    dict(Credit=2, Name="BİLGİSAYAR DESTEKLİ UYGULAMALAR 1"),
    dict(Credit=3, Name="DİJİTAL ELEKTRONİK 1"),
    dict(Credit=2, Name="ELEKTRİK-ELEKTRONİK TEKNİK RESMİ 1"),
    dict(Credit=2, Name="ELEKTRİK-ELEKTRONİK TEKNİK RESMİ 2"),
    dict(Credit=9, Name="ELEKTRİK-ELEKTRONİK VE ÖLÇME 1 (*)"),
    dict(Credit=9, Name="ELEKTRİK-ELEKTRONİK VE ÖLÇME 2 (*)"),
    dict(Credit=3, Name="ELEKTRİK ELEKTRONİK ESASLARI 1"),
    dict(Credit=3, Name="ELEKTRİK ELEKTRONİK ESASLARI 2"),
    dict(Credit=6, Name="ELEKTRİK MAKİNELERİ VE KONTROL SİSTEMLERİ 1 (*)"),
    dict(Credit=0, Name="ENDÜSTRİYEL ELEKTRİK SİSTEMLERİ 1"),
    dict(Credit=4, Name="ENDÜSTRİYEL KONTROL SİSTEMLERİ 1"),
    dict(Credit=5, Name="ENDÜSTRİYEL KONTROL VE ARIZA ANALİZ 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 2"),
    dict(Credit=2, Name="MİKROKONTROL DEVRELERİ 1"),
    dict(Credit=9, Name="TEMEL ELEKTRİK-ELEKTRONİK ATÖLYESİ 1 (*)")]
MLessons = [
    dict(Credit=4, Name="BİLGİSAYAR DESTEKLİ TASARIM VE ÜRETİM 1 (CAD/CAM)"),
    dict(Credit=4, Name="BİLGİSAYAR DESTEKLİ TASARIM VE ÜRETİM 2 (CAD/CAM)"),
    dict(Credit=8, Name="BİLGİSAYAR KONTROLLÜ TEZGAHLARLA ÜRETİM 1 (CNC) (*)"),
    dict(Credit=2, Name="HİDROLİK PNÖMATİK 1"),
    dict(Credit=8, Name="İMALAT İŞLEMLERİ 1"),
    dict(Credit=24, Name="İŞLETMELERDE MESLEKİ EĞİTİM 1 (*)"),
    dict(Credit=24, Name="İŞLETMELERDE MESLEKİ EĞİTİM 2 (*)"),
    dict(Credit=8, Name="KATI MODELLEME VE ANİMASYON 1"),
    dict(Credit=8, Name="KATI MODELLEME VE ANİMASYON 2"),
    dict(Credit=8, Name="MAKİNE ELEMANLARI VE MEKANİZMALAR 1 (*)"),
    dict(Credit=8, Name="MAKİNE ELEMANLARI VE MEKANİZMALAR 2 (*)"),
    dict(Credit=4, Name="MAKİNE MESLEK RESMİ 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 1"),
    dict(Credit=2, Name="MESLEKİ GELİŞİM 2"),
    dict(Credit=3, Name="TASARI GEOMETRİ 1"),
    dict(Credit=3, Name="TASARI GEOMETRİ 2"),
    dict(Credit=8, Name="TEMEL İMALAT İŞLEMLERİ 1 (*)"),
    dict(Credit=8, Name="TEMEL İMALAT İŞLEMLERİ 2 (*)"),
    dict(Credit=4, Name="TEKNİK RESİM 1"),
    dict(Credit=2, Name="BİLGİSAYAR DESTEKLİ ÇİZİM 1")]
# endregion

# region > Read Students Form Excel
BilisimStudents = ExcelRW.read_excel(excelFilePath, 0)
ElektronikStudents = ExcelRW.read_excel(excelFilePath, 1)
MakinaStudents = ExcelRW.read_excel(excelFilePath, 2)
# endregion

# region > Read Students Degrees Form Web
WebIO.Start(DriverPath)

WebIO.read_web(BilisimStudents)
WebIO.read_web(ElektronikStudents)
# endregion

# region > Preparing Data
Data = [
    dict(Students=BilisimStudents, Lessons=BLessons, SheetName="Bilisim", TotalLCredits=51),
    dict(Students=ElektronikStudents, Lessons=ELessons, SheetName="Elektronik", TotalLCredits=63),
    dict(Students=MakinaStudents, Lessons=MLessons, SheetName="Makina", TotalLCredits=142)
]
# endregion

# region > Write To Excel
ExcelRW.write_excel(workBookWritePath, Data)
# endregion

# region > End Process
WebIO.close()
# endregion
