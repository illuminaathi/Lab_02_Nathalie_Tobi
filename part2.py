# REFERENCES:
# https://docs.python.org/3/howto/sorting.html#key-functions
# https://docs.python.org/3/reference/datamodel.html?highlight=__lt__#object.__lt__
# https://docs.python.org/3/library/stdtypes.html#ranges
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# https://docs.python.org/3/library/glob.html?highlight=glob#module-glob

# 2.1 create a list of numbers between 1 and 20:
# 2.2.2 make it sortable

# casts the range between the numbers 1 and 20 to a list
list1 = list(range(1, 21))

# 2.1.1 using list comprehension create a list containing the squares of list1

list2 = [x ** 2 for x in list1]

# 2.1.2 using list comprehension create a list with only the even values in list1

list3 = []
for x in list1:
    if x % 2 == 0:
        list3.append(x)
# this is the list comprehension equivalent:
list3 = [y for y in list1 if y % 2 == 0]


# 2.2.1 create your own datatype (class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 2.2.2 make it sortable
    def __lt__(self, other):  # we sorted our persons depending on the age the person has
        return self.age < other.age


natha = Person('Nathalie', 21)
tobi = Person('Tobias', 29)
#people = [tobi, natha]

a = Person('Anton', 18)
b = Person('Betina', 20)
c = Person('Chad', 30)
d = Person('Dolly', 21)
people = [a, b, c, d]
if __name__ == '__main__':
    print(list1)
    print(list2)
    print(list3)
    print(people[0].name + ", " + people[1].name +', '+ people[2].name)
    people.sort()
    print(people[0].name + ", " + people[1].name +', '+ people[2].name)
