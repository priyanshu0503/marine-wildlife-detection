import os
import random
import shutil

# Set paths
images_train_path = "images/train"
labels_train_path = "labels/train"

images_val_path = "images/val"
labels_val_path = "labels/val"

# Create val folders if not exist
os.makedirs(images_val_path, exist_ok=True)
os.makedirs(labels_val_path, exist_ok=True)

# Get all images
images = [f for f in os.listdir(images_train_path) if f.endswith(('.jpg', '.png'))]

# Shuffle
random.shuffle(images)

# 20% for validation
val_count = int(len(images) * 0.2)
val_images = images[:val_count]

for img in val_images:
    # Move image
    shutil.move(
        os.path.join(images_train_path, img),
        os.path.join(images_val_path, img)
    )

    # Move corresponding label
    label = img.rsplit('.', 1)[0] + ".txt"
    shutil.move(
        os.path.join(labels_train_path, label),
        os.path.join(labels_val_path, label)
    )

print("Split complete!")