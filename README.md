# Lab_02_Nathalie_Tobi

### Part 2: Small Python Exercises

This should be done together.
- List Comprehension: create a list of numbers between 1 and 20 (list1), then, using List Comprehension:
        create a list containing the squares of list1
        create a list with only the even values in list1
- Sorting:
        create your own datatype (class) - you may want to read ahead and do something that relates to your example for part 3.
        make it sortable, put it in a list and sort the list.

Part 3: Lambdas and List Comprehensions Applied

This should be done together. Create a Python script that does something useful with some files on your computer, e.g. find all duplicate Photos (mp3s, etc):

- Find all relevant files on your disk/in a certain directory. Pass the directory in as a parameter. Use glob to generate the list of files.
- Define “Identical Photos / Duplicate Files” for you - how to you check if two files contain the same photo? (hint: an usual approach is to compare file name, creation date and/or md5 hash)
- Sketch the algorithm to detect and document duplicate files in pseudo code 
- Create a data structure that supports detection and documentation of the duplicate files. (This will usually be a class or namedtuple to represent the files and some collection) 
- Implement the script completely. 
- How do you test your script? 
- for the bored: how would you go about actually deleting the duplicate files? (be careful with that part, obviously.)

Feel free to do something else with files as long as your example contains glob and a non-trivial internal data structure.