#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch.sh
#
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29
# REVISED DATE: 2026-09-18
# PURPOSE: Runs all three models to test which provides the 'best' solution.
#          Output from each run is piped into a text file.
#
#          The dataset is validated first: if pet_images/ is incomplete or
#          contains files that are not real, decodable photos, the batch stops
#          rather than writing summary files that do not reflect a real run.
#
# Usage: sh run_models_batch.sh    -- runs from the commandline on Windows & Mac/Unix
#
python validate_dataset.py --dir pet_images/ --dogfile dognames.txt || exit 1

python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg     --dogfile dognames.txt > vgg_pet-images.txt
