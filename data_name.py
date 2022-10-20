import os

data_root = 'data_fixedtest.list'
f0 = open(data_root, 'r')
ori = f0.readlines()
f = open('data_val.list', 'w')
for line in ori:
    line = line.strip()
    rgb, dep_sp, dep = line.split(' ')
    rgb_info = rgb.split('/')
    new_rgb = "/".join(rgb_info[1:])
    dep_sp_info = dep_sp.split('/')
    new_dep_sp = "/".join(dep_sp_info[1:])
    dep_info = dep.split('/')
    new_dep = "/".join(dep_info[1:])

    f.write(new_rgb + ' ' + new_dep_sp + ' ' + new_dep + '\n')

f0.close()
f.close()
