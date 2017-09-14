#!/bin/bash
ls /home/analisi/coincidences/newana/$1/$2-$3*.root|tail --lines=$4 >lista
export last=$(tail --lines=1 lista|awk -F"/" '{print $7}')
export ts=$(tail --lines=1 lista|awk -F"/" '{print $7}'|awk -F"-" '{print $5"-"$6"-"$7}'|awk -F"." '{print "date -d"$1,"+%s"}'|bash)
export tsNow=$(date +%s)
let tsDiff=$tsNow-$ts
root -b -q -l DoMerge.C\(\"lista\",\"$2-$3d$4.root\"\)
root -b -q -l draw.C\(\"$2-$3d$4.root\",\"$2-$3d$4.png\",$5,\"$6\",\"$last\",$4,$7,$tsDiff\)


cp template.html $2-$3.html
sed -i "s|SCHOOLS|${2}-${3}|g" $2-$3.html
sed -i "s|DAYS|${4}|g" $2-$3.html
cp $2-$3.html /home/analisi/dqmcoincidences/.
