import numpy
  
angles = numpy.load("gtensor_ori_degree.npy")
par = angles[0]
perp1 = angles[1]
perp2 = angles[2]
chi1 = angles[3]
chi2 = angles[4]
numpy.savetxt("gamma_degree.txt", par, delimiter=",")
numpy.savetxt("neta1_degree.txt", perp1, delimiter=",")
numpy.savetxt("neta2_degree.txt", perp2, delimiter=",")
numpy.savetxt("chi1_degree.txt", chi1, delimiter=",")
numpy.savetxt("chi2_degree.txt", chi2, delimiter=",")

