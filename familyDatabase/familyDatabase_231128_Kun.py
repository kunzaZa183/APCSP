class Person:
    def __init__(self, name):
        self.name = name
        self.parents = ("None", "None")
        self.children = []

    def set_parents(self, mother, father):
        self.parents = (mother, father)

    def add_child(self, child):
        self.children.append(child)


def read_family_tree(file_name):
    people = {"None":"None"}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            name = line[0].strip()
            mother = line[1].strip()
            father = line[2].strip()

            if name not in people:
                people[name] = Person(name)
            
            if mother != "None":
                if mother not in people:
                    people[mother] = Person(mother)
                people[name].set_parents(people[mother], people[father])
                people[mother].add_child(people[name])

            if father != "None":
                if father not in people:
                    people[father] = Person(father)
                people[name].set_parents(people[mother], people[father])
                people[father].add_child(people[name])

    return people


def print_family_lines(person):
    print("Maternal line:")
    maternal_line = [person.name]
    mother = person.parents[0]
    while mother != "None":
        maternal_line.append(mother.name)
        mother = mother.parents[0]
    print("\n".join(maternal_line[::-1]))

    print("\nPaternal line:")
    paternal_line = [person.name]
    father = person.parents[1]
    while father != "None":
        paternal_line.append(father.name)
        father = father.parents[1]
    print("\n".join(paternal_line[::-1]))

    print("\nChildren:")
    for child in person.children:
        print(child.name)


file_name = "family.txt"  # Replace this with your family tree file
people = read_family_tree(file_name)

person_name = input("Person's name? ")
if person_name in people:
    person = people[person_name]
    print_family_lines(person)
else:
    print("Person not found in the family tree.")
