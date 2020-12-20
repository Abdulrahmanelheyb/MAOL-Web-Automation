class Student:

    def __init__(self):
        self.ID: int = None
        self.firstName: str = None
        self.lastName: str = None
        self.studentNo: str = None
        self.tcNO: str = None
        self.register_date: str = None
        self.degrees: dict = dict()

    def getID(self):
        return self.ID

    def setID(self, value):
        self.ID = value

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, value):
        self.firstName = value

    def getLastName(self):
        return self.lastName

    def setLastName(self, value):
        self.lastName = value

    def getStudentNo(self):
        return self.studentNo

    def setStudentNo(self, value):
        self.studentNo = value

    def getTcNo(self):
        return self.tcNO

    def setTcNo(self, value):
        self.tcNO = value

    def getRegisterDate(self):
        return self.register_date

    def setRegisterDate(self, value):
        self.register_date = value

    def getDegrees(self):
        return self.degrees

    def setDegrees(self, value):
        self.degrees = value