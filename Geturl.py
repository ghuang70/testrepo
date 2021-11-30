from lxml.html import parse
from urllib2 import urlopen

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))

doc = parsed.getroot()

links = doc.findall('.//a')
urls =[lnk.get('href') for lnk in doc.findall('.//a')]
print urls[-10:]

tables = doc.findall('.//table')
calls = tables[0]
puts = tables[13]

from pandas.io.parsers import TextParser

def parse_options_data(table):
    rows = table.findall('://tr')
    header = _unpack