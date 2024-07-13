from datetime import date


class Person(object):

    def __init__(self, name):
        self.name = name
        self.dob = None

    def __str__(self):
        return "Person: {}".format(self.name)

    ## lesser is younger
    def __lt__(self, oth):
        print("Person __lt__ called")
        return self.get_age() < oth.get_age()

    def __gt__(self, oth):
        print("Person __gt__ called by {}".format(self.name))
        return self.get_age() > oth.get_age()

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        assert type(dob) == date
        self.dob = dob

    def get_age(self):
        assert self.dob is not None
        today = date.today()
        dob = self.dob
        return (today - dob).days


p1 = Person("Akash Maji")
p2 = Person("Suraj Maji")
print(p1)
print(p2)
p1.set_dob(date(1999, 3, 4))
p2.set_dob(date(2006, 10, 1))
print(p1.get_dob())
print(p2.get_dob())
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)


class MITPerson(Person):
    student_id = 0

    def __init__(self, name, branch = None):
        Person.__init__(self, name)
        self.branch = branch
        self.sid = MITPerson.student_id
        MITPerson.student_id += 1

    def __str__(self):
        return "MIT Person: {}[{}]".format(self.name, self.sid)

    ## lesser is older
    def __lt__(self, other):
        print("MITPerson __lt__ called")
        return self.sid < other.sid

    def get_branch(self):
        return self.branch

    def set_branch(self, branch):
        assert type(branch) == str
        self.branch = branch


m1 = MITPerson("Anup Maji", "CS")
m2 = MITPerson("Mithu Maji")
print(m1)
print(m2)
print(m1.get_branch())
m2.set_branch("EC")
print(m2.get_branch())

m1.set_dob(date(1975, 1, 1))
m2.set_dob(date(1980, 1, 1))
print(m1.get_age())
print(m2.get_age())

print(m1 < m2)
print(m2 > m1)

print("----------------------")

print(p1 < m1) #OK
print(m1 > p1) #OK

print(p1 > m1) #NOT OK
print(m1 < p1) #NOT OK



