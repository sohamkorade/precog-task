#!/bin/bash
# Subsample a csv file to N lines

N=100000

for f in "$@"
do
	echo "Subsampling from $f..."
	file=$(basename $f)
	dir=$(dirname $f)
	newfile=$dir/small_${file:0:-4}.csv
	header=$(head -n 1 $f)
	tail -n +2 $f | shuf -n $N -o $newfile && sed -i "1i$header" $newfile
done