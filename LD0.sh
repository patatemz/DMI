#!/bin/bash
num=("$@")

n=$#

	sortednum=($(printf "%s\n" "${num[@]}" | sort -n))
		echo "Sakartotie:" ${sortednum[@]}
		echo "MIN:" ${sortednum[0]}
		echo "MAX:" ${sortednum[n-1]}


	sum=0
		for((i=0;i<n;i++))
		do
			sum=`expr $sum + ${num[$i]}`
		done

	vidver=$sum/$n
		echo -n "AVG:"
		echo $vidver|bc

	if (( n%2 != 0 ))
	then
	        echo -n "MED:"
        	echo "${sortednum[($n-1)/2]}" | bc
	else
        	echo -n "MED:"
        	echo "scale=1;(${sortednum[$n/2]} + ${sortednum[$n/2-1]})/2" |bc
	fi
