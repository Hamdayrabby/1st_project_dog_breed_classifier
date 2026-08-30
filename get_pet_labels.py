#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (relative or absolute) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Retrieve the filenames from folder image_dir
    filename_list = os.listdir(image_dir)

    # Processes through each file in the directory, extracting true pet labels
    for filename in filename_list:
        # Skip files that start with a dot (e.g. .DS_Store or hidden files)
        if filename.startswith('.'):
            continue

        # Convert filename to lowercase and split by underscore
        low_pet_image = filename.lower()
        word_list_pet_image = low_pet_image.split('_')

        # Create pet name string by extracting only alphabetic words
        pet_name = ""
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "

        # Strip leading/trailing whitespaces
        pet_name = pet_name.strip()

        # If filename is not in results_dic, add it; otherwise print warning
        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print(f"** Warning: Key={filename} already exists in results_dic with value={results_dic[filename]}")

    # Return results_dic
    return results_dic
