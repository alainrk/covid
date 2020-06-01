#!/bin/sh

echo "Load Italy and Regions data. Confirm (y/N)? "
read confirm
if [[ $confirm != "y" ]]; then
  echo "Ok, exit..."
  exit 0
fi

# ./load_italia.sh &&
# ./load_regioni.sh

i=1
curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-2020060$i.csv | tail -n +2 >> italia.csv
curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-2020060$i.csv | tail -n +2 >> regioni.csv
# curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-202005$i.csv | tail -n +2 >> italia.csv
# curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-202005$i.csv | tail -n +2 >> regioni.csv

exit 0
