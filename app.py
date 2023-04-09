import streamlit as ss


import numpy as np #standard
import plotly.express as px  #plots and graphing lib
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from PIL import Image

import tensorflow
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD,Adam
from tensorflow.keras.layers import Dense,Input,Flatten
from tensorflow.keras.applications.inception_v3 import InceptionV3,preprocess_input,decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# food =  "none"

def dic_maker(arr):
  """ dis takes in arr [[prob(1),prob(2),prob(3)......prob(n)]]
   and outputs [(1,prob(1)),(2,prob(2))]
   (basically some formatting to make life easier)"""
  dict_ = {}
  for ind in range(len(arr[0])):
    dict_[ind] = arr[0][ind]
  return sorted(dict_.items(), key=lambda x: x[1],reverse=True)[:3]


def dic_maker_tuple(tuple_arr):
  """ takes in [(x,y),(a,b)]
      outputs {x:y,a:b} (basically some formatting to make life easier)
  """
  dict_ = {}
  for tuple_ in tuple_arr:
    dict_[target_dict[tuple_[0]]] = tuple_[1]
  return dict_


def inception_no_gen(image):
  """ 
  prediction happens in this function
  super important, takes in image_path (/content/test_1/test/111.jpg)
  outputs: {1:prob(1),2:prob(2)}
  """
  #image_1 = tensorflow.keras.preprocessing.image.load_img(image_path)


  input_arr = tensorflow.keras.preprocessing.image.img_to_array(image)
  input_arr = preprocess_input(input_arr)
  input_arr = tensorflow.image.resize(input_arr,size = (256,256))
  input_arr = np.array([input_arr])  # Convert single image to a batch.
  predictions = model_saved.predict(input_arr)
  return dic_maker_tuple(dic_maker(predictions))

def predictNutrition(test_imgs):
  global food
  print('--------------')
  food = list(inception_no_gen(test_imgs).keys())[0]
  print(food)


#------streamlit starts here----------------

model_saved = tensorflow.keras.models.load_model("inception_food_rec_50epochs.h5")
target_dict = {0:"Bread",1:"Dairy_product",2:"Dessert",3:"Egg",4:"Fried_food",
                 5:"Meat",6:"Noodles/Pasta",7:"Rice",8:"Seafood",9:"Soup",10:"veggies/Fruit"}

target_nutrition = {"Bread": 67, "Dairy_product": 200, "Dessert": 140, "Egg": 75, "Fried_food": 196,
                 "Meat": 143, "Noodles/Pasta": 138, "Rice": 130, "Seafood": 204, "Soup": 74, "veggies/Fruit": 52}
ss.set_page_config(page_title = "Food Recognition using Inception V3", layout = "wide")
ss.title("An AI Based Neutirend Tracking and Analysis ")

ss.markdown(
'''
This is the final year group project for ECM IV-A Batch 13\n
''')

# ss.image("f1.jpg")
ss.markdown(
'''
- Training on 16,600 images yielded 90% accuracy on train and 76% accuracy on validation. over 50 epochs.
- This model is saved and used later
'''
)
ss.markdown(
'''
### Block Diagram
''')
ss.image("block_diagram.png")

ss.markdown('### Dataset Details and Classes')
ss.markdown('Data consists of 1.1GB of 16,600 images of different categories of food.')
ss.markdown('the categories of food that can be classified are ')
ss.markdown(
  '''
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
  '''
)
ss.markdown('Dataset is obtained from [kaggle](https://www.kaggle.com/trolukovich/food11-image-dataset)')


ss.markdown('### Food Recognition step - Upload Image')
image_path = ss.file_uploader("drop the image file here: ", type = ["jpg", "jpeg"])

if image_path:
  image = Image.open(image_path)
  predictNutrition(image)
  ss.image(image)
  ss.write("Nutrient Intake:-")
  ss.warning('**'+food+'(Intake)**'+': '+str(target_nutrition[food])+' calories')
  print(food)
  print(target_nutrition[food])

ss.markdown('''
This project is made by
- Ashwin Kumar Uppala 19311A1901
- Sanjana Reddy 19311A1908
- Raveena Ganji 19311A1958
''')
