import glob
import hashlib

globs = glob.iglob("./Downloads/*.txt",
                   recursive=True)


#  prints all the file names
def print_globs():
    for globi in globs:
        print(globi)

#  gets the md5 hashes of all files
def get_md5(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        data = file.read()
        hasher.update(data)
    return hasher.hexdigest()


#  creates a list containing all hashes. If a hash appears a second time, it will be printed
def find_doublettes(file_paths):
    hashes = []
    for globi in file_paths:
        md = get_md5(globi)
        if hashes.__contains__(md):
            print(globi + ', ' + md)
        else:
            hashes.append(md)


if __name__ == '__main__':
    find_doublettes(globs)
