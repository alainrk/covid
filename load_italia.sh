#!/bin/sh

curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-20200323.csv | head -1 > italia.csv

for i in $(seq 24 29); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-202002$i.csv | tail -n +2 >> italia.csv; done

for i in $(seq 1 9); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-2020030$i.csv | tail -n +2 >> italia.csv; done

for i in $(seq 10 31); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-202003$i.csv | tail -n +2 >> italia.csv; done

for i in $(seq 1 9); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-2020040$i.csv | tail -n +2 >> italia.csv; done

for i in $(seq 10 30); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-202004$i.csv | tail -n +2 >> italia.csv; done

for i in $(seq 1 9); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-2020050$i.csv | tail -n +2 >> italia.csv; done

for i in $(seq 10 31); do curl https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-202005$i.csv | tail -n +2 >> italia.csv; done
