#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29                                  
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pre-trained CNN model. With this 
#          program we will be comparing the performance of 3 different ImageNet-trained
#          CNN model architectures (AlexNet, VGG, ResNet).
#
# Usage:
#     python check_images.py --dir <directory with images> --arch <model> --dogfile <file that contains dog names>
#
# Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Sets start time
    start_time = time()

    # Function that retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window
    in_arg = get_input_args()

    # Function that creates the results dictionary that contains the results, 
    # this dictionary is returned from the function call as the variable results
    results = get_pet_labels(in_arg.dir)

    # Function that classifies the images with the CNN model, creates the 
    # classifier labels and compares them to the true pet labels
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that adjusts the results dictionary to indicate if the pet image 
    # is of-a-dog and if the classifier label is of-a-dog
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that calculates the summary statistics of the classification results
    results_stats = calculates_results_stats(results)

    # Function that prints the summary results, and any incorrect classifications
    print_results(results, results_stats, in_arg.arch, True, True)

    # Sets end time
    end_time = time()

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    hours = int(tot_time // 3600)
    minutes = int((tot_time % 3600) // 60)
    seconds = int(tot_time % 60)
    print("\n** Total Elapsed Runtime: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))

# Call to main function to run the program
if __name__ == '__main__':
    main()
