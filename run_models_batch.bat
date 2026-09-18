@echo off
REM Batch script to run check_images.py for all 3 CNN architectures on Windows
REM The dataset is validated first so an incomplete or placeholder pet_images/
REM folder stops the batch instead of producing meaningless summary files.

echo Validating pet_images dataset...
python validate_dataset.py --dir pet_images/ --dogfile dognames.txt
if errorlevel 1 (
    echo Dataset validation failed - batch aborted.
    exit /b 1
)

echo Running check_images.py with ResNet...
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt

echo Running check_images.py with AlexNet...
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt

echo Running check_images.py with VGG...
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt > vgg_pet-images.txt

echo All model runs completed! Check resnet_pet-images.txt, alexnet_pet-images.txt, and vgg_pet-images.txt for results.
