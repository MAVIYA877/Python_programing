class students:
    def __init__(self,name,roll_no,city,college):
        self.name = name
        self.roll_no = roll_no
        self.city = city
        self.college = college

    def show_name_roll_no(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)

    def show_city_college(self):
        print("city:",self.city)
        print("college:",self.college)

s1 = students("mr.yes",1,"new delhi","international university")
s1.show_name_roll_no()
s1.show_city_college()

#short version
class students:
    def __init__(self,name,roll_no,city,college):
        self.name = name
        self.roll_no = roll_no
        self.city = city
        self.college = college

    def show_all(self):
        print(f"name: {self.name}, roll_no: {self.roll_no}, city: {self.city}, college: {self.college}")

s1 = students("mr.yes",1,"new delhi","international university")
s1.show_all()

#Ultra short version 
class students:
    def __init__(self,name,roll_no,city,college):
        print(name,roll_no,city,college)

s1 = students("mr,yes",1,"bengaluru","international university")