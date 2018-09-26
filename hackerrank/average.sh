#!/usr/bin/env bash
:'
Given N integers, compute their average correct to three decimal places.

Input Format
The first line contains an integer, N.
N lines follow, each containing a single integer.

Output Format
Display the average of the integers, rounded off to three decimal places.
'

read max
let x=0
let sum=0
while [ $x -lt $max ]
do
    read i
    let sum=$sum+$i
    let x=$x+1
done
echo $sum $max | awk {'printf("%0.3f\n", $1/$2)'}
# we can also use bc to handle the division
#  echo "160/100" | bc -l