#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/validate_dataset.py
#
# PROGRAMMER: Shamim
# DATE CREATED: 2026-09-18
# PURPOSE: Preflight check for the pet_images/ folder. Confirms the full course
#          dataset is present and that every file is a genuine, decodable image
#          before the batch run is started. Catches placeholder/stub files that
#          would otherwise produce meaningless summary statistics.
#
# Usage:
#     python validate_dataset.py --dir pet_images/ --dogfile dognames.txt
##

import argparse
import os
import sys

from PIL import Image

EXPECTED_IMAGES = 40
EXPECTED_DOGS = 30
EXPECTED_NOTDOGS = 10
MIN_BYTES = 1024
MIN_PIXELS = 32


def pet_label(filename):
    """Derives the pet label from a filename the same way get_pet_labels does."""
    words = [w for w in filename.lower().split('_') if w.isalpha()]
    return " ".join(words)


def load_dognames(dogfile):
    with open(dogfile) as f:
        return {line.strip().lower() for line in f if line.strip()}


def main():
    parser = argparse.ArgumentParser(
        description="Validate the pet_images dataset before running the batch.")
    parser.add_argument('--dir', type=str, default='pet_images/')
    parser.add_argument('--dogfile', type=str, default='dognames.txt')
    args = parser.parse_args()

    problems = []

    if not os.path.isdir(args.dir):
        print("FAIL: image folder not found: {}".format(args.dir))
        return 1

    filenames = sorted(f for f in os.listdir(args.dir)
                       if not f.startswith('.')
                       and f.lower().endswith(('.jpg', '.jpeg', '.png')))

    if len(filenames) != EXPECTED_IMAGES:
        problems.append("expected {} images, found {}".format(
            EXPECTED_IMAGES, len(filenames)))

    dognames = load_dognames(args.dogfile)
    n_dogs = 0

    for filename in filenames:
        path = os.path.join(args.dir, filename)
        size = os.path.getsize(path)

        if size < MIN_BYTES:
            problems.append("{}: only {} bytes -- looks like a placeholder "
                            "stub, not a real photo".format(filename, size))
            continue

        try:
            with Image.open(path) as img:
                img.verify()
            with Image.open(path) as img:
                img.convert('RGB')
                width, height = img.size
        except Exception as err:
            problems.append("{}: cannot be decoded as an image ({})".format(
                filename, err))
            continue

        if width < MIN_PIXELS or height < MIN_PIXELS:
            problems.append("{}: {}x{} pixels -- too small to be a real "
                            "photo".format(filename, width, height))
            continue

        if pet_label(filename) in dognames:
            n_dogs += 1

    n_notdogs = len(filenames) - n_dogs
    if n_dogs != EXPECTED_DOGS or n_notdogs != EXPECTED_NOTDOGS:
        problems.append("expected {} dog / {} not-dog images, found {} / {}"
                        .format(EXPECTED_DOGS, EXPECTED_NOTDOGS,
                                n_dogs, n_notdogs))

    if problems:
        print("Dataset validation FAILED ({} problem(s)):\n".format(len(problems)))
        for problem in problems:
            print("  - {}".format(problem))
        print("\nRestore the original 40 pet images from the project workspace "
              "before running the batch.")
        return 1

    print("Dataset OK: {} images ({} dog / {} not-dog), all decodable."
          .format(len(filenames), n_dogs, n_notdogs))
    return 0


if __name__ == '__main__':
    sys.exit(main())
