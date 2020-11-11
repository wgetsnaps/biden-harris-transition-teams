#!/bin/sh

# this script makes a local subdirectory named ./docs, which is where wget saves its work

TARGET_URL=https://www.example.com/

wget "${TARGET_URL}" \
      --adjust-extension \
      --convert-links \
      --directory-prefix=./docs/ \
      --include-directories 'STUFF/,MORE_STUFF/*' \
      --no-host-directories \
      --output-file /dev/stdout \
      --page-requisites \
      --recursive --level 1 \
      --span-hosts \
  | tee ./wget.log
