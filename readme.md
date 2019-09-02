# Fast Multi Face Detection 
### Sivateja Gollapudi
<Br>
  
![Examples from validation set](./examples/demo_gif.gif)
  The images in the gif are obtained from running the model on the validation set of Wider Faces dataset.


## Table of contents
  1. [Overview](#overview)
  2. [To Do](#todo)
  3. [Download Weights](#weights)
  4. [Environment Setup](#setup)
  5. [Running The Detector](#detector)


### 1. Overview <a name=overview></a>
A fast multi scale multi face detector based on SSD 512 model.
The model has been trained on [Wider Faces dataset](http://shuoyang1213.me/WIDERFACE/).

The best performing versions of the model have attained Average Precision of 72% on the easy validation set and 63% on the medium validation set. 

A research paper on this has been accepted in IEEE VITECON conference.


##### Link to Original SSD object detector
[SSD Object Detector Paper](https://arxiv.org/abs/1512.02325)

##### Code inspired from 
The keras code for SSD and its utilities have been based on   [GitHub - pierluigiferrari/ssd_keras: A Keras port of Single Shot MultiBox Detector](https://github.com/pierluigiferrari/ssd_keras).

### 2. To Do <a name="todo"></a>

A ipython notebook for training various model versions will be uploaded soon.
Currently the plain SSD_512 version of the model has been uploaded.

There are multiple different versions with different architectural changes such as 
1. Incorporation of Context module from [SSH](https://arxiv.org/abs/1708.03979).
2. .[Feature Pyramid Networks for Object Detection](https://arxiv.org/abs/1612.03144)
3. Usage of Different number of detection layers
4. Usage of  various aspect ratios

These models and thier weights will be uploaded soon.

### 3. Download Weights<a name="weights"></a>

Download the model weights from [Google drive links for weights](https://drive.google.com/open?id=1LYgHEHtU-_J_UKoh8IJ5YI92viEAbvTz) and place them in the ssd_512 folder.

### 4. Environment setup <a name="setup"></a>

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

### 5. Running the detector <a name="detector"></a>
To run the face detector on the video stream obtained from Pc's camera run 
live_demo.py.
```
python live_demo.py
```
To run the detector 




