class Person:
    def __init__(self, name,  salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.salary > other.salary

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age

    def __str__(self):
        return f"{self.name}: Age: {self.age} Salary: {self.salary}"


if __name__ == '__main__':
    persons = [Person("Avi",50000, 28), Person("Sapir",50000, 27), Person("Adir",48000, 31), Person("Tal",32000, 28), Person("Kobi",40000, 45)]
    print("before sorted")
    for person in persons:
        print(person)

    print("after sorted")

    for person in sorted(persons):
        print(person)
