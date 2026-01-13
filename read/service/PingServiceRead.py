from read.read.PingDataRead import read_ping_data
from domain.model.Ping import Ping
import re

# Takes the line with PING inside -> It recognize the starting of Ping Results
ping_starter_regex = r'^PING\s+.+\s+bytes of data\.$'
ping_byte_regex = r"^(\d+)\s+bytes"
ping_time_regex = r'time=(\d+(?:\.\d+)?)\s*ms'
ping_icmp_regex = r'icmp_seq=(\d+)'
ping_statistic_regex = r'^---(?:\s+([^\s]+))?\s+ping statistics ---$'
ping_timestamp_regex = r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+$'


def findAllPingResults ():
    
    # Each run is a file with multiple ping results
    files_ping_data = read_ping_data()
    
    # Here it reads all the Files which can contain multiple data
    for file_data in files_ping_data:    
        
        # Here takes one File which can contain multiple Ping runs
        file_data = file_data.strip().splitlines()
        
        # File Builder -> it returns a List of Ping
        listPingDataBuilder(file_data)
         
    return False


def listPingDataBuilder (file_data:str):
    
    instance = None
    reading_process = False
    
    for line in file_data:
        
        if re.match(pattern = ping_starter_regex, string = line):
            
            instance = Ping()
            reading_process = True
            continue
              
        icmp_match = re.search(pattern= ping_icmp_regex , string = line)
            
        if icmp_match and reading_process:
            
            # Tuple savings
            icmp = icmp_match.group(1)
            ping_tuple_record = []
            byte_match = re.search(pattern= ping_byte_regex , string = line)
            time_match = re.search(pattern= ping_time_regex , string = line)
            
            if byte_match:    
                byte = byte_match.group(1)
                ping_tuple_record.append(byte)
            else:
                ping_tuple_record.append("0")
                print("not byte found")
            
            icmp = icmp_match.group(1)
            ping_tuple_record.append(icmp)
            
            if time_match:                
                time = time_match.group(1)
                ping_tuple_record.append(time)
                
            else:              
                ping_tuple_record.append("0")
                print("not time found")
                       
            instance.time_history.append(ping_tuple_record)
            
    return None