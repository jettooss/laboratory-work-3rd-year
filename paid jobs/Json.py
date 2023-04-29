
import json

class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'group': self.group,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            surname=data['surname'],
            group=data['group']
        )

students = [

    Student("Frank", "Nelson ", "PMI "),
    Student("Gary  ", "Morris ", "PMI "),
    Student("Steven  ", "Ramsey ", "PMI "),
    Student("Sergio  ", "Banks ", "PMI "),
    Student("Alvin  ", "Daniels ", "PMI "),
    Student("Mitchell  ", "Jackson ", "PMI "),
    Student("Steven  ", "Ramsey ", "PMI "),
]


serialized_students = json.dumps([s.to_dict() for s in students])
with open('students.json', 'w') as f:
 f.write(serialized_students)


with open('students.json', 'r') as f:
 deserialized_students = [Student.from_dict(s) for s in json.loads(f.read())]
# Print list of students
for student in deserialized_students:
    print("{}, {}, {}".format(student.name, student.surname, student.group))
