class Student:

    def __init__(self):

        # region > Initialize Attribute
        self.ID: int = None
        self.firstName: str = None
        self.lastName: str = None
        self.studentNo: str = None
        self.tcNO: str = None
        self.register_date: str = None
        self.branch: str = None
        self.degrees: list = []
        # endregion

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

    def getSumCredits(self) -> int:
        total: int = 0
        if self.degrees is not None:
            for degree in self.degrees:
                total += int(degree["Score"])
        return total

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
    """
    The Method calculate student degrees.

    :param student: Student Instance
    :param Lessons: Lessons List
    :return: No return set directly on student instance
    """
    # Check Student degrees var in not None.
    if student.degrees is not None:

        # region > Loop on Dictionaries in Degrees
        for degree in student.degrees:

            # Check degrees is greater than or equal to 45.00
            if float(degree["Score"]) >= 45.00:
                for lesson in Lessons:
                    if degree["LessonName"] == lesson["Name"]:
                        degree["Score"] = lesson["Credit"]
                        break

            # if else condition Set 0
            else:
                for lesson in Lessons:
                    if degree["LessonName"] == lesson["Name"]:
                        degree["Score"] = 0
                        break
        # endregion
