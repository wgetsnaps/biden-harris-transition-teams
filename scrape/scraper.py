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

SRC_PATH = Path("docs/index.html")
OUT_HEADER = (
    "agency",
    "last_name",
    "first_name",
    "middle_name",
    "recent_employment",
    "funding_source",
    "is_team_lead",
    "full_name",
    "row_index",
)
TEAM_LEAD_TXT = (
    ", Team Lead"  # this is boilerplate in the name of the first person in each table
)


def parse_page(html: str) -> ListType[DictType]:
    """convert html text to a list of team member data"""
    data = []
    doc = hparse(html)

    for hed in doc.cssselect("h2"):
        agency = hed.text_content()
        for i, row in enumerate(hed.getnext().cssselect("tbody tr"), 1):
            cells = [r.text_content().strip() for r in row.cssselect("td")]

            d = {
                "agency": agency,
                "full_name": cells[0].replace(TEAM_LEAD_TXT, ""),
                "recent_employment": cells[1],
                "funding_source": cells[2],
                "is_team_lead": True if i == 1 else False,
                "row_index": i,
            }

            # A very sloppy, lazily assuming name parsing script, but good enough for now...
            d["first_name"], d["middle_name"], *lname = d["full_name"].split(" ", 2)
            d["last_name"] = lname[0] if lname else d.pop("middle_name")
            data.append(d)

    return data


def main():
    data = parse_page(SRC_PATH.read_text())
    stderr.write("Parsed %s data rows from: %s\n" % (len(data), SRC_PATH))

    outs = csv.DictWriter(stdout, fieldnames=OUT_HEADER)
    outs.writeheader()
    outs.writerows(data)


if __name__ == "__main__":
    main()
