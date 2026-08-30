# Dog Breed Classifier using Pre-trained CNN Models

An image classification program that uses pre-trained Convolutional Neural Network (CNN) architectures (**AlexNet**, **VGG**, and **ResNet**) in PyTorch to classify pet images and evaluate model accuracy on identifying dogs vs. non-dogs, as well as specific dog breeds.

---

## 📌 Project Overview

The objective of this project is to:
1. **Identify Pet Labels**: Extract ground-truth labels from pet image filenames.
2. **Classify Images**: Use pre-trained CNN models (AlexNet, VGG16, ResNet18) to predict image labels.
3. **Compare Results**: Evaluate whether predictions match true labels and verify if the image/prediction represents a dog using `dognames.txt`.
4. **Compute Statistics**: Generate comprehensive metrics (e.g., % correctly classified dogs, % correctly classified breeds, % correctly classified non-dogs).
5. **Compare Model Architectures**: Determine which CNN architecture performs best on runtime and classification accuracy.

---

## 📂 Project Structure

```text
├── check_images.py                   # Main application script
├── get_input_args.py                 # Handles CLI arguments
├── get_pet_labels.py                 # Extracts ground-truth labels from filenames
├── classify_images.py                # Performs classification using pre-trained CNNs
├── classifier.py                     # CNN model inference helper
├── adjust_results4_isadog.py         # Labels images and predictions as dog / not dog
├── calculates_results_stats.py       # Computes metrics and accuracy statistics
├── print_results.py                  # Formats and prints classification summaries
├── print_functions_for_lab_checks.py # Debugging / lab verification helpers
├── test_modules.py                   # Unit testing script
├── dognames.txt                      # Reference dataset of recognized dog names
├── pet_images/                       # Sample dataset of pet images
├── run_models_batch.bat              # Batch script for Windows
├── run_models_batch.sh               # Batch script for Linux/macOS
├── alexnet_pet-images.txt            # Results log for AlexNet
├── vgg_pet-images.txt                # Results log for VGG
└── resnet_pet-images.txt             # Results log for ResNet
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 and PyTorch installed:

```bash
pip install torch torchvision torchvision-models pillow
```

### Usage

Run the main classification script with custom arguments:

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

#### Command Line Arguments:
- `--dir`: Directory containing pet images (default: `pet_images/`)
- `--arch`: CNN model architecture to use: `alexnet`, `vgg`, or `resnet` (default: `vgg`)
- `--dogfile`: Text file containing recognized dog names (default: `dognames.txt`)

---

## 🧪 Running Batch Comparisons

### Windows:
```cmd
run_models_batch.bat
```

### Linux / macOS:
```bash
sh run_models_batch.sh
```

---

## 📊 Summary of Results

| Metric | AlexNet | VGG | ResNet |
| :--- | :---: | :---: | :---: |
| **% Correct Dogs** | 100% | 100% | 100% |
| **% Correct Breeds** | ~80% | ~93% | ~90% |
| **% Correct Non-Dogs** | 100% | 100% | 100% |

*VGG typically delivers the highest breed accuracy, while AlexNet offers the fastest execution time.*

---

## 👤 Author

- **Shamim (Hamday Rabby Hossain)**
