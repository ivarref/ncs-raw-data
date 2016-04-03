#!/usr/local/bin/python

import requests_cache
import requests
import sys
import codecs

def field_production_per_month():
  page = requests.get("http://factpages.npd.no/ReportServer?/FactPages/TableView/field_production_monthly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&rs:Format=CSV&Top100=false&IpAddress=80.212.17.244&CultureCode=en")
  content = page.content.decode('utf-8-sig')
  with codecs.open('data/fpm.csv', mode='wt', encoding='utf-8') as fd:
    for line in content.split('\n'):
      line = line.strip()
      if line == '':
        continue
      fd.write(line)
      fd.write('\n')

if __name__=="__main__":
  requests_cache.install_cache('cache')
  field_production_per_month()

