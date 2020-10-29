from keras import backend as K
from keras.models import load_model
from keras.preprocessing import image
from keras.optimizers import Adam,SGD
import numpy as np
from matplotlib import pyplot as plt
import cv2
import sys

from models.keras_ssd512 import ssd_512
from keras_loss_function.keras_ssd_loss import SSDLoss
from keras_layers.keras_layer_AnchorBoxes import AnchorBoxes
from keras_layers.keras_layer_DecodeDetections import DecodeDetections
from keras_layers.keras_layer_DecodeDetectionsFast import DecodeDetectionsFast
from keras_layers.keras_layer_L2Normalization import L2Normalization

from ssd_encoder_decoder.ssd_output_decoder import decode_detections, decode_detections_fast


img_height = 512
img_width = 512
print('-'*80+'\n')
print('\t'*5+'INITITALIZING SESSSION')
K.clear_session() # Clear previous models from memory.

if len(sys.argv)!=2:
    print('\n'*2)

    print('\t Please provide path to the video file as a command line arg')
    print('\t python demo.py ./path/to/video/file.avi')
    exit()


img_height = 512 # Height of the model input images
img_width = 512 # Width of the model input images
img_channels = 3 # Number of color channels of the model input images
mean_color = [123, 117, 104] # The per-channel mean of the images.
swap_channels = [2, 1, 0] # The color channel order in the original SSD is BGR, so we'll have the model reverse the color channel order of the input images.
n_classes = 1 # Number of Classes excluding background class
scales = [0.07, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05] # The anchor box scaling factors used in the original SSD300 for the Pascal VOC datasets
aspect_ratios = [[1.0],
                 [1.0],
                 [1.0],
                 [1.0],
                 [1.0],
                 [1.0],
                 [1.0]
                ] 
two_boxes_for_ar1 = True
steps = [8, 16, 32, 64, 128, 256,512] # The space between two adjacent anchor box center points for each predictor layer.
offsets = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5,0.5] # The offsets of the first anchor box center points from the top and left borders of the image as a fraction of the step size for each predictor layer.
clip_boxes = False # Whether or not to clip the anchor boxes to lie entirely within the image boundaries
variances = [0.1, 0.1, 0.2, 0.2] # The variances by which the encoded target coordinates are divided as in the original implementation
normalize_coords = True



model = ssd_512(image_size=(img_height, img_width, img_channels),
                n_classes=n_classes,
                mode='training',
                l2_regularization=0.0005,
                scales=scales,
                aspect_ratios_per_layer=aspect_ratios,
                two_boxes_for_ar1=two_boxes_for_ar1,
                steps=steps,
                offsets=offsets,
                clip_boxes=clip_boxes,
                variances=variances,
                normalize_coords=normalize_coords,
                subtract_mean=mean_color,
                swap_channels=swap_channels)

# 2: Load some weights into the model.
print('-'*80+'\n')
print('\t'*5+'Loading Weights')

# TODO: Set the path to the weights you want to load.
weights_path = './ssd_512/ssd512_face_epoch-31_loss-2.9192_val_loss-3.1465.h5'

model.load_weights(weights_path, by_name=True)

print('-'*80+'\n')
print('\t'*5+'Weights Loaded')

model.summary()

print('-'*80+'\n')
print('\t'*5+'Initiating Video Capture')
print('\t'*5+ 'Press  q   to quit')


#load the video
cap = cv2.VideoCapture(str(sys.argv[1])) 



while True:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(512,512))
    frame2=frame
    frame= frame[...,::-1] #convert from rgb to bgr
    frame=np.expand_dims(frame, axis=0)
    y_pred = model.predict(frame)
    y_pred_thresh = decode_detections(y_pred,
                                   confidence_thresh=0.3,
                                   iou_threshold=0.5,
                                   top_k=200,
                                   normalize_coords=normalize_coords,
                                   img_height=img_height,
                                   img_width=img_width)

    np.set_printoptions(precision=2, suppress=True, linewidth=90)
    
    
    classes = ['background',
           'face']


    current_axis = plt.gca()


    for box in y_pred_thresh[0]:
    	cv2.rectangle(frame2, (int(box[2]),int( box[3])), (int(box[4]), int(box[5])), (0, 255, 255), 5) 
    cv2.imshow("faces detection", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to stop capture 
        break
cap.release()
cv2.destroyAllWindows()