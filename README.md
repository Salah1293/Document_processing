# **Document Processing**

*Document Processing* is a Django-based web application designed to efficiently manage and manipulate document files, including images and PDFs. This application provides tools to upload, rotate, convert PDFs to images, and manage uploaded documents.

## **Features**

- **File Upload**: 
  - Easily upload image files (JPEG, PNG, etc.) and PDFs.
  - Automatically validate file types and ensure that only supported formats are processed.

- **Image Processing**:
  - Rotate images by any angle to adjust orientation.
  - Modify image filenames to prevent excessive length and maintain consistency.

- **PDF to Image Conversion**: 
  - Convert PDFs into images, one image per page, using high-quality rendering.
  - Automatically create directories and save images in an organized structure for each PDF.

- **Document Management**:
  - View and retrieve specific image and PDF documents by their unique ID.
  - List all uploaded images and PDFs for easy browsing.

- **File Deletion**:
  - Delete unwanted image and PDF files from the system to free up storage and maintain organization.

## **Technologies Used**

- **Backend**: Django, Python
- **File Handling**: 
  - Media file management via Django’s `MEDIA_ROOT` for file storage.
  - Image processing using the Python Imaging Library (PIL/Pillow).
  - PDF rendering and conversion to images using `pdf2image` and Poppler.

## **How It Works**

- **Image Upload & Rotation**: Upload images and specify angles for rotation. The system processes the images and stores them in the designated folder, ensuring the filenames are correctly updated to prevent conflicts.

- **PDF Conversion**: Uploaded PDFs are converted into individual image files for each page, making it easier to work with the content of the PDFs in image form. These images are saved in organized folders based on the original PDF file.

- **File Deletion**: Both images and PDFs can be deleted from the system as needed, which is useful for cleaning up old files or removing incorrect uploads.


## **Requirements**
Python 3.x
Django
djangorestframework
Pillow
PyPDF2 (for handling PDFs)
poppler-utils (for converting PDFs to images)