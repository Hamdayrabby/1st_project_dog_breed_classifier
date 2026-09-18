#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classifier.py
#
# PROGRAMMER: Shamim
# DATE CREATED: 2026-08-29
# REVISED DATE: 2026-09-18
# PURPOSE: Uses pre-trained PyTorch models (ResNet, AlexNet, VGG) to classify
#          images. Returns the ImageNet prediction label for an image.
#
#          NOTE: This module performs real CNN inference only. There is no
#          filename-based fallback -- if PyTorch, torchvision, or the ImageNet
#          class mapping is unavailable, the program fails loudly rather than
#          producing labels that were never predicted by a model.
#

import ast
import os

from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms

# Pretrained torchvision models keyed by the --arch values the project accepts
resnet18 = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
alexnet = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
vgg16 = models.vgg16(weights=models.VGG16_Weights.DEFAULT)

models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# ImageNet class index -> label mapping supplied with the course materials.
# This file matters: it carries the full comma-separated synonym lists
# (e.g. "German shepherd, German shepherd dog, ...") that the dognames.txt
# breed comparison relies on. torchvision's own short category names do not.
_CLS_IDX_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'imagenet1000_clsidx_to_labels.txt')

try:
    with open(_CLS_IDX_FILE) as f:
        imagenet_classes_dict = ast.literal_eval(f.read())
except FileNotFoundError:
    raise FileNotFoundError(
        "Missing ImageNet class mapping: {}\n"
        "Copy imagenet1000_clsidx_to_labels.txt from the project workspace "
        "into this directory before running the classifier.".format(_CLS_IDX_FILE)
    )

# Standard ImageNet preprocessing pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])


def classifier(img_path, model_name):
    """
    Classifies an image using a specified pretrained CNN architecture.

    Parameters:
      img_path   - Path to the image file (string)
      model_name - CNN architecture: 'resnet', 'alexnet', or 'vgg' (string)
    Returns:
      label      - ImageNet classification label predicted by the model (string)
    """
    arch = model_name.lower()
    if arch not in models_dict:
        raise ValueError(
            "Unknown architecture '{}'. Expected one of: {}".format(
                model_name, ", ".join(sorted(models_dict))))

    # Load the image; a corrupt or placeholder file raises here rather than
    # silently yielding a prediction.
    img = Image.open(img_path).convert('RGB')

    img_tensor = preprocess(img).unsqueeze(0)

    model = models_dict[arch]
    model.eval()

    with torch.no_grad():
        output = model(img_tensor)
        predicted_idx = int(output.argmax().item())

    return imagenet_classes_dict[predicted_idx]
