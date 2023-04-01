# An AI Based Neutirend Tracking and Analysis
Food recognition deployed on streamlit with inception v3 backend
#### Deployed at [Streamlit](https://ashwinexe-fyp-f00d-recog-inception-bhdsz4.streamlit.app/)


In this project, we propose a novel system based on artificial intelligence (AI) to accurately estimate nutrient intake, by processing image pairs captured in day meal consumption. This allows sequential food segmentation, recognition, and estimation of the consumed food volume, permitting fully automatic estimation of the nutrient intake for each meal. For this development and evaluation of the system, a dedicated new database containing images and nutrient recipes of large variety of meals must be assembled and coupled.

### Learning details
- The paper for Inception can be found [here](https://arxiv.org/abs/1512.00567v3)

- The paper implementation using pytorch can be found [here](https://github.com/pytorch/vision/blob/6db1569c89094cf23f3bc41f79275c45e9fcb3f3/torchvision/models/inception.py#L64)

- Inception-v3 is a convolutional neural network architecture from the Inception family that makes several improvements including using 
  - Label Smoothing,
  - Factorized 7 x 7 convolutions,\n 
  and the use of an auxiliary classifer to propagate label information lower down the network (along with the use of batch normalization for layers in the sidehead).
- Training on 16,600 images yielded 90% accuracy on train and 76% accuracy on validation. over 50 epochs!
- This model is saved and used later

### Model Architecture

![architecture](https://github.com/sirreajohn/F00d_recognition/blob/master/inception_2.png)
### Dataset Details and Classes
Data consists of 1.1GB of 16,600 images of different categories of food.
the categories of food that can be classified are 

    - Bread
    - Dairy Product
    - Dessert
    - Egg
    - Fried Food
    - Meat
    - Noodles-pasta
    - Rice
    - Seafood
    - Soup
    - Vegetable-fruit
    
Dataset is obtained from [kaggle](https://www.kaggle.com/trolukovich/food11-image-dataset)
