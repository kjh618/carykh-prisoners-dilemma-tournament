#!/bin/bash

for i in $(seq 1 $1)
do
    echo "Run $i"
    time python3 prisonersDilemma.py && mv results.txt results$i.txt
    echo
done
