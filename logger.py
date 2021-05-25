import csv
import datetime

def logger(filepath):
    def _logger(function):
        def new_function(*args, **kwargs):
            func_time = datetime.datetime.now()
            foo_name = function.__name__
            result = function(*args, **kwargs)
            with open(filepath, 'a', newline='') as f:
                writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([func_time, foo_name, args, kwargs, result])
            return result
        return new_function
    return _logger
