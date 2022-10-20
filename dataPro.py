import os

data_root = './data/nyudepthv2/val/'
cls_names = os.listdir(data_root)
f = open('data_val.list', 'w')
for cls_name in cls_names:
    cls_full_path = os.path.join(data_root, cls_name)
    ths = os.listdir(cls_full_path)
    for th in ths:
        th_path = cls_name + '/' + th
        f.write(th_path + '\n')

f.close()