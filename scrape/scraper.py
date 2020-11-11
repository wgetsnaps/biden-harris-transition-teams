#!/usr/bin/env python3
"""
Just a simple scraper that converts the index.html page's tables into CSV
- requires Python 3.5+
- writes to stdout
- run `make scrape` task to scrape and write to scrape/data.csv

To interactively debug an exception:

$ python -m pdb -c continue scrape/scraper.py
"""

import csv
from lxml.html import fromstring as hparse
from pathlib import Path
from sys import stderr, stdout
from typing import Dict as DictType, List as ListType

SRC_PATH = Path('docs/index.html')

OUT_HEADER = ('agency', 'last_name',  'first_name', 'middle_name', 'recent_employment', 'funding_source', 'is_team_lead', 'full_name', 'row_index')
TEAM_LEAD_TXT = ', Team Lead' # this is in the name of the first person in each row

def parse_page(html:str) -> ListType[DictType]:
    data = []

    doc = hparse(html)
    for hed in doc.cssselect('h2'):
        agency = hed.text
        for i, row in enumerate(hed.getnext().cssselect('tbody tr'), 1):
            cells = row.cssselect('td')
            if (i == 1 and TEAM_LEAD_TXT not in cells[0].text) or (i != 1 and ',' in cells[0].text):
                # just making sure "Team Lead" appears only in the first row and nowhere else
                raise ValueError('what the f')

            d = {
                    'agency': agency,
                    'full_name': cells[0].text.replace(TEAM_LEAD_TXT, ''),
                    'recent_employment': cells[1].text,
                    'funding_source': cells[2].text,
                    'is_team_lead': True if i == 1 else False,
                    'row_index': i,
                }

            # sloppy but whatever
            d['first_name'], d['middle_name'], *lname = d['full_name'].split(' ', 2)
            d['last_name'] = lname[0] if lname else d.pop('middle_name')
            data.append(d)

    return data

def main():
    data = parse_page(SRC_PATH.read_text())
    stderr.write('Parsed %s data rows from: %s\n' % (len(data), SRC_PATH))

    outs = csv.DictWriter(stdout, fieldnames=OUT_HEADER)
    outs.writeheader()
    outs.writerows(data)


if __name__ == '__main__':
    main()
