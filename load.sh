#!/bin/sh

echo "Load Italy and Regions data. Confirm (y/N)? "
read confirm
if [[ $confirm != "y" ]]; then
  echo "Ok, exit..."
  exit 0
fi

./load_italia.sh &&
./load_regioni.sh

exit 0