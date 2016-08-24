#!/bin/bash

# Create a base file for a particular problem
# Tong Jia
# 2016

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [PROBLEM #]";
    exit 1
fi


cd Chap${1:0:1}_*
folder=`pwd`

prob_file=$1.py
touch $prob_file

printf "%0.s#" {1..79} >> $prob_file
echo -e "" >> $prob_file
echo -e "#" >> $prob_file
echo -e "#" >> $prob_file
echo -e "#" >> $prob_file
echo -e "#" >> $prob_file
echo -e "#" >> $prob_file
printf "%0.s#" {1..79} >> $prob_file
echo -e "\n" >> $prob_file

echo -e "==================================================\n"
echo -e "Created:"

chapRegex='CtCI\/(.+)$'
if [[ $folder =~ $chapRegex ]]
then
    echo -e "    "${BASH_REMATCH[1]}/$prob_file
else
    echo -e "    "$folder/$prob_file
fi

echo -e "\n==================================================\n"
