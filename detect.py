import torch
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\merno\\yolov5\\runs\\train\\exp4\\weights\\best.pt')

def detect_terminal_blocks(image_path):
    results = model(image_path)
    return results

image_path = 'C:\\Users\\merno\\Pictures\\output_folder\\page_0.png'
results = detect_terminal_blocks(image_path)
results.print()
results.save()

def extract_text_from_blocks(image_path, results):
    image = cv2.imread(image_path)
    blocks = []
    for result in results.xyxy[0].cpu().numpy():
        xmin, ymin, xmax, ymax, conf, cls = map(int, result)
        block_image = image[ymin:ymax, xmin:xmax]
        block_text = pytesseract.image_to_string(block_image)
        blocks.append((cls, block_text.strip()))
    return blocks

blocks = extract_text_from_blocks(image_path, results)
for cls, text in blocks:
    print(f'Block Class: {cls}, Text: {text}')