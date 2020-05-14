import mdtraj
import numpy

# Here is the script to caculate the relative orientations between two spin labels within a system
# First, you need to know the atom index of the He, Ne, Ar, Kr and the spin center (Cu2+ in this case) 
# from the .gori.xyz files from ORCA calculations.
# 'conda activate' then 'conda activate mdtraj'

def get_vectors(topologyA, topologyB, trajA, trajB):
    # get the index of each atom of the two residues. He, Ne, Ar, Ke are the origin, x, y, and z direction.
    Cu1_idx = topologyA.atom(70).index
    He1_idx = topologyA.atom(71).index
    Ne1_idx = topologyA.atom(72).index
    Ar1_idx = topologyA.atom(73).index
    Kr1_idx = topologyA.atom(74).index
    Cu2_idx = topologyB.atom(70).index
    He2_idx = topologyB.atom(71).index
    Ne2_idx = topologyB.atom(72).index
    Ar2_idx = topologyB.atom(73).index
    Kr2_idx = topologyB.atom(74).index

    # get the coordinates of each atom
    Cu1_coords = trajA.xyz[:,Cu1_idx,:]
    He1_coords = trajA.xyz[:,He1_idx,:]
    Ne1_coords = trajA.xyz[:,Ne1_idx,:]
    Ar1_coords = trajA.xyz[:,Ar1_idx,:]
    Kr1_coords = trajA.xyz[:,Kr1_idx,:]
    Cu2_coords = trajB.xyz[:,Cu2_idx,:]
    He2_coords = trajB.xyz[:,He2_idx,:]
    Ne2_coords = trajB.xyz[:,Ne2_idx,:]
    Ar2_coords = trajB.xyz[:,Ar2_idx,:]
    Kr2_coords = trajB.xyz[:,Kr2_idx,:]

    # get the vectors of g_perpendicular, g_parallel, and Cu-Cu
    He1_Ne1 = Ne1_coords - He1_coords
    He1_Ar1 = Ar1_coords - He1_coords
    He1_Kr1 = Kr1_coords - He1_coords
    He2_Ne2 = Ne2_coords - He2_coords
    He2_Ar2 = Ar2_coords - He2_coords
    He2_Kr2 = Kr2_coords - He2_coords
    Cu_Cu = Cu2_coords - Cu1_coords

    return He1_Ne1, He1_Ar1, He1_Kr1, He2_Ne2, He2_Ar2, He2_Kr2, Cu_Cu

def get_angle(vector1, vector2):
    # get the angle between two vectors 
    vector1 = numpy.squeeze(vector1)
    vector2 = numpy.squeeze(vector2)
    dot = numpy.dot(vector1, vector2)
    mag_vector1 = numpy.linalg.norm(vector1)
    mag_vector2 = numpy.linalg.norm(vector2)
    angle = numpy.arccos(dot/(mag_vector1*mag_vector2))
    return angle

# Create empty lists to put the values of each angles in.
# Due to the unequal value of gxx and gyy, the angle between g_perpendicular are calculated between gxx of two labels# or between gyy of two labels 
# In this system where the two residues are identical, either residue can be considered containing A spin.
# Thus, the chi angles can have two sets of values.
parallel = []
perpendicular1 = []
perpendicular2 = []
chi1 = []
chi2 = []
a = 1

for i in range(1, 10000, 100):
    trajA = mdtraj.load_xyz("./input/frame"+str(i)+".gori.xyz",top="strip1.pdb")
    print(trajA)
    print("loaded A"+str(i))
    topologyA = trajA.topology
    trajB = mdtraj.load_xyz("./site2/input/frame"+str(i)+".gori.xyz",top="strip1.pdb")
    print("loaded B"+str(i))
    topologyB = trajB.topology
    He1_Ne1, He1_Ar1, He1_Kr1, He2_Ne2, He2_Ar2, He2_Kr2, Cu_Cu = get_vectors(topologyA, topologyB, trajA, trajB)
    par = get_angle(He1_Kr1, He2_Kr2)
    perp1 = get_angle(He1_Ne1, He2_Ne2)
    perp2 = get_angle(He1_Ar1, He2_Ar2)
    ch1 = get_angle(He1_Kr1, Cu_Cu)  
    ch2 = get_angle(He2_Kr2, Cu_Cu)  
    parallel.append(par)
    perpendicular1.append(perp1)
    perpendicular2.append(perp2)
    chi1.append(ch1) 
    chi2.append(ch2)
    a += 1
    print("frame",a,"done") 

final = numpy.stack((parallel,perpendicular1,perpendicular2,chi1,chi2))
final = (final/numpy.pi)*180

numpy.save("rigid_gtensor_ori_degree.npy", final)
