import numpy as np
import pandas as pd

from pathlib import Path

import torch
from torch.utils.data.dataset import Dataset
from torchvision.io import read_image

class RectangleDataset(Dataset):
    """Fixed dimension rectangle dataset"""

    def __init__(self, csv_file, dataset_settings, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(csv_file, header=None)

        self.settings = dataset_settings

        self.transform = transform
        self.target_transform = target_transform
    
    def __len__(self):
        return len(self.img_labels)
    
    def __getitem__(self, idx):
        img_name = self.img_labels.iloc[idx, 0]
        img_path = Path(self.settings['path'])/img_name
        img = read_image(str(img_path))

        label = np.array([self.img_labels.iloc[idx, 1:]], dtype='float')
        print(label)
        label = self.reduction(label, self.settings['sample']['dim'])

        if self.transform:
            img = transform(img)

        if self.target_transform:
            label = target_transform(label)
        
        return {'image': img, 'label': label}
    
    def reduction(self, label, img_size):
        reduced_label = np.zeros_like(label)
        nbr_dim = len(img_size)

        #TODO: handle len(label)%nbr_dim = len(label)%nbr_dim case != 0

        for i in range(label.shape[-1]//nbr_dim):
            point = label[:, i*nbr_dim : (i+1)*nbr_dim]
            reduced_point = point/img_size
            print(point, img_size, reduced_point)
            reduced_label[:, i*nbr_dim : (i+1)*nbr_dim] = reduced_point
        
        return reduced_label