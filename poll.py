import urllib2
import time


def make_coffee():
    print("Making Coffee")

while True:
    time.sleep(5)
    value = urllib2.urlopen("http://hack.zahlen.io/index").read()
    if value == "1":
        make_coffee()
