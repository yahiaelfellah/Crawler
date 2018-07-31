import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import shutil

PROJECT_NAME = 'YahiaProject'
HOMEPAGE = 'https://www.indeed.fr/jobs?q=jave+&l=france'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work())
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()
        if queue.empty():
            print("end of process......")
            break


# Each link in the queue is a job
def create_job():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("------ We have to list --------- = " + len(queued_links))
        create_job()


def clear_project(PROJECT_NAME):
    shutil.rmtree(PROJECT_NAME)


if __name__ == '__main__':
    # TODO : until to find how i can detet the first run of the main
    # clear_project(PROJECT_NAME)
    create_workers()
    crawl()
