#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (string) and the 'value' is one. If a label is found to exist
#          within this dictionary of dog names, then the label is of-a-dog, otherwise
#          the label is not of-a-dog.
#
##
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model can correctly classify images as a dog even if it 
    cannot correctly classify the dog's breed.
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int)  where 1 = match between pet image
                                and classifier labels and 0 = no match between labels
                    --- at end of function will contain:
                      index 3 = 1/0 (int)  where 1 = pet image 'is-a-dog' and 
                                0 = pet image 'is-NOT-a-dog' 
                      index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                                'as-a-dog' and 0 = Classifier classifies image  
                                'as-NOT-a-dog'
     dogfile - A text file that contains names of all dogs from the ImageNet 
               dataset (one dog name per line).
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Creates dognames dictionary for quick lookup
    dognames_dic = dict()

    # Read in dog names from file
    with open(dogfile, "r") as infile:
        for line in infile:
            # Strip trailing newline/whitespace and convert to lowercase
            dog_name = line.strip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                pass

    # Adjust results dictionary by checking if pet label and classifier label are in dognames_dic
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Determine if pet image is a dog
        if pet_label in dognames_dic:
            pet_is_dog = 1
        else:
            pet_is_dog = 0

        # Determine if classifier label is a dog. ImageNet labels are
        # comma-separated synonym lists (e.g. "german shepherd, german shepherd
        # dog, alsatian") whereas dognames.txt stores one synonym per line, so
        # the label is split and each term is checked individually. A plain
        # lookup of the whole label string would never match a multi-synonym
        # class and would wrongly report those dogs as not-a-dog.
        classifier_is_dog = 0
        for term in classifier_label.split(','):
            if term.strip() in dognames_dic:
                classifier_is_dog = 1
                break

        # Append results
        results_dic[key].extend([pet_is_dog, classifier_is_dog])
