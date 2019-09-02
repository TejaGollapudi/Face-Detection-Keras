# Fast Multi Face Detection 
### Sivateja Gollapudi
![examples from validation set](./examples/demo_gif.gif)

## Table of contents


### 1. Overview
A fast multi scale multi face detector based on SSD 512 model.
The model has been trained on Wider Faces dataset.

The best performing versions of the model have attained Average Precision of 72% on the easy validation set and 63% on the medium validation set. 

A research paper on this has been accepted in IEEE VITECON conference.


##### Link to Original SSD object detector
[SSD Object Detector Paper](https://arxiv.org/abs/1512.02325)

##### Code inspired from 
The keras code for SSD and its utilities have been based on   [GitHub - pierluigiferrari/ssd_keras: A Keras port of Single Shot MultiBox Detector](https://github.com/pierluigiferrari/ssd_keras).

### 2. To Do

A ipython notebook for training various model versions will be uploaded soon.
Currently the plain SSD_512 version of the model has been uploaded.

There are multiple different versions with different architectural changes such as 
1. Incorporation of Context module from [SSH](https://arxiv.org/abs/1708.03979).
2. .[Feature Pyramid Networks for Object Detection](https://arxiv.org/abs/1612.03144)
3. Usage of Different number of detection layers
4. Usage of  various aspect ratios

These models and thier weights will be uploaded soon.

### 3. Download Weights

Download the model weights from [Google drive links for weights](https://drive.google.com/open?id=1LYgHEHtU-_J_UKoh8IJ5YI92viEAbvTz) and place them in the ssd_512 folder.

### 4. Environment setup

The code has been run using Tensorflow version 1.7 as keras backend.
You can create a virutal environment if you are using Anaconda,

```
conda create -n yourenvname python=preffered python version
conda activate yourenvname
pip install tensorflow==1.7.0
```
Later on you can use the Tensorflow 1.7 enviroment again by simply activating the previous environment
```
conda activate yourenvname
```
To deactivate run 
```
conda deactivate 
```

### 5. Running the detector
To run the face detector on the video stream obtained from Pc's camera run 
live_demo.py.
```
python live_demo.py
```
To run the detector 

### 6. Examples



