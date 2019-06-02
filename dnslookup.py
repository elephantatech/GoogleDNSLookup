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
        dnsrecordtypes={
        1:'A',
        2:'NS',
        3:'MD',
        4:'MF',
        5:'CNAME',
        6:'SOA',
        7:'MB',
        8:'MG',
        9:'MR',
        10:'NULL',
        11:'WKS',
        12:'PTR',
        13:'HINFO',
        14:'MINFO',
        15:'MX',
        16:'TXT',
        17:'RP',
        18:'AFSDB',
        19:'X25',
        20:'ISDN',
        21:'RT',
        22:'NSAP',
        23:'NSAP-PTR',
        24:'SIG',
        25:'KEY',
        26:'PX',
        27:'GPOS',
        28:'AAAA',
        29:'LOC',
        30:'NXT',
        31:'EID',
        32:'NIMLOC',
        33:'SRV',
        34:'ATMA',
        35:'NAPTR',
        36:'KX',
        37:'CERT',
        38:'A6',
        39:'DNAME',
        40:'SINK',
        41:'OPT',
        42:'APL',
        43:'DS',
        44:'SSHFP',
        45:'IPSECKEY',
        46:'RRSIG',
        47:'NSEC',
        48:'DNSKEY',
        49:'DHCID',
        50:'NSEC3',
        51:'NSEC3PARAM',
        52:'TLSA',
        53:'SMIMEA',
        54:'Unassigned',
        55:'HIP',
        56:'NINFO',
        57:'RKEY',
        58:'TALINK',
        59:'CDS',
        60:'CDNSKEY',
        61:'OPENPGPKEY',
        62:'CSYNC',
        99:'SPF',
        100:'UINFO',
        101:'UID',
        102:'GID',
        103:'UNSPEC',
        104:'NID',
        105:'L32',
        106:'L64',
        107:'LP',
        108:'EUI48',
        109:'EUI64',
        249:'TKEY',
        250:'TSIG',
        251:'IXFR',
        252:'AXFR',
        253:'MAILB',
        254:'MAILA',
        255:'ANY',
        257:'CAA'
        }
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
