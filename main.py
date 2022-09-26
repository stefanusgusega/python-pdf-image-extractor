"""
Main program
"""
import argparse
from src.extractor import extract_images_from_pdf

parser = argparse.ArgumentParser()
parser.add_argument("--pdffile")
parser.add_argument("--imgdir")
parser.add_argument("--pages", default=None)
args = parser.parse_args()

# Decrement all elements by 1, so it is aligned with
# Python indexing
pages = (
    list(map(lambda x: int(x) - 1, args.pages.split(",")))
    if args.pages is not None
    else None
)

extract_images_from_pdf(args.pdffile, args.imgdir, pages=pages)
