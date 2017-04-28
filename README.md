# GoogleDNSLookup
Python application to lookup Google's Recursive DNS servers ( 8.8.8.8 and 8.8.4.4) via the http://dns.google.com api connection.

## output format
The tool outputs record Answer with the Name, type, TTL and data for example query for A record for google.com will give you the following:

Name: google.com  
Type: A  
TTL: 255  
Data: 172.217.9.78  

the format it will show up as

    google.com, A, 255, 172.217.9.78

for more than one it will list it out each answer from the query with the same format.

    google.com, A, 31, 172.217.0.14
    google.com, A, 255, 172.217.9.78
    
    

## Prerequisites
- Python (v2.7 tested but should work with v3)
- requests library from pip or app store
- Internet access

## Usage

Lookup Host record or A record for google.com

    ./dnslookup.py --name google.com --recordtype A

Lookup ANY record for google.com

    ./dnslookup.py --name google.com --recordtype ANY
    
Short hand options

    ./dnslookup.py -n google.com -t A

## Contributors
Vivek Mistry (elephantatech)

## License
Apache License 2.0 - see [license](LICENSE)

