class Student:
    def __init__(self, name, house):
        self.name = name # to force it to call setter, when .name is called
        self.house = house # to force it to call setter, when .house is called, so error can be check

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod # does not require to create Student object first
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self.__name = name # one underscore can still change, if double underscore, it's super private and can't be change

    # getter
    @property
    def house(self):
        return self.__house

    # setter -> catch if someone wanna access student.house = "something unwanted"
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.__house = house

def main():
    student = Student.get_student()  # calling classmethod
    print(student)  # this will call __str__ when see print(student)

"""Move to classmethod
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # instantiate student object
"""


if __name__ == "__main__":
    main()
