from Student import Student, GetStudentDegrees, insertStudents

# region Globals
workBookReadPath = "C:\\Users\\abdul\\Desktop\\2020-2021-yeni-kayıt-listesi-yeni2.xlsx"
workBookWritePath = "C:\\Users\\abdul\\Desktop\\Students-IT-Data.xlsx"
# endregion

Student.loadStudents(workBookReadPath)
bwr = Student.BeginBrowser()
for std in range(len(Student.Students)):
    GetStudentDegrees(bwr, Student.Students[std])

insertStudents(workBookWritePath)
Student.EndBrowser(bwr)