from pdf2image import convert_from_path
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

def pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, image in enumerate(images):
        image_path = f'{output_folder}/page_{i}.png'
        image.save(image_path, 'PNG')
        image_paths.append(image_path)
    return image_paths

pdf_path = "C:\\Users\\merno\\Documents\\PDF2IMAGE\\pdf_path\\teszt7.pdf"
output_folder = "C:\\Users\\merno\\Documents\\PDF2IMAGE\\output_folder"
image_paths = pdf_to_images(pdf_path, output_folder)