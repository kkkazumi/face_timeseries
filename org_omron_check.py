import numpy as np

filepath = "/home/kazumi/prog/test/kitekan_plot_test/1/signal_before.csv"
data = np.loadtxt(filepath,delimiter="\t")
hap=data[:,0]
print(hap)
print(np.sort(hap))
print(np.argsort(hap))

