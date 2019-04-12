## This is the PyTorch1.0 implement of SENet (train on NWPU-RESISC45 dataset)

Paper: [Squeeze-and-Excitation Networks](https://arxiv.org/pdf/1709.01507.pdf)


# Usage

### Prepare data

This code takes NWPU-RESISC45 dataset as example. You can download NWPU-RESISC45 dataset and put them as follows. 

```
├── train_resnext.py # train resnext script
├── train_senet.py # train senet script
├── split_datasets.py # split datasets script
├── se_resnet.py # network of se_resnet
├── se_resnext.py # network of se_resnext
├── resnext.py # network of resnext
├── read_image.py # my dataset read script
├── dataset # train and validation data
	├── train
		├──airplane
		   ├── ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']
		   ├──    ...
		   ├── ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']
		├──  ...
		├──wetland
	├── val
	    ├──airplane
		   ├── ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']
		   ├──    ...
		   ├── ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']
	    ├──  ...
	    ├──wetland
	
```

### Train

* If you want to train from scratch, you can run as follows:

```
python split_datasets.py
python train_senet.py --network se_resnext_50 --batch-size 256 --gpus 0,1,2,3

```

parameter `--network` can be `se_resnet_18` or `se_resnet_34` or `se_resnet_50` or `se_resnet_101` or `se_resnet_152` or `se_resnext_50` or `se_resnext_101` or `se_resnext_152`.

* If you want to train from one checkpoint, you can run as follows(for example train from `epoch_4.pth, the `--start-epoch` parameter is corresponding to the epoch of the checkpoint):

```
python train_senet.py --network se_resnext_50 --batch-size 256 --gpus 0,1,2,3 --resume output-senet/epoch_4.pth --start-epoch 4
```
