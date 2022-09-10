"""
Module for extractor utilities
"""
import os
import fitz


def extract_images_from_pdf(pdf_file_path: str, dir_to_save: str = "images"):
    """
    Extract images from pdf and save it to images.
    """
    file = fitz.open(pdf_file_path)

    for page_index in range(file.page_count):
        image_list = file.get_page_images(page_index)

        if len(image_list) > 0:
            print(
                f"Found a total of {len(image_list)} images in page {page_index + 1}."
            )
        else:
            print(f"No images found on page {page_index + 1}.")

        print(f"Extracting images from page {page_index + 1}...")
        for img in image_list:
            xref = img[0]
            base_image = file.extract_image(xref)

            page_dir = os.path.join(dir_to_save, str(page_index + 1))

            try:
                os.mkdir(page_dir)
            except FileExistsError:
                print(
                    f"Directory '{page_dir}' exists. Proceed to extract images anyway..."
                )
            finally:
                img_file_path = os.path.join(
                    dir_to_save, str(page_index + 1), f"img_{xref}.{base_image['ext']}"
                )
                with open(img_file_path, "wb") as opened_file:
                    opened_file.write(base_image["image"])
        print(f"{len(image_list)} images from page {page_index + 1} extracted.")
