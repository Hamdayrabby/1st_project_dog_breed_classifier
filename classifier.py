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

import ast
import os

from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms

# Dictionary to cache initialized models
models_dict = {}
models_cache = models_dict


def _load_model(arch):
    """Loads a pretrained CNN architecture, compatible with all torchvision versions."""
    if hasattr(models, 'ResNet18_Weights'):
        # torchvision >= 0.13
        if arch == 'resnet':
            return models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        elif arch == 'alexnet':
            return models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
        elif arch == 'vgg':
            return models.vgg16(weights=models.VGG16_Weights.DEFAULT)
    else:
        # torchvision < 0.13
        if arch == 'resnet':
            return models.resnet18(pretrained=True)
        elif arch == 'alexnet':
            return models.alexnet(pretrained=True)
        elif arch == 'vgg':
            return models.vgg16(pretrained=True)
    raise ValueError(f"Unknown architecture '{arch}'. Expected one of: alexnet, resnet, vgg")


# ImageNet class index -> label mapping supplied with the course materials.
# Supports both imagenet1000_clsid_to_human.txt (official workspace name)
# and imagenet1000_clsidx_to_labels.txt.
_DIR = os.path.dirname(os.path.abspath(__file__))
_CANDIDATE_FILES = [
    os.path.join(_DIR, 'imagenet1000_clsid_to_human.txt'),
    os.path.join(_DIR, 'imagenet1000_clsidx_to_labels.txt'),
    'imagenet1000_clsid_to_human.txt',
    'imagenet1000_clsidx_to_labels.txt'
]

imagenet_classes_dict = None
for _path in _CANDIDATE_FILES:
    if os.path.exists(_path):
        try:
            with open(_path) as f:
                imagenet_classes_dict = ast.literal_eval(f.read())
            break
        except Exception:
            continue

if imagenet_classes_dict is None:
    raise FileNotFoundError(
        "Missing ImageNet class mapping: imagenet1000_clsid_to_human.txt / imagenet1000_clsidx_to_labels.txt\n"
        "Copy imagenet1000_clsid_to_human.txt from the project workspace into this directory."
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
    valid_archs = {'resnet', 'alexnet', 'vgg'}
    if arch not in valid_archs:
        raise ValueError(
            "Unknown architecture '{}'. Expected one of: {}".format(
                model_name, ", ".join(sorted(valid_archs))))

    # Load and cache model on demand
    if arch not in models_dict:
        models_dict[arch] = _load_model(arch)

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
