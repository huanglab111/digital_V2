import skimage.io as io
from glob import glob
import os
import numpy as np
import torch



root_key='20230527AD'
datapath='\\\\192.168.0.241\\Liaozhizhao\\HuanglabWork\\WorksNet\\BoneBlast\\'+root_key+'\\'
rootpath='./boneblast/'+root_key+'/'

if not os.path.exists(rootpath):
    os.mkdir(rootpath)
key='sample'

left=np.ones([670,670])/670
right=np.ones([480,480])/480
test=io.imread(datapath+'sample1\\1_001.tiff')
print(left.shape,test.shape,right.shape)
print(test.dot(right))