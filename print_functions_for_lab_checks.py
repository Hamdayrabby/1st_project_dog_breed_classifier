#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_functions_for_lab_checks.py
#
# PURPOSE: Helper functions to check and validate each step of the classification project.
#

def check_command_line_arguments(in_arg):
    """
    Checks print_results function's inputs and outputs.
    """
    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
    else:
        print("Command Line Arguments:\n     dir =", in_arg.dir, 
              "\n    arch =", in_arg.arch, "\n dogfile =", in_arg.dogfile)

def check_creating_pet_image_labels(results_dic):
    """
    Checks create_pet_image_labels function's outputs.
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
    else:
        # Code to print 10 key-value pairs
        stop_point = len(results_dic)
        if stop_point > 10:
            stop_point = 10
        print("\nPet Image Label Dictionary has", len(results_dic), "key-value pairs.\nBelow are", 
              stop_point, "of them:")
        
        # Counter to track how many items have been printed
        prt_ctr = 0
        for key in results_dic:
            if prt_ctr < stop_point:
                print("{:2d} key: {:>30}  label: {:>26}".format(prt_ctr+1, key, results_dic[key][0]))
                prt_ctr += 1
            else:
                break

def check_classifying_images(results_dic):
    """
    Checks classifying_images function's outputs.
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    elif len(results_dic[list(results_dic.keys())[0]]) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been run.")
    else:
        # Code to print 10 key-value pairs
        stop_point = len(results_dic)
        if stop_point > 10:
            stop_point = 10
        print("\nPet Image Label Dictionary has", len(results_dic), "key-value pairs.\nBelow are", 
              stop_point, "of them:")
        
        # Counter to track how many items have been printed
        prt_ctr = 0
        for key in results_dic:
            if prt_ctr < stop_point:
                print("{:2d} key: {:>30}  label: {:>26} \n       classifier: {:>30}  match: {:>2}".format(
                    prt_ctr+1, key, results_dic[key][0], results_dic[key][1], str(results_dic[key][2])))
                prt_ctr += 1
            else:
                break

def check_classifying_labels_as_dogs(results_dic):
    """
    Checks classifying_labels_as_dogs function's outputs.
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    elif len(results_dic[list(results_dic.keys())[0]]) < 4:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been run.")
    else:
        # Code to print 10 key-value pairs
        stop_point = len(results_dic)
        if stop_point > 10:
            stop_point = 10
        print("\nPet Image Label Dictionary has", len(results_dic), "key-value pairs.\nBelow are", 
              stop_point, "of them:")
        
        # Counter to track how many items have been printed
        prt_ctr = 0
        for key in results_dic:
            if prt_ctr < stop_point:
                print("{:2d} key: {:>30}  label: {:>26} \n       classifier: {:>30}  match: {:>2}  dog_image: {:>2}  dog_class: {:>2}".format(
                    prt_ctr+1, key, results_dic[key][0], results_dic[key][1], str(results_dic[key][2]),
                    str(results_dic[key][3]), str(results_dic[key][4])))
                prt_ctr += 1
            else:
                break

def check_calculating_results(results_dic, results_stats_dic):
    """
    Checks calculates_results_stats function's outputs.
    """
    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
    else:
        print("\n*** Results Statistics Dictionary ***")
        for key in results_stats_dic:
            print("{:20}: {}".format(key, results_stats_dic[key]))
