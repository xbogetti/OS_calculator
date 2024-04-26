=============
OS_calculator
=============
This set of scripts helps to calculate g-tensors and relative orientations between two EPR spin labels for selected frames of MD simulations.
First, run the MD simulation of your system and create a folder containing the topology file and coordinates file.
The example MD simulation were run using AMBER force field ff14SB, and the newly developed dHis-Cu2+ force field (https://pubs.acs.org/doi/full/10.1021/acs.jpcb.0c00739).
For information of running MD simulation with AMBER, please refer to https://ambermd.org/
For extracting relative frames for g-tensor analysis, CPPTRAJ (part of the AmberTools) and ORCA 4.2 (https://sites.google.com/site/orcainputlibrary/home) are used.
More information about predicting EPR using ORCA, please refer to https://www.orcasoftware.de/tutorials/spec/EPR.html.
The scipts get_pdb.sh, cpptraj.template, and orca.template are used to prepare the xyz files for selected frames of spin labels, and prepare the input files for ORCA calculations.
After the ORCA calculations are done, the gori.xyz files containing the g-tensor orientations will be used to calculate the relative orientations between two set of spin labels within the same system.
To calculate the relative orientations between two labels, chi (between g_parallel and spin-spin vector r), gamma (between g_parallel of two labels), and eta (between g_perpendicular of two labels) will be calculated using the orientation.py
Python installation is needed (https://www.python.org/). MDTraj is used here to analyze the angles and Numpy to write the values to files.
The get_gtens.sh is to extract the gxx, gyy and gzz values from the ORCA output files and make seperate files for them.
