#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic
#            -The results statistics dictionary as results_stats_dic
#            -The CNN Model Architecture as model
#            -The boolean for printing misclassified dogs as print_incorrect_dogs
#            -The boolean for printing misclassified dog breeds as print_incorrect_breed
#         This function prints:
#            -The Model Architecture used
#            -Total number of images, dog images, and not-a-dog images
#            -All percentage statistics calculated by calculates_results_stats
#            -Optional: Cases where dog/not-dog was misclassified
#            -Optional: Cases where dog breed was misclassified
#
##
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index 0 = pet image label (string)
              index 1 = classifier label (string)
              index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
              index 3 = 1/0 (int)  where 1 = pet image 'is-a-dog' and 
                    0 = pet image 'is-NOT-a-dog' 
              index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                    'as-a-dog' and 0 = Classifier classifies image  
                    'as-NOT-a-dog')
      results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print (default: False)
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print (default: False)
    Returns:
           None - simply printing to console
    """
    # Prints summary header with model architecture
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:5d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:5d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:5d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Prints percentage statistics from results_stats_dic
    print("\n*** Percentage Statistics ***")
    for key in results_stats_dic:
        if key.startswith('pct'):
            print("{:20}: {:5.1f}%".format(key, results_stats_dic[key]))

    # IF print_incorrect_dogs == True AND there were misclassifications of dogs/not-dogs
    if print_incorrect_dogs and (
        (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
        != results_stats_dic['n_images']
    ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            # Pet image is a dog and classifier says not a dog, OR vice versa
            if sum(results_dic[key][3:]) == 1:
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))

    # IF print_incorrect_breed == True AND there were misclassifications of dog breeds
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            # Both pet image and classifier agree it's a dog, but breed does not match
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))
