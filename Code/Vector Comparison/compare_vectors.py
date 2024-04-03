from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from scipy.spatial.distance import cosine

# Function to load and preprocess the image
def load_and_preprocess_image(img_path):
    # Load image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Function to extract features
def extract_features(img_array, model):
    features = model.predict(img_array)
    features_flatten = features.flatten()
    return features_flatten

# Function to calculate cosine similarity
def calculate_similarity(vector1, vector2):
    return 1 - cosine(vector1, vector2)

# Load the ResNet50 model
model = ResNet50(weights='imagenet', include_top=False)

# Paths to the images
img_path1 = 'frame_48.jpg'
img_path2 = 'frame_46.jpg'
img_path3 = 'frame_44.jpg'

# Load and preprocess each image
img_array1 = load_and_preprocess_image(img_path1)
img_array2 = load_and_preprocess_image(img_path2)
img_array3 = load_and_preprocess_image(img_path3)

# Extract features for each image
features1 = extract_features(img_array1, model)
features2 = extract_features(img_array2, model)
features3 = extract_features(img_array3, model)

# Calculate similarities
similarity1 = calculate_similarity(features1, features2)
similarity2 = calculate_similarity(features1, features3)

# Determine which image is most similar to the first one
most_similar = "frame_46" if similarity1 > similarity2 else "frame_44"
print(f"The image most similar to 'frame_48.jpg' is: {most_similar}")
