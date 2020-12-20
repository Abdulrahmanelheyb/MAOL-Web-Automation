from models.Student import Student


class BStudent(Student):
    Students = []
    Lessons = [
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

    @staticmethod
    def getTotalLessonsCredits() -> int:
        total = 0
        for Credit in BStudent.Lessons:
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
            std = BStudent()
            std.setID(student["ID"])
            std.setStudentNo(student["studentNo"])
            std.setTcNo(student["tcNO"])
            std.setFirstName(student["firstName"])
            std.setLastName(student["lastName"])
            BStudent.Students.append(std)

    def calculateDegrees(self):
        for degree in self.degrees:
            if degree["Score"] != "-":
                if float(degree["Score"]) > 40.00:
                    for lesson in BStudent.Lessons:
                        if degree["LessonName"] == lesson["Name"]:
                            degree["Score"] = lesson["Credit"]
