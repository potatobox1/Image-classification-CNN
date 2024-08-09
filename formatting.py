import os
import shutil
from sklearn.model_selection import train_test_split

original_dataset_dir = r'C:\Users\GNG\Desktop\AI coursepack\Pet_Breeds'
base_dir = r'C:\Users\GNG\Desktop\some'

train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

# Create train and test directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Split ratio
split_ratio = 0.8

# Loop over each breed folder
for breed in os.listdir(original_dataset_dir):
    breed_folder = os.path.join(original_dataset_dir, breed)
    
    if os.path.isdir(breed_folder):
        # Create breed folders in train and test directories
        os.makedirs(os.path.join(train_dir, breed), exist_ok=True)
        os.makedirs(os.path.join(test_dir, breed), exist_ok=True)
        
        # Get all images in the current breed folder
        images = [f for f in os.listdir(breed_folder) if f.endswith('.jpg')]
        
        print(f'Processing breed: {breed}, Total images: {len(images)}')

        # Check if there are enough images to split
        if len(images) > 1:
            # Split images into train and test sets
            train_images, test_images = train_test_split(images, train_size=split_ratio)
            print(f'Breed: {breed}, Train images: {len(train_images)}, Test images: {len(test_images)}')
        else:
            print(f'Breed: {breed} has not enough images to split.')
            train_images = images
            test_images = []

        # Copy images to the respective folders
        for img in train_images:
            src = os.path.join(breed_folder, img)
            dst = os.path.join(train_dir, breed, img)
            shutil.copyfile(src, dst)
        
        for img in test_images:
            src = os.path.join(breed_folder, img)
            dst = os.path.join(test_dir, breed, img)
            shutil.copyfile(src, dst)

print("Dataset restructuring completed.")
