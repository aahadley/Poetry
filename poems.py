import os
import sys
import json
import random

def update_index(directory):
    ''' Returns two dictionaries mapping titles and authors to filenames '''
    titles = {}
    authors = {}

    for filename in os.listdir(directory):
        f = open("poems/" + filename, "r")

        title = f.readline().strip().lower()
        author = f.readline().strip().lower()

        if author in authors:
            authors[author].append(filename)
        else:
            authors[author] = [filename]

        titles[title] = filename

        f.close()

    with open("index.json", "w") as f:
        json.dump([titles, authors], f)

    return titles, authors


def main(args):
    directory = "poems/"

    numargs = len(args) # number of additional arguments

    if numargs >= 2 and (args[1] == "--update" or args[1] == "-u"):
        titles, authors = update_index(directory)
        return
    else:
        with open("index.json", 'r') as f:
            temp = json.load(f)
            titles = temp[0]
            authors = temp[1]

    if numargs < 2 or args[1] == "--update" or args[1] == "-u":
        with open(directory + random.choice(list(titles.values())), "r") as f:
            print(f.read(), end="")

    elif args[1].lower() in titles and args[1].lower() not in authors:
        with open(directory + titles[args[1].lower()], "r") as f:
            print(f.read(), end="")

    elif args[1].lower() in authors and args[1].lower() not in titles:
        with open(directory + random.choice(authors[args[1].lower()])) as f:
            print(f.read(), end="")        

if __name__ == "__main__":
    main(sys.argv)
