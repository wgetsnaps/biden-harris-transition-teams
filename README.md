# Archive and scrape of Biden-Harris Transition Agency Review Team Members


> **tl;dr note:** if you just care about data scraped from the target page, jump to the **[Scraped results section](#mark-scraped-results)**

This repo contains a working mirror of the [Biden-Harris Transition Agency Review Teams announcement page](https://buildbackbetter.com/the-transition/agency-review-teams/) – and the wget script and other code to reproduce that mirror.

- Mirror: https://wgetsnaps.github.io/biden-harris-transition-teams/
- Original: https://buildbackbetter.com/the-transition/agency-review-teams/
- Wayback: http://web.archive.org/save/https://buildbackbetter.com/the-transition/agency-review-teams/
- Last updated: 2020-11-10


<a href="https://wgetsnaps.github.io/biden-harris-transition-teams/">
<img src="assets/page-screenshot.png" alt="page-screenshot.png">
</a>

## Code and data

See [wgetsnap.sh](wgetsnap.sh) to check out the `wget` code for mirroring the page.

<a id="mark-scraped-results" name="mark-scraped-results"></a>

### Scraped results

> **Caveat:** This repo's [scraped data](scrape/data.csv) is provided as-is, with absolutely no assurances or promises about its accuracy or integrity, so use it at your own risk! Of course, feel free to inspect and re-run the [scraper script](scrape/scraper.py) yourself.

Because this mirrored page and its HTML tables have newsworthy information, I've added a scraper script – [scrape/scraper.py](./scrape/scraper.py) – which parses and extracts the tabular data from [docs/index.html](docs/index.html) and outputs it as CSV.

**The scraped results can be found at**: [scrape/data.csv](scrape/data.csv) 

Or, if you'd like to see an interactive preview of the data on Google Sheets, [click here](https://docs.google.com/spreadsheets/d/18N7JDh_s5jqzQEe8qHfGexFy7dXrsgMrQBIk_X0om5A/edit#gid=0)

<a href="https://docs.google.com/spreadsheets/d/18N7JDh_s5jqzQEe8qHfGexFy7dXrsgMrQBIk_X0om5A/edit#gid=0">
<img src="assets/preview-sheet.png" alt="preview-sheet.png">
</a>


## Related links

- @Transition46 tweet: https://twitter.com/Transition46/status/1326257434080522241
- @alexkotch critiquing the Biden-Harris transition teams: https://twitter.com/alexkotch/status/1326266162330669056
- Wayback snapshot of Donald Trump's agency landing teams page: https://web.archive.org/web/20161217040522/https://greatagain.gov/agency-landing-teams-54916f71f462

As annoying as it is to have to scrape the Biden transition page to get data, it's a big improvement from the previous administration's agency teams page, which was basically a [Medium blog post](https://web.archive.org/web/20161217040522/https://greatagain.gov/agency-landing-teams-54916f71f462
):


<a href="https://web.archive.org/web/20161217040522/https://greatagain.gov/agency-landing-teams-54916f71f462
">
    <img src="assets/2016-page-screenshot.png" alt="2016-page-screenshot.png">
</a>


## Developer notes

If you've cloned this repo and want to recreate the wget mirror yourself, check out the [Makefile](Makefile).

Basically:

- `make snap` to execute script(s) for creating a mirror of the target site mirroring the target site (if ./docs doesn't already exist)

- `make serve` to view the locally mirrored site

- `make clean`  to clean out an existing mirror (wget.log and ./docs/)


