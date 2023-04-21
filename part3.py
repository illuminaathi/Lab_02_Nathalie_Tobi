import glob
import hashlib
# https://developer.mozilla.org/

globs = glob.iglob("./Downloads/**",
                   recursive=True)



def print_globs():
    for globi in globs:
        print(globi)


# https://docs.python.org/3/library/functions.html#open
# https://www.youtube.com/watch?v=FxjeV0ePOKU
def get_md5(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        data = file.read()
        hasher.update(data)
    return hasher.hexdigest()


if __name__ == '__main__':
    print_globs()
    print(get_md5('./Downloads/kursliste.txt'))
    print(get_md5('./Downloads/kursliste(1).txt'))
    print(get_md5('./Downloads/kursliste(2).txt'))

