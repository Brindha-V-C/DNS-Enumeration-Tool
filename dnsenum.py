import dns.resolver
import sys

try:
    domain = sys.argv[1]
except IndexError:
    print("Syntax Error - python dnsenum.py <domainname>")
    quit()

options = ['A','AAAA','NS','CNAME','MX','PTR','SOA','TXT']

for records in options:
    try:
        ans = dns.resolver.resolve(domain,records)
        print(f'\n{records} Records')
        print("-"*30)
        for s in ans:
            print(s.to_text())

    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist')
        quit()

    except dns.resolver.NoAnswer:
        pass