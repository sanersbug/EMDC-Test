import cv2

# target = './data/MIPI2/test/depth/BeachApartmentInterior_My_ir_Image0003.exr'
target = '00000_depth_sparse.exr'
# target = 'Image0976.exr'
# target = '0.exr'
# target = 'Image0001.exr'
np_tar = cv2.imread(target, cv2.IMREAD_ANYDEPTH)
# print(np_tar)
print(np_tar[np_tar>0])