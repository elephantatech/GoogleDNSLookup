"""
This is a CLI application that queries google DNS via REST api on https://dns.google.com/
Check https://github.com/elephantatech/GoogleDNSLookup/ for details
@Author: elephantatech
@DateUpdated: 28th April 2017
@prerequisites: python and python requests lib
"""
# importing libs
import argparse
import json
import requests

# get arguments
parser = argparse.ArgumentParser(prog='GoogleDNSLookup',description='Google dns lookup')
parser.add_argument('-n','--name', help='domain name or zone name for the lookup',required=True)
parser.add_argument('-t','--recordtype', help='Type of record you want to find',required=False)
args = parser.parse_args()


def gettype(querytype):
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
        return dnsrecordtypes.get(querytype, querytype)

def lookup(domainlookup, typenumber):
        """
        google dns zone lookup function to go to the internet to get the infromation
        """
        dnslookup='https://dns.google.com/resolve?name='+domainlookup+'&type='+typenumber
        # make the request
        r = requests.get(dnslookup)
        #print r.status_code
        print r.headers['date']
        parsed_json = json.loads(r.content)
        #print parsed_json
        #question=parsed_json['Question']
        #print question[0]

        try:
            answer=parsed_json['Answer']
            print("Name, Type, TTL, Data")
            for items in answer:
                print items['name']+", "+str(gettype(items['type']))+", "+str(items['TTL'])+", "+str(items['data'])
        except KeyError:
            print("Unable to get Answer")

def main():
    """
    main function where the arguments are processed
    """
    #print args
    if args.recordtype == None:
        lookup(args.name,'ANY')
    else:
        lookup(args.name,args.recordtype)
    
if __name__ == "__main__":
    main()
