import scipy.io
import numpy as np
import

mat = scipy.io.loadmat('EyeBlinks/1Blink5Sec.mat')['Baseline_Segment_03']
print mat[1,:]
print mat[2,:]

# save('EyeBlinks/1Blink5Sec.mat','-v7')
# mat1 = scipy.io.loadmat('EyeBlinks/Baseline.mat').keys()
# mat2 = scipy.io.loadmat('EyeBlinks/1Blink5Sec.mat').keys()
# mat3 = scipy.io.loadmat('EyeBlinks/2Blink4Seconds.mat').keys()
# mat4 = scipy.io.loadmat('EyeBlinks/2Blink5Sec.mat').keys()
# mat5 = scipy.io.loadmat('EyeBlinks/3Blink2Seconds.mat').keys()
# mat6 = scipy.io.loadmat('EyeBlinks/3Blink5Sec.mat').keys()
# mat7 = scipy.io.loadmat('EyeBlinks/4Blink3Seconds.mat').keys()
# mat8 = scipy.io.loadmat('EyeBlinks/4Blink5Sec.mat').keys()
# mat9 = scipy.io.loadmat('EyeBlinks/4Blinks4Seconds.mat').keys()

# print mat1
# print mat2
# print mat3
# print mat4
# print mat5
# print mat6
# print mat7
# print mat8
# print mat9