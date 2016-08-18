#!/bin/bash

# Run a particular problem
# Tong Jia
# 2016

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [PROBLEM #]";
    exit 1
fi


cd Chap${1:0:1}_*
prob_file=`ls $1_*.py`
folder=`pwd`

echo -e "==================================================\n"
echo -e "Running:"

chapRegex='CtCI\/(.+)$'
if [[ $folder =~ $chapRegex ]]
then
    echo -e "    "${BASH_REMATCH[1]}/$prob_file
else
    echo -e "    "$folder/$prob_file
fi
echo -e ""

python $prob_file

echo -e "\n==================================================\n"
