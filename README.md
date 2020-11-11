# wget snapshot of TEMPLATE_SOMETHING

Updated: 2020-11-10

This repo contains a working mirror of the [Biden-Harris Transition Agency Review Teams announcement page](https://buildbackbetter.com/the-transition/agency-review-teams/) – and the wget script and other code to reproduce that mirror.

- Mirror: https://wgetsnaps.github.io/biden-harris-transition-teams/
- Original: https://buildbackbetter.com/the-transition/agency-review-teams/
- Wayback: http://web.archive.org/save/https://buildbackbetter.com/the-transition/agency-review-teams/


## Script

See [wgetsnap.sh](wgetsnap.sh) to see the code.


## Related

- @Transition46 tweet: https://twitter.com/Transition46/status/1326257434080522241
- @alexkotch critiquing the announced teams: https://twitter.com/alexkotch/status/1326266162330669056

## Developer notes

If you've cloned this repo and want to recreate the wget mirror yourself, check out the [Makefile](Makefile).

Basically:

- `make snap` to execute script(s) for creating a mirror of the target site mirroring the target site (if ./docs doesn't already exist)

- `make serve` to view the locally mirrored site

- `make clean`  to clean out an existing mirror (wget.log and ./docs/)


