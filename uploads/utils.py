from PyPDF2 import PdfReader
import os


#function to return number of pdf file pages
def get_pdf_page(pdf_file):
    reader = PdfReader(pdf_file)
    return len(reader.pages)


#function to rename an item with a name longer than 100 characters
def update_filename(filename):

    original_name, extension = os.path.splitext(filename)

    if len(original_name) > 100:
        updated_original_name_char_number = 100 - len(extension)
        new_name = f"{original_name[:updated_original_name_char_number]}{extension}"

    else:
        new_name = f"{original_name}{extension}"

    return new_name