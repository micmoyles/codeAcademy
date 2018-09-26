#!/usr/bin/env bash

:'
Given three integers (X , Y and Z)
representing the three sides of a triangle,
identify whether the triangle is Scalene, Isosceles, or Equilateral.
'
X=$1
Y=$2
Z=$3

if [ $X -ne $Y ] && [ $X -ne $Z ] && [ $Y -ne $Z ]
then
    echo SCALENE
elif [ $X -eq $Y ] && [ $X -eq $Z ] && [ $Y -eq $Z ]
then
    echo EQUILATERAL
elif [ $X -eq $Y ] || [ $X -eq $Z ] || [ $Y -eq $Z ]
then
    echo ISOSCELES
fi