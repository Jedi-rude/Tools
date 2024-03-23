#/bin/bash

grep "href=" $1 | cut -d "/" -f 3 | grep $2 | cut -d '"' -f 1 | sort -u > $2-domain.txt
