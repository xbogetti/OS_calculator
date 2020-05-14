#!/bin/bash

# Here are the scripts extracting the xyz files of the residue for ORCA calculations.
# First, run the MD simulation of your system and create a folder containing the topology file and coordinates file.
# Make a pdb file of 1 frame, extract the last column of the residue you'd analyze and paste into atom.txt file.
# Know the number of atoms to analyze, here we have 71 atoms of the residue of interests 
# Copy the cpptraj.template, orca.template, and atom.txt file into this folder; try the script with one frame first.
# Extract the frames from the trajectory to analyze; here we extract every 100 frames out of 10000 frames to analyze
for i in `seq 1 100 10000`; do

# search and replace the word "FRAME" from the template with the current frame number, and run the cpptraj script
  sed -e s"/FRAME/${i}/g" cpptraj.template > cpptraj.in
  cpptraj -i cpptraj.in > /dev/null 2>&1
# Exclude the first and last two lines of the pdb, and extract the x, y and z coordinates into the txt files.
  cat frame${i}.pdb | tail -n +2 | head -n 71 > strip${i}.pdb
  awk {'print $6'} strip${i}.pdb > x.txt
  awk {'print $7'} strip${i}.pdb > y.txt
  awk {'print $8'} strip${i}.pdb > z.txt
# Paste the atoms, corresponding x, y and z coordinates of each atom into the temp.txt,
# and add the number of atoms to the first line, and add a blank line after it.
# The xyz file name of i'th frame is framei.xyz
  paste atoms.txt x.txt y.txt z.txt > temp.txt
  awk 'BEGIN{print""}1' temp.txt > temp2.txt
  awk 'BEGIN{print""}1' temp2.txt > temp3.txt
  vim -c "1 s/^/71/" -c "wq" temp3.txt
  mv temp3.txt frame${i}.xyz
  sed s/FILE/frame${i}.xyz/ orca.template > frame${i}.inp
  rm temp.txt temp2.txt
  echo finished frame$i
done
