from read.read.PingDataRead import read_ping_data
from domain.model.Ping import Ping
# TODO return single or list of Ping domain, methods or 

"""
cases:
    1. We can have multiple files of ping
    2. Each can contain multiple Ping results
    3. Find a way to display each Run
    4. Each run must be seen as ping instance from main

"""
def findAllPingResults ():
    
    # Each run is a file with multiple ping results
    files_ping_data = read_ping_data()
    
    print(type(files_ping_data))

    for file_data in files_ping_data:
        print(type(file_data))
        file_data = file_data.strip().splitlines()
        for line in file_data:
            print(line)

    return False