import os, fnmatch
import sys
import os.path as ops
import scipy.io as scio
from math import log10
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import random
from utils.init_weights import define_init_weights

def define_model(arch):
    # 1. define model structure
    if arch == 'EMDC':
        from models.EMDC import dcmodel
        model = dcmodel().cuda()
    
    elif arch == 'CSPN':
        from models.cspn.torch_resnet_cspn_nyu import resnet18, resnet50
        cspn_config = {'step': 24, 'norm_type': '8sum'}  # cspn_step=24, cspn_norm_type=8sum
        model = resnet50(pretrained=True, cspn_config=cspn_config).cuda()

    elif arch == 'Fusion':
        from models.fusion import define_model
        model = define_model(mod='mod', in_channels=4, thres=0)
        define_init_weights(model, 'kaiming')
        
    # elif arch == 'PENet':
    #     from models.PENet import dcmodel
    #     model = dcmodel().cuda()

    else:
        print('Unsupported model structure!')
        sys.exit(1)
    
    return model