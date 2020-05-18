#!/bin/bash

for i in `seq 1 1 10`; do
    grep "g(tot)" ${i}/frame${i}.oout | awk '{print $2}' >> gxx.txt
    grep "g(tot)" ${i}/frame${i}.oout | awk '{print $3}' >> gyy.txt
    grep "g(tot)" ${i}/frame${i}.oout | awk '{print $4}' >> gzz.txt
done 
