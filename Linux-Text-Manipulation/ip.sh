#/bin/bash

cat $1 | cut -d " " -f 4 | sort -u
