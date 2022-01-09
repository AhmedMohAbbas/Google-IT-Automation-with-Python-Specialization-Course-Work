import sys
import os
import re


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, 'r', encoding='UTF-8') as fh:
        for log in fh:
            error_patterns = ["error"]
            for x in range(len(error.split())):
                error_patterns.append(r"{}".format(error.split()[x].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
    return returned_errors


def file_output(returned_errors):
    with open(os.path.expanduser('~')+'/data/errors_found.log', 'w') as fh:
        for error in returned_errors:
            fh.write(error)


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
