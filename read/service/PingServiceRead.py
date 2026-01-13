from read.read.PingDataRead import read_ping_data
from domain.model.Ping import Ping
import re

ping_starter_regex = r'^PING\s+.+\s+bytes of data\.$'
ping_byte_regex = r"^(\d+)\s+bytes"
ping_time_regex = r'time=(\d+(?:\.\d+)?)\s*ms'
ping_icmp_regex = r'icmp_seq=(\d+)'
ping_statistic_regex = r'^---(?:\s+([^\s]+))?\s+ping statistics ---$'
ping_timestamp_regex = r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+$'

def findAllPingResults ():
    
    files_ping_data = read_ping_data()
    
    for single_file_ping_data in files_ping_data:            
        single_file_ping_data = single_file_ping_data.strip().splitlines()
        listPingConstructor(single_file_ping_data) 
    return False

def listPingConstructor (single_file_ping_data:str):
    
    ping = None
    reading_process = False
    list_ping = []
    
    for line in single_file_ping_data:
        
        icmp_match = re.search(pattern= ping_icmp_regex , string = line)
        timestamp_match = re.search(pattern= ping_timestamp_regex , string = line)

        if re.match(pattern = ping_starter_regex, string = line):
            ping = Ping()
            reading_process = True
                                    
        if icmp_match and reading_process:
            
            icmp = icmp_match.group(1)
            ping_tuple_record = []
            byte_match = re.search(pattern= ping_byte_regex , string = line)
            time_match = re.search(pattern= ping_time_regex , string = line)
            
            if byte_match:    
                byte = byte_match.group(1)
                ping_tuple_record.append(byte)
            else:
                ping_tuple_record.append("0")
                         
            icmp = icmp_match.group(1)
            ping_tuple_record.append(icmp)
            
            if time_match:                
                time = time_match.group(1)
                ping_tuple_record.append(time)
                
            else:              
                ping_tuple_record.append("0")
                       
            ping.time_history.append(ping_tuple_record)
        
        if timestamp_match and reading_process:
            
            timestamp = timestamp_match.group()
            ping.timestamp = timestamp
            reading_process = False
            list_ping.append(ping)
              
    for ping in list_ping:
        
        print(ping.time_history)
        print("XXXXXXXX Whatever")
       
    return None