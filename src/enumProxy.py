#!/usr/bin/env python3

from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys
log.startLogging(sys.stdout)

class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy

reactor.listenTCP(1024, ProxyFactory())
reactor.run()

