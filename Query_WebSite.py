import urllib.request
import urllib.parse
import os
import argparse
import threading
import timeit

# Done : 7/19/2018 3:47PM
# modified : 7:07 PM
# Adding the thread module and functionality to improve the time of results : DONE = 7/19 9:32 PM
parser = argparse.ArgumentParser()
directory_name = 'pages'


class myThread:
    def __init__(self, threadId, name, counter, url, search, location):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
        self.url = url
        self.search = search
        self.location = location

    def run(self):
        print("starting : " + self.name)
        query(self.url, self.search, self.location, self.counter)
        print("exiting :" + self.name)


# parser.add_argument("search",help="Search for a Job/Intern",type=str)
# parser.add_argument("location",help="Location you desire",type=str)
# args = parser.parse_args()
def create_directory():
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name);


def query(url, search, location, counter):
    number = counter / 10
    values = {'q': search, 'l': location, 'start': counter}
    data = urllib.parse.urlencode(values)
    url = 'emplois?'.join([url, data])
    response = urllib.request.urlopen(url)
    if 'text/html' in response.getheader('Content-Type'):
        page = response.read()
        html_string = page.decode("utf-8")
        file_name = "/page_" + str(number) + ".html"
        path_file = directory_name + file_name
        if not os.path.isfile(path_file):
            with open(path_file, "w", encoding='utf-8') as f:
                f.write(html_string)


if __name__ == "__main__":
    create_directory()
    start = timeit.default_timer()
    for i in range(0, 100, 10):
        try:
            thread_name = "thread_" + str(i / 10)
            _thread = myThread(i / 10, thread_name, i, "https://www.indeed.fr/", "java", "france")
            _thread.run()
        except Exception as ex:
            print(ex)
    end = timeit.default_timer()
    print("Time Run = " + str(end - start))
    print("exist ..................")
