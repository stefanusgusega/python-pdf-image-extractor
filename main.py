"""
Main program
"""
import argparse
from src.extractor import extract_images_from_pdf

parser = argparse.ArgumentParser()
parser.add_argument("--pdffile")
parser.add_argument("--imgdir")
args = parser.parse_args()

extract_images_from_pdf(args.pdffile, args.imgdir)
