#!/bin/bash
export TTIME=$(date +"%H:%M %A %d %B %Y")

sed -e "s/TTIME/$TTIME/g" templateSummary.html >coincidences.html

cat summary.txt |awk '{print "<tr><td class=\"gray\"><a href=\"coincidences/"$1".html\"><font color=\"blue\">"$1"</font></a></td><td class=\"ERRCODE"$3"\"><font color=\"black\">"$2"</font></a></td><td class=\"ERRCODE"$7"\"><font color=\"black\">"$4" +/- "$5"</font></a></td></tr>"}' >>coincidences.html

sed -i -e "s/ERRCODE0/green/g" coincidences.html
sed -i -e "s/ERRCODE1/yellow/g" coincidences.html
sed -i -e "s/ERRCODE2/red/g" coincidences.html

cat templateEnd.html >>coincidences.html
