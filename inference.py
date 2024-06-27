import argparse
import os
import cv2
from ultralytics import YOLO


def load_model(model_path):
    # Load the YOLOv8 model using the ultralytics package
    model = YOLO(model_path)
    return model


def run_inference(model, img):
    # Run inference on the image
    results = model(img)
    return results


def extract_boxes_and_labels(model, results):
    boxes = []
    labels = []
    confidences = []
    for result in results:
        for box, conf, cls in zip(result.boxes.xyxy.cpu().numpy(), result.boxes.conf.cpu().numpy(),
                                  result.boxes.cls.cpu().numpy()):
            boxes.append(box)
            confidences.append(conf)
            labels.append(model.names[int(cls)])
    return boxes, labels, confidences


def draw_boxes(img, boxes, labels, confidences):
    for box, label, confidence in zip(boxes, labels, confidences):
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


def main(input_dir, output_dir, person_model_path, ppe_model_path):
    os.makedirs(output_dir, exist_ok=True)

    # Load the models
    person_model = load_model(person_model_path)
    ppe_model = load_model(ppe_model_path)

    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        # Run person detection
        person_results = run_inference(person_model, img)
        person_boxes, person_labels, person_confidences = extract_boxes_and_labels(person_model, person_results)

        # Draw person detections
        draw_boxes(img, person_boxes, person_labels, person_confidences)

        for box in person_boxes:
            x1, y1, x2, y2 = map(int, box)
            person_crop = img[y1:y2, x1:x2]

            # Run PPE detection on person crop
            ppe_results = run_inference(ppe_model, person_crop)
            ppe_boxes, ppe_labels, ppe_confidences = extract_boxes_and_labels(ppe_model, ppe_results)

            # Adjust PPE box coordinates relative to the original image
            ppe_boxes = [[x1 + box[0], y1 + box[1], x1 + box[2], y1 + box[3]] for box in ppe_boxes]

            # Draw PPE detections
            draw_boxes(img, ppe_boxes, ppe_labels, ppe_confidences)

        # Save the output image
        output_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_path, img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inference script for person and PPE detection")
    parser.add_argument('input_dir', type=str,
                        help='Path to the input directory containing images')
    parser.add_argument('output_dir', type=str,
                        help='Path to the output directory to save results')
    parser.add_argument('person_det_model', type=str,
                        help='Path to the person detection model file')
    parser.add_argument('ppe_detection_model', type=str,
                        help='Path to the PPE detection model file')
    args = parser.parse_args()

    main(args.input_dir, args.output_dir, args.person_det_model, args.ppe_detection_model)
