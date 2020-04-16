#!/bin/bash

START="20200223"
DAY=$(date "+%Y%m%d")

i=0
while [[ $START < $DAY ]]; do
  echo $START, $DAY
  i=$(echo "$i + 1" | bc)
  echo $i
  DAY=$(date -v-${i}d "+%Y%m%d")
done