import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory..." + directory)
        os.makedirs(directory)


# Create queue and crawled files if not created
def create_data_files(project_name, base_url):
    # a list of waiting url to be crawled
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Adding file into existing file
def add_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


7  # delete the containt of a file


def delete_file_content(path):
    with open(path, 'w'):
        pass


# Read a file and convert into set of items
def file_to_set(file_name):
    results = set();
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Convert to file
def set_to_file(links, file):
    delete_file_content(file)
    for link in links:
        add_to_file(file, link )
