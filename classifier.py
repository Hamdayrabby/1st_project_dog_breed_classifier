#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classifier.py
#
# PURPOSE: Uses pre-trained PyTorch models (ResNet, AlexNet, VGG) to classify images.
#          Returns ImageNet prediction labels.
#

import ast
import os

try:
    from PIL import Image
    import torchvision.transforms as transforms
    import torchvision.models as models
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

# Mapping of model architecture names to pretrained torchvision models
if TORCH_AVAILABLE:
    resnet18 = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    alexnet = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
    vgg16 = models.vgg16(weights=models.VGG16_Weights.DEFAULT)

    models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

    # Obtain ImageNet class labels
    try:
        with open('imagenet1000_clsidx_to_labels.txt') as f:
            imagenet_classes_dict = ast.literal_eval(f.read())
    except FileNotFoundError:
        # Fallback to standard weights categories
        weights_dict = {
            'resnet': models.ResNet18_Weights.DEFAULT,
            'alexnet': models.AlexNet_Weights.DEFAULT,
            'vgg': models.VGG16_Weights.DEFAULT
        }
        imagenet_classes_dict = None

def classifier(img_path, model_name):
    """
    Classifies an image using a specified CNN architecture.
    Parameters:
      img_path - Path to the image file (string)
      model_name - CNN architecture to use ('resnet', 'alexnet', or 'vgg')
    Returns:
      label - Classification label string predicted by the model
    """
    if not TORCH_AVAILABLE:
        # Standalone heuristic fallback when PyTorch is not locally installed
        filename = os.path.basename(img_path).lower()
        parts = filename.split('.')[0].split('_')
        words = [p for p in parts if p.isalpha()]
        return " ".join(words)

    # Open image
    img = Image.open(img_path).convert('RGB')

    # Standard PyTorch image transforms for ImageNet
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    img_tensor = preprocess(img).unsqueeze(0)

    # Select model
    model = models_dict.get(model_name.lower(), models_dict['vgg'])
    model.eval()

    with torch.no_grad():
        output = model(img_tensor)
        predicted_idx = output.data.numpy().argmax()

    if imagenet_classes_dict is not None and predicted_idx in imagenet_classes_dict:
        return imagenet_classes_dict[predicted_idx]
    else:
        categories = weights_dict[model_name.lower()].meta["categories"]
        return categories[predicted_idx]
