import os
import random
import shutil


data_root = './data/MIPI/train/'
data_root2 = './data/MIPI2/'
f = open('./data/MIPI/data_train.list', 'r')
lines = f.readlines()
val_num = int(len(lines) * 0.1)
val_list = random.sample(lines, val_num)

f2_train = open('./data/MIPI2/data_train.list', 'w')
f2_val = open('./data/MIPI2/data_val.list', 'w')

fs = os.listdir(data_root)
for f in fs:
    f_full = os.path.join(data_root2, 'train', f, 'rgb')
    if os.path.exists(f_full):
        pass
    else:
        # os.mkdir(f_full)
        os.makedirs(f_full)

    f_full2 = os.path.join(data_root2, 'train', f, 'depth')
    if os.path.exists(f_full2):
        pass
    else:
        # os.mkdir(f_full2)
        os.makedirs(f_full2)

for line0 in lines:
    line = line0.strip()
    rgb, depth = line.split(' ')
    old_rgb_path = os.path.join(data_root, rgb)
    old_depth_path = os.path.join(data_root, depth)
    if line0 in val_list:
        rgb_info = rgb.split('/')
        depth_info = depth.split('/')
        new_rgb = rgb_info[0] + '_' + rgb_info[-1]
        new_depth = depth_info[0] + '_' + depth_info[-1]
        new_rgb_path = os.path.join(data_root2, 'test/rgb', new_rgb)
        new_depth_path = os.path.join(data_root2, 'test/depth', new_depth)
        shutil.copy(old_rgb_path, new_rgb_path)
        shutil.copy(old_depth_path, new_depth_path)
        f2_val.write('rgb/' + new_rgb + ' ' + 'depth/' + new_depth + '\n')
    else:
        new_rgb_path = os.path.join(data_root2, 'train', rgb)
        new_depth_path = os.path.join(data_root2, 'train', depth)
        shutil.copy(old_rgb_path, new_rgb_path)
        shutil.copy(old_depth_path, new_depth_path)
        f2_train.write(rgb + ' ' + depth + '\n')

f.close()
f2_train.close()
f2_val.close()

