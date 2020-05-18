#!/bin/bash

for i in `seq 1 1 10`; do
  sed -e s"/FRAME/${i}/g" cpptraj.template > cpptraj.in
  cpptraj -i cpptraj.in > /dev/null 2>&1
  cat frame${i}.pdb | tail -n +2 | head -n 46 > strip${i}.pdb
  awk {'print $6'} strip${i}.pdb > x.txt
  awk {'print $7'} strip${i}.pdb > y.txt
  awk {'print $8'} strip${i}.pdb > z.txt
  paste atoms.txt x.txt y.txt z.txt > temp.txt
  awk 'BEGIN{print""}1' temp.txt > temp2.txt
  awk 'BEGIN{print""}1' temp2.txt > temp3.txt
  vim -c "1 s/^/46/" -c "wq" temp3.txt
  mv temp3.txt frame${i}.xyz
  sed s/FILE/frame${i}.xyz/ orca.template > frame${i}.inp
  rm temp.txt temp2.txt
  echo finished frame$i
done
