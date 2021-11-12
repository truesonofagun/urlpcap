#!/bin/usr/env python3

from urllib.parse import urlparse


def url_parse(u):
    d = urlparse(u)
    return d
