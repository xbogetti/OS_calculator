#!/bin/bash

for i in `seq 1 100 10000`; do
    grep "g(tot)" ${i}/frame${i}.oout | awk '{print $4}' >> gtens.txt
done 
