# Fast Multi Face Detection 
### Sivateja Gollapudi


A fast multi scale multi face detector based on SSD 512 model.

[SSD Object Detector Paper](https://arxiv.org/abs/1512.02325)

The keras code for SSD_512 model and its utilities have been inspired by and taken from  [GitHub - pierluigiferrari/ssd_keras: A Keras port of Single Shot MultiBox Detector](https://github.com/pierluigiferrari/ssd_keras).

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
To run the face detector on the video stream obtained from Pc's camera run 
live_demo.py.
```
python live_demo.py
```
The code has been run on Tensorflow version 1.7. 