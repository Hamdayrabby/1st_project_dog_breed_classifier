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
├── pet_images/                       # The 40 course pet images (not committed)
├── validate_dataset.py               # Preflight check on the pet_images dataset
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
pip install torch torchvision pillow
```

You also need two things that ship with the Udacity project workspace and are
**not** committed to this repository:

- `pet_images/` — the 40 course pet images (30 dog, 10 not-a-dog). Copy the
  originals; placeholder or substitute images make the results ungradeable.
- `imagenet1000_clsidx_to_labels.txt` — the ImageNet class-index mapping. This
  file carries the full comma-separated synonym lists (e.g.
  `German shepherd, German shepherd dog, ...`) that breed matching against
  `dognames.txt` depends on. torchvision's own short category names are not a
  substitute.

Before running the batch, confirm the dataset is intact:

```bash
python validate_dataset.py --dir pet_images/ --dogfile dognames.txt
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

The table below records the measured benchmark figures from the batch run on the 40-image course set.

| Metric | AlexNet | VGG | ResNet |
| :--- | :---: | :---: | :---: |
| **N Images** | 40 | 40 | 40 |
| **N Dog Images** | 30 | 30 | 30 |
| **N Not-Dog Images** | 10 | 10 | 10 |
| **% Match** | 75.0% | 87.5% | 82.5% |
| **% Correct Dogs** | 100.0% | 100.0% | 100.0% |
| **% Correct Breeds** | 80.0% | 93.3% | 90.0% |
| **% Correct Non-Dogs** | 90.0% | 100.0% | 90.0% |
| **Elapsed Runtime** | 00:00:03 | 00:00:14 | 00:00:04 |

*Findings:*
- **Highest Breed Accuracy**: **VGG** achieved the highest breed classification accuracy at **93.3%** and correctly identified 100% of non-dogs and dogs.
- **Fastest Model**: **AlexNet** achieved the fastest inference runtime at **00:00:03**, but had lower breed accuracy (80.0%).
- **Balanced Performance**: **ResNet** provided a great balance of fast runtime (00:00:04) and high breed accuracy (90.0%).

---

## 👤 Author

- **Shamim (Hamday Rabby Hossain)**
