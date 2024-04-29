# https://idealo.github.io/imagededup/


from imagededup.methods import CNN
from imagededup.utils import plot_duplicates
import pandas as pd
import matplotlib.pyplot as plt
import os 


image_dir = "Images/"

from imagededup.methods import PHash
phasher = PHash()

# Generate encodings for all images in an image directory
encodings = phasher.encode_images(image_dir=image_dir)

# Find duplicates using the generated encodings
duplicates = phasher.find_duplicates(encoding_map=encodings)



cnn = CNN()



from imagededup.methods import CNN

cnn_encoder = CNN()

# Find duplicates using the generated encodings
duplicates_list = cnn_encoder.find_duplicates(image_dir=image_dir, min_similarity_threshold=0.95, scores=True,
        outfile='results.json')

print(duplicates_list)

# plot_duplicates(image_dir=image_dir,
#                 duplicate_map=duplicates_list,
#                 filename='test.jpg')

for duplicate_filename in duplicates_list_cnn:
    # Create the full file path
    file_path = os.path.join(image_dir, duplicate_filename)
    # Delete the file
    os.remove(file_path)
    print(f"Deleted: {file_path}")

