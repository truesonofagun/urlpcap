# urlpcap
This will be a simple application to collect pcap (and other) information from a URL

### Objectives
- Create a proxy server that can pass traffic and then capture the traffic
- Create URL input validation for all http and https option
- Create a parsing file to pass the raw traffic to a pcap file

##### Optional
- DNS option passed through the command line

### Install
1. The Build package will need to be installed
`pip3 install build`

2. From within the urlpcap direction
`python3 -m build`

3. In the same directory
`pip3 install dist/*.whl`
