import os

def create_file_list(image_dir, output_file, relative_path_prefix):
    with open(output_file, 'w') as f:
        for image_name in os.listdir(image_dir):
            image_path = os.path.join(relative_path_prefix, image_name).replace('\\', '/')
            f.write(f"{image_path}\n")

train_image_dir = 'D:/Projects/Coding/deepvision/datasets/coco/train2017'
val_image_dir = 'D:/Projects/Coding/deepvision/datasets/coco/val2017'
train_output_file = 'D:/Projects/Coding/deepvision/datasets/coco/train2017.txt'
val_output_file = 'D:/Projects/Coding/deepvision/datasets/coco/val2017.txt'

create_file_list(train_image_dir, train_output_file, 'images/train2017')
create_file_list(val_image_dir, val_output_file, 'images/val2017')

print("File lists created.")