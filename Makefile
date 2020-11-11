.PHONY: help clean serve
.DEFAULT_GOAL := help


# Loosely define the expected starting point of the mirrored site, locally speaking
EXPECTED_MIRROR_INDEX_FILE = ./docs/index.html



# a bunch of code so that `make serve` can automatically pop open a browser at the expected index file
define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"


define HELP_NOTE
- `make snap` to execute script(s) for creating a mirror of the target site mirroring the target site (if ./docs doesn't already exist)

- `make serve` to view the locally mirrored site

- `make clean`  to clean out an existing mirror (wget.log and ./docs/)

Look at Makefile for more info!
endef
export HELP_NOTE

help:
	echo "$$HELP_NOTE"

clean:
	rm -fr docs/
	rm -f wget.log

docs/index.html:
	./wgetsnap.sh

snap: $(EXPECTED_MIRROR_INDEX_FILE)


serve: $(EXPECTED_MIRROR_INDEX_FILE)
	@echo "Opening $< in web browser..."
	@sleep 0.3
	$(BROWSER) $<

