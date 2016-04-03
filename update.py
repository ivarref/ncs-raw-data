#!/usr/local/bin/python

import requests_cache
import requests
import sys
import codecs

def pull_url_to_file(url, fil):
  page = requests.get(url)
  content = page.content.decode('utf-8-sig')
  with codecs.open(fil, mode='wt', encoding='utf-8') as fd:
    for line in content.split('\n'):
      line = line.strip()
      if line == '':
        continue
      fd.write(line)
      fd.write('\n')
  
def field_production_per_month():
  pull_url_to_file("http://factpages.npd.no/ReportServer?/FactPages/TableView/field_production_monthly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=80.212.17.244&CultureCode=en", 'data/fpm.csv')

def field_reserves():
  pull_url_to_file("http://factpages.npd.no/ReportServer?/FactPages/TableView/field_reserves&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=80.212.17.244&CultureCode=en", 'data/field_reserves.csv')

if __name__=="__main__":
  requests_cache.install_cache('cache')
  field_production_per_month()
  field_reserves()

