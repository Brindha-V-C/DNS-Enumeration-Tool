# DNS Enumeration Tool

This is a simple DNS enumeration tool written in Python. It uses the **dnspython** library to query various DNS records for a given domain.

## Requirements

- Python 3.13
- "dnspython" library

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:
         pip install dnspython sys

## Usage

Run the script with the domain name as an argument
   **python dnsenum.py <domainname>**

The tool queries the following DNS records:
      A,AAAA,NS,CNAME,MX,PTR,SOA,TXT
