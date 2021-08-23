#!/usr/bin/env python3

import argparse

def parserVar():
    parser = argparse.ArgumentParser(description='Enumerating URL to capture pcap file of traffic')
    parser.add_argument('-f', '--foo', help='templete for this project', action='store_true', default=False)

    parsed = parser.parse_args()
