#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the true pet image labels. This function inputs:
#            -The Image Folder as image_dir
#            -The results dictionary as results_dic
#            -The CNN Model Architecture as model
#          This function uses the extend function to add items to the list 
#          that's the 'value' of the results dictionary. You will be adding the
#          classifier label as the item at index 1 of the list and the comparison 
#          of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports python modules
import os
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they match the pet image labels (all 
    lower case letters with leading and trailing whitespace characters removed).
    
    Parameters: 
     images_dir - The (relative or absolute) path to the folder of images that are to be
                  classified by the classifier function (string)
     results_dic - Dictionary with 'key' as image filename and 'value' as a 
                   List. The list contains for following item:
                     index 0 = pet image label (string)
                   --- at end of function will contain:
                     index 1 = classifier label (string)
                     index 2 = 1/0 (int)  where 1 = match between pet image
                     and classifer labels and 0 = no match between labels
     model - Indicates which CNN model architecture will be used by the 
             classifier function to classify the pet images,
             values must be either: resnet alexnet vgg (string)
     Returns:           
       None - results_dic is mutable data type so no return needed.         
    """
    for key in results_dic:
        # Construct the full image path
        image_path = os.path.join(images_dir, key)

        # Classify the image using the specified CNN model
        model_label = classifier(image_path, model)

        # Process classifier label: lower case and strip whitespace
        model_label = model_label.lower().strip()

        # Retrieve the ground truth pet label
        truth = results_dic[key][0]

        # Check if the pet label matches or is contained in the classifier label
        # (Handling possible multiple terms separated by commas in ImageNet classes)
        # Check standard Udacity rubric condition: truth in model_label
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])
