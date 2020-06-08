#!/usr/bin/env bash
cut -d',' -f18 flightdelays.csv | sort | uniq -c | sort -rn | head -3 > topdest.csv
echo "Number_of_ArrPlane Dest" > header1.csv
cat header1.csv topdest.csv > top3dest.csv
csvlook top3dest.csv

