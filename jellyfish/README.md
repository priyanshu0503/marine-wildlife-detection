# Jellyfish Identification and Counting using YOLO11
**Department of Applied Computer Science | University of Winnipeg**

**Researcher:** Priyanshu Mittal
**Student ID:** 3165633
**Date:** March 2026

---

## 1. Project Overview
The objective of this research is to automate the monitoring of marine ecosystems by identifying and counting specific species of jellyfish. Using the **YOLO11** (You Only Look Once) object detection framework, this project provides a high-speed, accurate method for quantifying jellyfish populations from underwater imagery.

### Target Species:
The model is trained to distinguish between five distinct classes:
1. **Arctic Comb**
2. **Common Northern Comb**
3. **Lion's Mane**
4. **Melon Comb**
5. **Moon Jelly**

---

## 2. Technical Implementation

### Architecture
This project utilizes **YOLO11n**, the latest iteration in the YOLO series. It was selected for its improved feature extraction and balance between inference speed and detection precision, which is critical for identifying translucent marine organisms.

### Development Environment
* **Language:** Python 3.11
* **Framework:** Ultralytics YOLO11
* **Hardware:** Intel Core i7-8700 CPU

---

## 3. How to Run the System

### Installation
Ensure the necessary libraries are installed:
`pip install ultralytics opencv-python`

### Training the Model
To reproduce the research results or further fine-tune the model, run:
`python train_yolo11.py`

### Running Identification & Counting
To process a folder of images and generate a species count report, run:
`python counting_system.py`

---

## 4. Research Results
The model was evaluated against a YOLOv8 baseline to measure performance gains in marine environments.

* **Counting Capability:** The system successfully extracts bounding box counts per image, categorized by species, and outputs them via the terminal or saved report files.

---

## 5. Project Structure
* `images/`: Training and validation datasets.
* `jellyfish.yaml`: Dataset configuration file defining class names and local paths.
* `train_yolo11.py`: Script used for model training.
* `counting_system.py`: Primary script for identifying and counting jellyfish in new data.
* `runs/`: Folder containing performance charts (`results.png`), confusion matrices, and the final model weights (`best.pt`).

---

## 6. Future Research
* **Real-time Video Analysis:** Adapting the counter for live underwater drone feeds.
* **Biomass Estimation:** Using bounding box dimensions to estimate the age and weight of jellyfish swarms.
* **Environmental Robustness:** Implementing data augmentation for water turbidity and variable lighting.
