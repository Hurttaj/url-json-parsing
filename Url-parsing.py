import argparse
from urllib.parse import urlparse
import urllib.request
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Enter an URL.')
parser.add_argument(dest='url', default=None)
args = parser.parse_args()
print(args.url)
o = urlparse(args.url)
print(o)
netloc = o.netloc
print("Hostname: " + netloc)
host = netloc.split('.')
print("TLD: " + host[-1])
SecondLevelDomains = ['co', 'org', 'gov', 'net', 'ltd', 'mod', 'mil', 'ac', 'plc', 'nhs']
#Since second level domains exist, naively grabbing the last and second to last dot-separated element would return the wrong result given a URL with a second-level domain.
# I'm checking the second to last element against a list first. My list is incomplete, but it will at least work for more domains.
if host[-2] in SecondLevelDomains:
    Domain = host[-3] + "." + host[-2] + "." + host[-1]
    print("Domain: " + Domain)
else:
    Domain = host[-2] + "." + host[-1]
    print("Domain: " + Domain)
print("Path: " + o.path)

page = urllib.request.urlopen(args.url)
soup = BeautifulSoup(page, 'html.parser')
Links = []
for link in soup.find_all('a'):
    Links.append(link.get('href'))
SameDomain = [x for x in Links if str(Domain) in str(x)]
SameHost = [x for x in Links if str(netloc) in str(x)]
OnlySameDomain = []
for x in SameDomain:
    if x not in SameHost:
        OnlySameDomain.append(x)

DiffDomain = [x for x in Links if str(Domain) not in str(x) and '.' in str(x) and (str(x).startswith('//www') or str(x).startswith('http'))]
print("Same Host:")
for x in SameHost:
    print(x)
print("Same Domain:")
for x in OnlySameDomain:
    print(x)
print("Different Domain:")
for x in DiffDomain:
    print(x)
