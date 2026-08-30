#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification test suite for the dog image classification project modules.
"""

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
from print_functions_for_lab_checks import (
    check_command_line_arguments,
    check_creating_pet_image_labels,
    check_classifying_images,
    check_classifying_labels_as_dogs,
    check_calculating_results
)

def run_tests():
    print("========================================")
    print("STEP 1: Testing get_input_args")
    print("========================================")
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)
    assert in_arg.dir == 'pet_images/', f"Expected pet_images/, got {in_arg.dir}"
    assert in_arg.arch == 'vgg', f"Expected vgg, got {in_arg.arch}"
    assert in_arg.dogfile == 'dognames.txt', f"Expected dognames.txt, got {in_arg.dogfile}"
    print("PASS: get_input_args works correctly!")

    print("\n========================================")
    print("STEP 2: Testing get_pet_labels")
    print("========================================")
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)
    assert len(results) > 0, "results_dic should not be empty"
    assert 'Boston_terrier_02259.jpg' in results, "Boston_terrier_02259.jpg missing"
    assert results['Boston_terrier_02259.jpg'][0] == 'boston terrier', f"Expected 'boston terrier', got {results['Boston_terrier_02259.jpg'][0]}"
    assert results['cat_01.jpg'][0] == 'cat', f"Expected 'cat', got {results['cat_01.jpg'][0]}"
    print("PASS: get_pet_labels works correctly!")

    print("\n========================================")
    print("STEP 3: Testing classify_images")
    print("========================================")
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)
    for key, val in results.items():
        assert len(val) == 3, f"Expected 3 elements for key {key}, got {len(val)}"
        assert isinstance(val[1], str), f"Classifier label should be str, got {type(val[1])}"
        assert val[2] in (0, 1), f"Match index should be 0 or 1, got {val[2]}"
    print("PASS: classify_images works correctly!")

    print("\n========================================")
    print("STEP 4: Testing adjust_results4_isadog")
    print("========================================")
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)
    for key, val in results.items():
        assert len(val) == 5, f"Expected 5 elements for key {key}, got {len(val)}"
        assert val[3] in (0, 1), f"pet is-a-dog should be 0 or 1, got {val[3]}"
        assert val[4] in (0, 1), f"classifier is-a-dog should be 0 or 1, got {val[4]}"
    # Verify Boston terrier is a dog (1) and cat is not a dog (0)
    assert results['Boston_terrier_02259.jpg'][3] == 1, "Boston terrier should be dog (1)"
    assert results['cat_01.jpg'][3] == 0, "Cat should NOT be dog (0)"
    print("PASS: adjust_results4_isadog works correctly!")

    print("\n========================================")
    print("STEP 5: Testing calculates_results_stats")
    print("========================================")
    stats = calculates_results_stats(results)
    check_calculating_results(results, stats)
    required_keys = [
        'n_images', 'n_dogs_img', 'n_notdogs_img', 'n_match',
        'n_correct_dogs', 'n_correct_notdogs', 'n_correct_breed',
        'pct_match', 'pct_correct_dogs', 'pct_correct_breed', 'pct_correct_notdogs'
    ]
    for rk in required_keys:
        assert rk in stats, f"Missing key in results_stats_dic: {rk}"
    assert stats['n_images'] == len(results), "Total image count mismatch"
    assert stats['n_dogs_img'] + stats['n_notdogs_img'] == stats['n_images'], "Dog + Not-dog count mismatch"
    print("PASS: calculates_results_stats works correctly!")

    print("\n========================================")
    print("STEP 6: Testing print_results")
    print("========================================")
    print_results(results, stats, in_arg.arch, True, True)
    print("\nPASS: print_results works correctly!")

    print("\n========================================")
    print("ALL MODULE CHECKS PASSED SUCCESSFULLY!")
    print("========================================")

if __name__ == '__main__':
    run_tests()
