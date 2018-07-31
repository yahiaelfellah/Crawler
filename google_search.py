from general import *
try:
    from googlesearch import search
except ImportError as e:
    print("we have a problem " + str(e))
import os

PROJECT_NAME = "YahiaProject"
search_file = PROJECT_NAME + "/search.txt"


def create_search_file():
    if not os.path.isfile(search_file):
        write_file(search_file, '#this is first line in the file')


def my_search():
    query = "youtube"  # TODO : we have to modify the query from the gui interface
    search_set = set()
    for link in search(query, lang='en', num=10, stop=1, pause=2):
        search_set.add(link)
        print(link)
    # after that we save into our file
    set_to_file(search_set, search_file)


if __name__ == "__main__":
    create_search_file()
    my_search()
