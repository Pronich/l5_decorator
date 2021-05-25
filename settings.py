import os

def filepath():
    file_path = os.getcwd()
    return os.path.join(file_path, 'loggers.csv')