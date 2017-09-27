developer: F. Noferini

Description
Files needed to update the dqm page for coincidences

Assuming to have a copy of the content of this dir in
/home/analisi/coincDQM
otherwise change the cron below accordingly

a cronjob is running in the eee-analysis-user machine as analisi user (all days at 12.00)
0 12 * * * cd /home/analisi/coincDQM;./doall.sh

input files are expected to be in the same machine in
/home/analisi/coincidences/newana/
otherwise change coincDQM.sh accordingly

the results of the cron are expected to be loaded in
/home/analisi/dqmcoincidences/
and then parsed by other scripts
If path changes, please fix it in
coincDQM.sh
doall.sh
draw.C
