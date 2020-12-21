from models.Student import Student


class EStudent(Student):
    Students = []
    Lessons = [
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

    @staticmethod
    def getTotalLessonsCredits() -> int:
        total = 0
        for Credit in EStudent.Lessons:
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
            std = EStudent()
            std.setID(student["ID"])
            std.setStudentNo(student["studentNo"])
            std.setTcNo(student["tcNO"])
            std.setFirstName(student["firstName"])
            std.setLastName(student["lastName"])
            EStudent.Students.append(std)

    def calculateDegrees(self):
        for degree in self.degrees:
            if degree["Score"] != "-":
                if float(degree["Score"]) > 40.00:
                    for lesson in EStudent.Lessons:
                        if degree["LessonName"] == lesson["Name"]:
                            degree["Score"] = lesson["Credit"]
