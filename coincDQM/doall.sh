#!/bin/bash
cat coinc|awk '{print "./coincDQM.sh",$1,$2,$3,$4,$5,$6,$7}'|bash

rm summary.txt

cat summary*-*.txt >>summary.txt

cp summary.txt /home/analisi/dqmcoincidences/
