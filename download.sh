curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-20200320.csv | head -1 > data.csv

for i in $(seq 24 29); do echo $i; done

for i in $(seq 24 29); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-202002$i.csv | tail -n +2 >> data.csv; done

for i in $(seq 1 9); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-2020030$i.csv | tail -n +2 >> data.csv; done

for i in $(seq 10 22); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-202003$i.csv | tail -n +2 >> data.csv; done