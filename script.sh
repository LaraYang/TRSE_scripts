#!/bin/bash
# bash command-line arguments are accessible as $0 (the bash script), $1, etc.
# echo "Running" $0 "on" $1
subjects=$(ls * | grep 14[0-9][0-9]- | sed s/-[0-9].txt// | sort -u)

for file in $subjects; do
	echo $file	
	echo $file | python pscript.py
done
# for((n=1401; n<=1431; n++))
# do
  # if [ "$n" -ne 1410 ] && [ "$n" -ne 1420 ] && [ "$n" -ne 1424 ] && [ "$n" -ne 1425 ] && [ "$n" -ne 1428 ]
  	# then echo "$n" | python pscript.py
  # fi
# done
