#!/usr/bin/env bash

x=$1
y=$2

let diff=$x-$y

if [ $x == $y ]
then
    echo Even
fi
if [ $x -gt $y ]
then
    echo X larger
fi
if [ $x -lt $y ]
then
    echo X smaller
fi
