# file_handler.py

def read_reviews(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def write_results(file_path, results):
    with open(file_path, "w") as file:
        for line in results:
            file.write(line + "\n")
