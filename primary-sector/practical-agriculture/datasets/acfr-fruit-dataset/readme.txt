Dataset properties:

Mango data image properties:
# Items: 1964
# Properties: PNG image data, 500 x 500, 16-bit/color RGB, non-interlaced
# Annotations: Rectangles: #item,x,y,dx,dy,label

Apple data image properties:
# Items: 1120
# Properties: PNG image data, 308 x 202, 8-bit/color RGB, non-interlaced
# Annotations: Circles: #item,c-x,c-y,radius,label

Almond data image properties:
# Items: 620
# Properties: PNG image data, 300 x 300, 8-bit/color RGB, non-interlaced
# Annotations: Rectangles: #item,x,y,dx,dy,label

Dataset Structure:
acfr-fruit-dataset
├── almonds
│   ├── annotations
│   ├── images
│   ├── labelmap.json
│   └── sets
│       ├── all.txt
│       ├── test.txt
│       ├── train.txt
│       ├── train_val.txt
│       └── val.txt
├── apples
│   ├── annotations
│   ├── images
│   ├── labelmap.json
│   ├── segmentations
│   └── sets
│       ├── all.txt
│       ├── test.txt
│       ├── train.txt
│       ├── train_val.txt
│       └── val.txt
├── mangoes
│   ├── annotations
│   ├── images
│   ├── labelmap.json
│   └── sets
│       ├── all.txt
│       ├── test.txt
│       ├── train.txt
│       ├── train_val.txt
│       └── val.txt
└── readme.txt

Dataset info:
-Each fruit contains an images, annotations and sets folder, along with a labelmap.json file for mapping labels to id.
-The images contained within are random crops extracted from data otherwise densely collected over the farms. The image names are typically appended with the ij co-ordinate or image sections from which the particular crop was extracted from. Refer to [1] for further information on data gathering.
-The Annotations folder contains corresponding .csv files with the same names as the images, with fruit annotation information per line.
-The sets folder contains the dataset splits (list of image names) as used in [1] for training, testing and validation.
For apples, the segemntation folder contains png files with pixel-wise annotations of apples.

[1] Bargoti, S., & Underwood, J. (2016). Deep Fruit Detection in Orchards. arXiv preprint arXiv:1610.03677. [Submitted to ICRA (2017)]


