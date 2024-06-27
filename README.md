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
   ```sh
   pip install -r requirements.txt
   
3.**Running the Inference Script:**
  To run the inference.py script, use the following command:
  ```sh
  python inference.py --person_model path/to/person_model --ppe_model path/to/ppe_model --input path/to/input/image_or_directory --output path/to/output/directory
  ```
4.**Converting Annotations:**
  To convert annotations from Pascal VOC format to YOLO format, use the PascalVoc_to_yolov8.py script:
  ```sh
  python convert_annotations.py --input_dir path/to/pascal_annotations --output_dir path/to/yolo_annotations
  ```
## Components

  1.**Person Detection Model:**
    The person detection model is trained to identify and locate persons in images. The model can be loaded and used for inference through the inference.py script.
    
  2.**PPE Detection Model:**
    The PPE detection model is trained to detect various types of personal protective equipment, such as helmets, vests, and gloves. This model is also integrated into the           inference.py script for combined inference.

  3.**Inference Script:**
    The inference.py script takes both the person detection model and the PPE detection model as inputs, processes the specified images, and outputs the detection results. The         results can be saved in a specified output directory.

  4.**Annotation Conversion Script:**
    The convert_annotations.py script converts annotation files from Pascal VOC format to YOLO format. This is useful for preparing datasets for training models that require YOLO     format annotations.

## Contributing
  Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License
  This project is licensed under the MIT License. See the LICENSE file for details.

  ```sh
    This corrected version ensures that the "Install dependencies" section and everything following it is correctly included in the `README.md` file.
  ```








    
