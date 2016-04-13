#!/usr/bin/python
from time import sleep
# function to write book.json with random data
f = 'book.json'

def main():
  template = '''
{
  "ticker": "ESM5",
  "Buy"   : "%s",
  "Sell"  : "%s"
}
'''
  buy  = 100.9
  sell = 101.1
  while buy < 102.0:
    print template % (str(buy),str(sell))
    buy+=0.1
    sell+=0.1
    sleep(1.0)
main()
