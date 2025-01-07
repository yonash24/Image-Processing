import numpy as np
import matplotlib as mp0
from PIL import Image

class ImageProcessor:
    
    #load an image and return it as numpy array
    def load_image(filepath):
        img = Image.open(filepath)
        img_array = np.array(img)/255.0 #normalize the pixel values
        return img_array
    
    #save the image
    def save_image(filepath,image_array):
        img = Image.fromarray((image_array * 255).astype(np.uint8))  # Rescale values to [0, 255]
        img.save(filepath)
    
    #convert RGB ro greyscale and return it as numpy array
    def convert_to_grayscale(image_array):
        img = Image.fromarray((image_array * 255).astype(np.uint8))  # Rescale values to [0, 255]
        img_greyscale = img.convert('L')
        greyscale_array = np.array(img_greyscale)
        return greyscale_array
    
    def apply_filter(image_array, kernel):
        pass
    
    def detect_edges(image_array):
        pass
    
    def adjust_brightness(image_array, factor):
        pass
    
    
    
