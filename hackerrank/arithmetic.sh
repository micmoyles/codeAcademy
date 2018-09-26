#!/usr/bin/env bash

:'
We provide you with expressions containing +,-,*,^, / and parenthesis.
None of the numbers in the expression involved will exceed 999.
Your task is to evaluate the expression and display the correct output rounding upto decimal places.
'

exp=$1
# remove whitespace
exp=$( echo $exp | sed 's/ //g')
echo $exp

# first check mulitplications '*'
if [ $exp 
