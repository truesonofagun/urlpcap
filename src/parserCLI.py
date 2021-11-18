#!/usr/bin/env python3

import argparse
from enumProxy import url_parse


def parserVar():
    parser = argparse.ArgumentParser(description='Enumerating URL to capture request and reponse and put into a pcap file or print')
    parser.add_argument('url', metavar='www.url.com', help='URL for enumeration')

    parsed = parser.parse_args()
    return parsed


if __name__ == '__main__':
    url = parserVar()
    print(url.url)
    decode = url_parse(url.url)
    print(decode)
