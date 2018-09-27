#!/usr/bin/env bash
# for challenge
# https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns/problem
# working with arrays
# tutorials here - https://www.thegeekstuff.com/2010/06/bash-array-tutorial/

for i in {0..500}
do
read country
if [[ $country == '' ]]
    then
    break
fi
countries[$i]=$country
done

echo ${countries[@]/*[A|a]*/}

# to concatenate the array 3 times
# https://www.hackerrank.com/challenges/bash-tutorials-concatenate-an-array-with-itself/problem
echo ${countries[@]} ${countries[@]} ${countries[@]}
