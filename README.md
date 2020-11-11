# wget snapshot of TEMPLATE_SOMETHING

Updated: 2020-11-10

This repo contains a working mirror of [SOME_SITE](https://example.com/SOME_SITE), which is LOREM_IPSUM, and the wget script and other code to reproduce that mirror.

- Mirror: https://wgetsnaps.github.io/SOME_SITE/
- Original: https://example.com/SOME_SITE
- Wayback: https://web.archive.org/web/*/https://example.com/SOME_SITE/


## Script

See [wgetsnap.sh](wgetsnap.sh) to see the code.


## Related

- related link https://example.com
- related link 2 https://example.com


## Developer notes

If you've cloned this repo and want to recreate the wget mirror yourself, check out the [Makefile](Makefile).

Basically:

- `make snap` to execute script(s) for creating a mirror of the target site mirroring the target site (if ./docs doesn't already exist)

- `make serve` to view the locally mirrored site

- `make clean`  to clean out an existing mirror (wget.log and ./docs/)


