import datetime

class Student:
    def __init__(self, id, name, dob, classification):
        self.__StudentID = id
        self.__DOB = dob
        self.__Name = name
        self.__classification = classification
        print('StudentID: ' + str(self.__StudentID))
        print('DOB: ' + self.__DOB)
        print('Name: ' + self.__Name)
        print('Classification: ' + self.__classification)

    def calcAge(self):
        today = datetime.date.today()
        date_time_obj = datetime.datetime.strptime(self.__DOB, "%m/%d/%y")
        years = today.year - date_time_obj.year
        if today.month < date_time_obj.month or (today.month == date_time_obj.month and today.day < date_time_obj.day):
            years -= 1
        print('student is ' + str(years) + ' years old')

    def whenReg(self):
        month = 4
        days = [[10,12], [7,9], [4,6], [1,3]]
        if self.__classification == 'F':
            n = 0
        if self.__classification == 'S':
            n = 1
        if self.__classification == 'Jr':
            n = 2
        else:
            n = 3
        
        print('you can register from ' + str(month) + '/' + str(days[n][0]) + ' to ' + str(month) + '/' + str(days[n][1]))   

