import os
import argparse
import xml.etree.ElementTree as ET


def convert_pascal_voc_to_yolo(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if not file_name.endswith('.xml'):
            continue

        # Parse Pascal VOC XML file
        tree = ET.parse(os.path.join(input_dir, file_name))
        root = tree.getroot()

        # Extract image dimensions
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        yolo_annotations = []

        for obj in root.findall('object'):
            name = obj.find('name').text
            class_id = name_to_class_id(name)  # You need to implement this function based on your class names and ids
            bbox = obj.find('bndbox')
            xmin = float(bbox.find('xmin').text)
            ymin = float(bbox.find('ymin').text)
            xmax = float(bbox.find('xmax').text)
            ymax = float(bbox.find('ymax').text)

            # Convert to YOLO format
            x_center = (xmin + xmax) / 2 / width
            y_center = (ymin + ymax) / 2 / height
            bbox_width = (xmax - xmin) / width
            bbox_height = (ymax - ymin) / height

            yolo_annotations.append(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}")

        # Write YOLO annotation file
        output_file_name = os.path.splitext(file_name)[0] + '.txt'
        with open(os.path.join(output_dir, output_file_name), 'w') as output_file:
            output_file.write('\n'.join(yolo_annotations))


def name_to_class_id(name):
    # Map class name to class id
    class_map = {
        'class1': 0,
        'class2': 1,
        # Add other class mappings here
    }
    return class_map.get(name, -1)  # Returns -1 if class not found


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Pascal VOC annotations to YOLO format")
    parser.add_argument('input_dir', type=str, help='/Users/dhyaneshjadhav/dataset/labels')
    parser.add_argument('output_dir', type=str,
                        help='/Users/dhyaneshjadhav/Desktop/test')

    args = parser.parse_args()

    convert_pascal_voc_to_yolo(args.input_dir, args.output_dir)
