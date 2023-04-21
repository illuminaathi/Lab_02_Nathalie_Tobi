import glob
# https://developer.mozilla.org/

globs = glob.iglob("./Downloads/**",
                   recursive=True)


def print_globs():
    for globi in globs:
        print(globi)


# https://docs.python.org/3/library/functions.html#open
def print_file(path):
    print()


if __name__ == '__main__':
    print_globs()

