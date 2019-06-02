"""
This is a CLI application that queries google DNS via REST api on https://dns.google.com/
Check https://github.com/elephantatech/GoogleDNSLookup/ for details
@Author: elephantatech
@DateUpdated: 29th May 2019
@prerequisites: python and python requests lib
"""
# importing libs
import argparse
import json
from requests import get
# get arguments
parser = argparse.ArgumentParser(
    prog='GoogleDNSLookup',description='Google dns lookup'
    )
parser.add_argument(
    '-n','--name', 
    help='domain name or zone name for the lookup',required=True
    )
parser.add_argument(
    '-t','--recordtype', 
    help='Type of record you want to find',required=False
    )
args = parser.parse_args()


def gettype(resourcetype):
        """
        get the type of DNS record looking up with a number value.
        """
        
        with open("recordtypes.json", "r") as f:
            json_data=json.load(f)

        dnsrecordtypes = {}
        for k, v in json_data.items():
            dnsrecordtypes[int(k)] = v

        return dnsrecordtypes.get(resourcetype, resourcetype)

def lookup(domainlookup, typenumber):
        """
        google dns zone lookup function to go to the internet 
        to get the infromation
        """
        url='https://dns.google.com/resolve?'
        
        params = {"name":domainlookup, "type":typenumber}
        # make the requests
        r = get(url, params=params)
        #print r.status_code
        print(r.headers['date'])
        parsed_json = json.loads(r.content)

        try:
            answer=parsed_json['Answer']
            updatedanswer = []
            for line in answer:
                line['type'] = gettype(line['type'])
                updatedanswer.append(line)
            return updatedanswer
        except KeyError as err:
            return err

def print_answer(answer):
    """
    print the answer from google DNS lookup in CSV format
    """
    if isinstance(answer, list):
        print("Name, Type, TTL, Resource Data")
        for lines in answer:
            answer_line = ""
            for k, v in lines.items():
                answer_line += f'{v}, '
            print(answer_line[:-2])
    else:
        print(answer)

def main():
    """
    main function where the arguments are processed
    """
    #print args
    if args.recordtype == None:
        result = lookup(args.name,'ANY')
    else:
        result = lookup(args.name,args.recordtype)

    print_answer(result)
    

if __name__ == "__main__":
    main()
