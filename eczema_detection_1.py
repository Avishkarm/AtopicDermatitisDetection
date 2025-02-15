# -*- coding: utf-8 -*-
"""eczema_detection_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aAKVcHT4wAzUZvB9OlJcSKea2t2PRdTw

This file uses pre-trained model to
1. classify images as eczema or non-eczema
2. determine the level of eczema
"""

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

!pip install tensorflow-hub

# Commented out IPython magic to ensure Python compatibility.
# Clone the GitHub repository
!git clone https://github.com/biswa932/EczemaDetectionUsingCNN.git

# Navigate to the cloned repository
# %cd EczemaDetectionUsingCNN

# Verify if the model file is downloaded
!ls

"""# Classifying as eczema or non - eczema"""

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.models import load_model

# Define the model path
model_path = "/content/EczemaDetectionUsingCNN/eczemaDetection.h5"

# Load the model without compiling
model = load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)

# Recompile the model with the correct loss and optimizer
model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Display model structure
model.summary()

"""To prompt user to input a single image and check for eczema."""

import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from google.colab import files

# Function to preprocess the image
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)  # Load image
    img_array = img_to_array(img) / 255.0  # Convert to array and normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Prompt user to upload an image
print("Please upload an image for classification:")
uploaded = files.upload()

# Get the uploaded file's path
for filename in uploaded.keys():
    image_path = filename

# Preprocess the image
input_image = preprocess_image(image_path)

# Make predictions
predictions = model.predict(input_image)

# Interpret the results
class_names = ['Non-Eczema', 'Eczema']
predicted_class = class_names[np.argmax(predictions)]

# Display results
print(f"Predicted Class: {predicted_class}")
print(f"Confidence Scores: {predictions[0]}")

"""To apply the model reccursively to multiple images. (Images have been saved in a folder in google drive)"""

import os
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from google.colab import drive

# Function to preprocess the image
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)  # Load image
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Path to the folder in your Google Drive
folder_path = "/content/drive/My Drive/eczema_eyes/unseen_images"  # Replace with your folder path

# Get a list of all files in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Classify each image in the folder
class_names = ['Non-Eczema', 'Eczema']

for image_path in image_files:
    print(f"Processing image: {os.path.basename(image_path)}")

    # Preprocess the image
    input_image = preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(input_image)

    # Interpret the results
    predicted_class = class_names[np.argmax(predictions)]
    confidence_scores = predictions[0]

    # Display results
    print(f"Predicted Class: {predicted_class}")
    print(f"Confidence Scores: {confidence_scores}")
    print("-" * 50)

"""# Eczema Level Detection"""

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.models import load_model

# Define the model path
model_path = "/content/EczemaDetectionUsingCNN/eczemaLevelDetection.h5"

# Load the model without compiling
model = load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)

# Recompile the model with the correct loss and optimizer
model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Display model structure
model.summary()

"""To prompt user to input a single image and determine the level/severity of eczema."""

import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from google.colab import files

# Function to preprocess the image
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)  # Load image
    img_array = img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Class labels for eczema levels
class_names = ['Mild', 'Moderate', 'Severe']  # Update labels if different

# Prompt the user to upload an image
print("Please upload an image for eczema level detection:")
uploaded = files.upload()

# Process the uploaded image
for filename in uploaded.keys():
    image_path = filename  # Get the path of the uploaded image
    input_image = preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(input_image)

    # Interpret the results
    predicted_class = class_names[np.argmax(predictions)]
    confidence_scores = predictions[0]

    # Display the results
    print(f"\nImage: {filename}")
    print(f"Predicted Eczema Level: {predicted_class}")
    print(f"Confidence Scores: {confidence_scores}")

"""To apply the model reccursively to multiple images. (Images have been saved in a folder in google drive)"""

import os
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from google.colab import drive

# Function to preprocess the image
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)  # Load image
    img_array = img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Mount Google Drive
drive.mount('/content/drive')

# Path to the folder in your Google Drive
folder_path = "/content/drive/My Drive/eczema_eyes/unseen_images"  # Replace with your folder path

# Get a list of all image files in the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Class labels for eczema levels (Update based on your model's output classes)
class_names = ['Mild', 'Moderate', 'Severe']  # Update class labels if needed

# Classify each image in the folder
for image_path in image_files:
    print(f"Processing image: {os.path.basename(image_path)}")

    # Preprocess the image
    input_image = preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(input_image)

    # Interpret the results
    predicted_class = class_names[np.argmax(predictions)]
    confidence_scores = predictions[0]

    # Display results
    print(f"Predicted Eczema Level: {predicted_class}")
    print(f"Confidence Scores: {confidence_scores}")
    print("-" * 50)

