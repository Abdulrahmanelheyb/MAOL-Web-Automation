class Student:

    def __init__(self):
        self.ID: int = None
        self.firstName: str = None
        self.lastName: str = None
        self.studentNo: str = None
        self.tcNO: str = None
        self.register_date: str = None
        self.branch: str = None
        self.degrees: dict = dict()

    # region Get Methods

    def getID(self):
        return self.ID

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getStudentNo(self):
        return self.studentNo

    def getTcNo(self):
        return self.tcNO

    def getRegisterDate(self):
        return self.register_date

    def getBranch(self):
        return self.branch

    def getDegrees(self):
        return self.degrees

    def getSumCredits(self):
        total: int = 0
        for degree in self.degrees:
            if degree["Score"] != "-":
                total += int(degree["Score"])

    # endregion

    # region Set Methods

    def setID(self, value):
        self.ID = value

    def setFirstName(self, value):
        self.firstName = value

    def setLastName(self, value):
        self.lastName = value

    def setStudentNo(self, value):
        self.studentNo = value

    def setTcNo(self, value):
        self.tcNO = value

    def setRegisterDate(self, value):
        self.register_date = value

    def setBranch(self, value):
        self.branch = value

    def setDegrees(self, value):
        self.degrees = value

    # endregion


def calculateDegrees(student: Student, Lessons):
    for degree in student.degrees:
        if degree["Score"] != "-":
            if float(degree["Score"]) > 44.99:
                for lesson in Lessons:
                    if degree["LessonName"] == lesson["Name"]:
                        degree["Score"] = lesson["Credit"]