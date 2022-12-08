#!/bin/bash
url=$1

python3 add_rule.py ${url}
git commit -m "add policy" -a & git push