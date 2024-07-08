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
        years = days//365
        months = (days - years*365)//30
        age = ""
        if yy and mm:
            age = str(years) + " years " + str(months) + " months"
        elif yy and not mm:
            age = str(years) + " years"
        elif not yy and mm:
            age = str(days//30) + " months"
        else:
            return str(days) + " days"
        return age

    def __str__(self):
        return self.full_name

    def __lt__(self, other):
        return self.get_age_days() < other.get_age_days()

    def __gt__(self, other):
        return self.get_age_days() > other.get_age_days()

    def __eq__(self, other):
        return self.get_age_days() == other.get_age_days()


me = Person("Akash Maji", "Male", date(1999, 3, 4))
print(me.get_age_days())
print(me.get_age(True, True))
print(me.get_last_name())
print(me.get_first_name())
print(me.get_full_name())
# print(me.mid_name)
print(me.get_gender())
print(me)

bro = Person("Suraj Kumar Maji")
print(bro.get_age())
bro.set_birthday(date(2006, 8, 1))
print(bro.get_age(False, True))
print(bro.get_age(True, False))
print(bro.get_age(False, False))
print(bro.get_gender())
bro.set_gender("MALE")
print(bro.get_gender())
print(bro < me)
print(bro > me)
print(bro.mid_name)
print(bro)

## will give thrown Exceptions
# who = Person(None, "M")
# who = Person("Killy", "F")
# who = Person(1920, "T")

