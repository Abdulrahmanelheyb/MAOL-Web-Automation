from models.Student import Student


class MStudent(Student):
    Students = []
    Lessons = [
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

    @staticmethod
    def getTotalLessonsCredits() -> int:
        total = 0
        for Credit in MStudent.Lessons:
            total += Credit["Credit"]
        return total

    def getTotalStudentCredits(self) -> int:
        total = 0
        for degree in self.degrees:
            if degree["Score"] != "-":
                total += int(degree["Score"])
        return total

    @staticmethod
    def setStudents(students: list):
        for student in students:
            std = MStudent()
            std.setID(student["ID"])
            std.setStudentNo(student["studentNo"])
            std.setTcNo(student["tcNO"])
            std.setFirstName(student["firstName"])
            std.setLastName(student["lastName"])
            MStudent.Students.append(std)

    def calculateDegrees(self):
        for degree in self.degrees:
            if degree["Score"] != "-":
                if float(degree["Score"]) > 40.00:
                    for lesson in MStudent.Lessons:
                        if degree["LessonName"] == lesson["Name"]:
                            degree["Score"] = lesson["Credit"]
                else:
                    for lesson in MStudent.Lessons:
                        if degree["LessonName"] == lesson["Name"]:
                            degree["Score"] = 0
