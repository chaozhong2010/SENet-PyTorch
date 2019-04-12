from torchvision import transforms, datasets
import os
import torch
from PIL import Image
import scipy.io as scio

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']

def ImageNetData(args):
# data_transform, pay attention that the input of Normalize() is Tensor and the input of RandomResizedCrop() or RandomHorizontalFlip() is PIL Image
    data_transforms = {
        'train': transforms.Compose([
            transforms.Resize(256),
            transforms.RandomCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'val': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    image_datasets = {x: datasets.ImageFolder(os.path.join(args.data_dir, x),
                                          data_transforms[x])
                     for x in ['train', 'val']}
    # wrap your data and label into Tensor
    dataloders = {x: torch.utils.data.DataLoader(image_datasets[x],
                                                 batch_size=args.batch_size,
                                                 shuffle=True,
                                                 num_workers=args.num_workers) for x in ['train', 'val']}


    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
    return dataloders, dataset_sizes




    # train_data = datasets.ImageFolder(args.data_dir, transform=train_transforms)
    # print("the size of train_data: ", train_data[0][0].size())
    # test_data = datasets.ImageFolder(args.data_dir, transform=test_transforms)
    #
    # num_train = len(train_data)  # 训练集数量
    # indices = list(range(num_train))  # 训练集索引
    # split = int(np.floor(vaild_size * num_train))  # 获取20%数据作为验证集
    # np.random.shuffle(indices)  # 打乱数据集
    #
    # from torch.utils.data.sampler import SubsetRandomSampler
    # train_idx, test_idx = indices[split:], indices[:split]  # 获取训练集，测试集
    # train_sampler = SubsetRandomSampler(train_idx)  # 打乱训练集，测试集
    # test_sampler = SubsetRandomSampler(test_idx)
    #
    # ############################数据加载器：加载训练集，测试集###################
    # train_loader = DataLoader(train_data, sampler=train_sampler, batch_size=4)
    # test_loader = DataLoader(test_data, sampler=test_sampler, batch_size=16)
    # return train_loader, test_loader
