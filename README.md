# Detection Models Project

This repository contains two detection models: a person detection model and a PPE (Personal Protective Equipmet) detection model. Additionally, it includes a script (`inference.py`) that takes both models as inputs and outputs the detection results. There is also a script that converts annotations from Pascal VOC format to YOLO format.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
  - [Person Detection Model](#person-detection-model)
  - [PPE Detection Model](#ppe-detection-model)
  - [Inference Script](#inference-script)
  - [Annotation Conversion Script](#annotation-conversion-script)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project aims to provide robust detection models for identifying persons and detecting personal protective equipment (PPE) in images. The `inference.py` script integrates both detection models to process input images and generate detection results. Additionally, the annotation conversion script facilitates the conversion of annotations from Pascal VOC format to YOLO format, aiding in training and evaluation.

## Installation

1. **Clone the repository:**

   ```sh
   git clone git@github.com:yourusername/your-repository-name.git
   cd your-repository-name
2. **Install dependencies:**

   pip install -r requirements.txt
   
3.**Running the Inference Script:**
  To run the inference.py script, use the following command:
   
