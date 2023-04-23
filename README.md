
# Lab_02_Nathalie_Tobi

## 1 Python Learning with Unit Tests

## 2 Small Python Exercises

### 2.1 Lists

#### Create a list of numbers between 1 and 20

To create a list of numbers between 1 and 20, we call
the `range` constructor with the arguments `start=1`,`stop=21`.
We use the returned `range` Object as a parameter in the `list` 
constructor.  
```python
list1 = list(range(1, 21))
```

#### Create a list containing the squares of list1, using List Comprehension

The power operator in python is `**`. To calculate the squares for each item in our `list`,
we use a List Comprehension with `x ** 2` as an expression. Next and last in line is a `for`
clause. It is part of every List Comprehension, and we use it to iterate all `list1` items.
We assign the new `list` Object to `list2`.
```python
list2 = [x ** 2 for x in list1]
```

#### Create a list with only the even values in list1, using List Comprehension

In this List Comprehension, we use `y` as statement, as there is no need to
change the `list1` items. We use the same `for` clause as before and follow up
with an `if-statement`. It uses the modulo operator to determine if `y` is evenly
divisible by two. If this returns `True`, `list[y]` is included in the returned `list`.
```python
list3 = [y for y in list1 if y % 2 == 0]
```

[Ranges](https://docs.python.org/3/library/stdtypes.html#ranges)  
[List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

### 2.2 Sorting

#### Create your own datatype

Our datatype is called `Person` and it's constructor takes parameters `Name`,`Age`.
To define our own `class`, we simply declare `class Person`.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
We define `__init__` to allow the construction of `Person` Objects with our own parameters. Every
new instance of `Person` that is created will call it during construction.


#### Make it sortable

We want to sort Persons by age, low to high. To make a datatype sortable with the `<` operator,
it needs to implement `__lt__`. `Fred < Frederike` calls `Fred.__lt__(Frederike)`. If Fred is 
younger than Frederike, this should return `True`. To archive this, `__lt__` returns `Fred.age < Frederike.age`.
```python
class Person:
    # details omitted
    def __lt__(self, other):  # we sorted our persons depending on the age the person has
        return self.age < other.age
```


[Object.lt](https://docs.python.org/3/reference/datamodel.html?highlight=__lt__#object.__lt__)  
[Class Objects](https://docs.python.org/3/tutorial/classes.html#class-objects)
## 3 Lambdas and List Comprehensions Applied

#### Find all relevant files on your disk/in a certain directory. Pass the directory in as a parameter. Use glob to generate the list of files.

#### Define “Identical Photos / Duplicate Files” for you - how to you check if two files contain the same photo? (hint: an usual approach is to compare file name, creation date and/or md5 hash)

#### Sketch the algorithm to detect and document duplicate files in pseudo code

#### Create a data structure that supports detection and documentation of the duplicate files. (This will usually be a class or namedtuple to represent the files and some collection)

#### Implement the script completely.

#### How do you test your script?

#### for the bored: how would you go about actually deleting the duplicate files? (be careful with that part, obviously.)