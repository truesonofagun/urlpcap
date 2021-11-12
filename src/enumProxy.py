#!/usr/bin/env python3

# import scapy
# TODO: construct the URL and then enumerate the URL here then parsing file

"""
Found the correct way to send a URL request in stackover flow
a=Ether()/IP(dst="www.example.com")/TCP()/"GET /index.html HTTP/1.0 \n\n"
scapy is able to save this into a pcap file for latter
The URL will need to be deconstructed and reconstructed
Check https://scapy.readthedocs.io/en/latest/ for more on how
"""
