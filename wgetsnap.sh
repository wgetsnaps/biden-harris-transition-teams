#!/bin/sh

# this script makes a local subdirectory named ./docs, which is where wget saves its work

TARGET_URL=https://buildbackbetter.com/the-transition/agency-review-teams/

wget "${TARGET_URL}" \
      --adjust-extension \
      --convert-links \
      --directory-prefix=./docs/ \
      --mirror \
      --no-host-directories \
      --no-directories \
      --output-file /dev/stdout \
      --no-parent \
      --page-requisites \
  | tee ./wget.log


      # --include-directories 'STUFF/,MORE_STUFF/*' \
