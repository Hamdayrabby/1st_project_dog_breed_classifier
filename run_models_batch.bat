@echo off
REM Batch script to run check_images.py for all 3 CNN architectures on Windows
echo Running check_images.py with ResNet...
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt

echo Running check_images.py with AlexNet...
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt

echo Running check_images.py with VGG...
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt > vgg_pet-images.txt

echo All model runs completed! Check resnet_pet-images.txt, alexnet_pet-images.txt, and vgg_pet-images.txt for results.
