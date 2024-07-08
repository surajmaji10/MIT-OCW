from datetime import date


class Person(object):

    def __init__(self, full_name, gender=None, date_of_birth=None):
        if full_name is None:
            raise ValueError("Full name can't be None")
        if type(full_name) != str:
            raise TypeError("Full name must be `str`")

        self.full_name = full_name.strip().upper()
        self.gender = gender.upper()[0] if gender is not None else None

        name_parts = full_name.split(" ")
        if len(name_parts) < 2:
            raise ValueError("Full name must have at least two parts")
        if len(name_parts) == 2:
            name_parts.insert(1, "")
        self.first_name = name_parts[0]
        self.mid_name = name_parts[1]
        self.last_name = name_parts[2]
        self.date_of_birth = date_of_birth

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        assert gender is not None
        self.gender = gender.upper()[0]

    def get_full_name(self):
        return self.full_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birthday(self):
        if self.date_of_birth is None:
            return None
        return date.isoformat(self.date_of_birth)

    def set_birthday(self, date_of_birth):
        assert type(date_of_birth) == date
        self.date_of_birth = date_of_birth

    def get_age_days(self):
        if self.get_birthday() is None:
            return -1
        today = date.today()
        dob = self.date_of_birth
        return (today - dob).days

    def get_age(self, yy=True, mm=True):
        days = self.get_age_days()
        if days == -1:
            return None
        years = days // 365
        months = (days - years * 365) // 30
        age = ""
        if yy and mm:
            age = str(years) + " years " + str(months) + " months"
        elif yy and not mm:
            age = str(years) + " years"
        elif not yy and mm:
            age = str(days // 30) + " months"
        else:
            return str(days) + " days"
        return age

    def __str__(self):
        return "Person: " + self.full_name

    def __lt__(self, other):
        print("Person lt called")
        return self.get_age_days() < other.get_age_days()

    def __gt__(self, other):
        print("Person gt called")
        return self.get_age_days() > other.get_age_days()

    def __eq__(self, other):
        print("Person eq called")
        return self.get_age_days() == other.get_age_days()


class Student(Person):
    student_count = 0

    def __init__(self, full_name, gender=None, date_of_birth=None, college=None):
        Person.__init__(self, full_name, gender, date_of_birth)
        self.college = college
        Student.student_count += 1

    def __str__(self):
        return "Student: {} [{}]".format(self.full_name, self.college)

    def get_college(self):
        return self.college

    def set_college(self, college):
        assert type(college) == str
        self.college = college


class IIScStudent(Student):
    student_id = 0

    def __init__(self, full_name, gender=None, date_of_birth=None, branch=None):
        Student.__init__(self, full_name, gender, date_of_birth, "IISc")
        self.branch = branch
        self.semester = None
        self.gpa = None
        IIScStudent.student_id += 1

    def __str__(self):
        return "IISc Student: {} [{}]".format(self.full_name, self.branch)

    def get_branch(self):
        return self.branch

    def set_branch(self, branch):
        assert type(branch) == str
        self.branch = branch

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        assert type(semester) == str
        self.semester = semester

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        assert type(gpa) == float
        self.gpa = gpa

    def __lt__(self, other):
        print("IISc lt called")
        if self.get_gpa() is None or other.get_gpa() is None:
            raise ValueError("GPA not defined")
        return self.get_gpa() < other.get_gpa()

    def __gt__(self, other):
        print("IISc gt called")
        # return self.get_gpa() > other.get_gpa() ##same as below
        return self.gpa > other.gpa

    def __eq__(self, other):
        print("IISc eq called")
        return abs(self.gpa - other.gpa) < 0.01


p1 = Person("Akash Maji", "M", date(1999, 3, 4))
p2 = Person("Anup Maji", "M", date(1975, 6, 15))
p3 = Person("Suraj Maji", "M", date(2006, 10, 1))
print(p1)

s1 = Student("Akash Maji", "M", date(1999, 3, 4))
print(s1)
s1.set_college("TIT")
print(s1)

s2 = Student("Suraj Maji", 'M', date(2000, 3, 4), "MMPS")
print(s2)

print(s1 > s2)
print(s1.get_birthday())

i1 = IIScStudent("Akash Maji", "M", date(1999, 3, 4))
print(i1)
i1.set_branch("CSA")
print(i1)

i2 = IIScStudent("Suraj Maji", 'M', date(1998, 3, 4))
print(i2)
print(i1.get_gpa())
i1.set_gpa(10.0)
i2.set_gpa(9.98)
print(i1 < i2)
print(i1 > i2)

## print(i1 < s2) ## AttributeError
## print(s2 > i1)  ##works with IISc lt commented, calls Person lt AND else not
## print(s2 < i1)  ##works with IISc gt commented, calls Person gt AND else not

i1.set_gpa(10.0)
i2.set_gpa(10.0)
print(i1 == i2) ##anyway works AND calls Person eq with IISc eq commented
print(s1 == s2)
# print(s1 == i1)

print(type(s1), type(i1))
print(isinstance(s1, IIScStudent))
print(isinstance(i1, IIScStudent))
print(isinstance(i1, Student))
print(Student.__gt__(s2, i1))



# me = Person("Akash Maji", "Male", date(1999, 3, 4))
# print(me.get_age_days())
# print(me.get_age(True, True))
# print(me.get_last_name())
# print(me.get_first_name())
# print(me.get_full_name())
# # print(me.mid_name)
# print(me.get_gender())
# print(me)
#
# bro = Person("Suraj Kumar Maji")
# print(bro.get_age())
# bro.set_birthday(date(2006, 8, 1))
# print(bro.get_age(False, True))
# print(bro.get_age(True, False))
# print(bro.get_age(False, False))
# print(bro.get_gender())
# bro.set_gender("MALE")
# print(bro.get_gender())
# print(bro < me)
# print(bro > me)
# print(bro.mid_name)
# print(bro)

## will give thrown Exceptions
# who = Person(None, "M")
# who = Person("Killy", "F")
# who = Person(1920, "T")

