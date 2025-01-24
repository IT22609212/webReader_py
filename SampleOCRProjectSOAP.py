from zeep import Client
import re
import openpyxl

"""
    Sample project for OCRWebService.com (SOAP API).
    Extract text from scanned images and PDF documents and convert into editable formats.
    Please create a new account with ocrwebservice.com via http://www.ocrwebservice.com/account/signup and get a license code
"""

# Provide your username and license code
LOGIN = 'MHD9771'
LICENSE = '523AC8E6-EF4A-42E3-9092-746BE59C98BB'

# Service URL
client = Client('http://www.ocrwebservice.com/services/OCRWebService.asmx?WSDL')

# List of file paths to process
file_paths = [
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\astra.png",
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\\3.png",
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\4.png",
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\5.png",
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\6.png",
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\7.png",
    r"C:\Users\lolz\Downloads\SampleOCRWSProjectPython\data\8.png"
]


# OCR settings
ocrZones = {
    'OCRWSZone': [
        {'Top': 0, 'Left': 0, 'Height': 1200, 'Width': 600, 'ZoneType': 0},
        {'Top': 500, 'Left': 1000, 'Height': 1200, 'Width': 600, 'ZoneType': 0}
    ]
}

OCRSettings = {
    'ocrLanguages': 'ENGLISH',
    'outputDocumentFormat': 'DOC',
    'convertToBW': 'true',
    'getOCRText': 'true',
    'createOutputDocument': 'true',
    'multiPageDoc': 'true',
    'pageNumbers': 'allpages',
    'ocrZones': ocrZones,
    'ocrWords': 'false',
    'Reserved': ''
}

# Define a function to extract required fields from the OCR text
def extract_fields(ocr_text):
    exhibitor_name = re.search(r"(?:Exhibitor Name|Text):\s*(.*?)\s*(?:Hall|Pavilion|Country)", ocr_text, re.IGNORECASE)
    hall = re.search(r"Hall(?: Number)?\s*(\w+)", ocr_text, re.IGNORECASE)
    pavilion = re.search(r"Pavilion\s*(\w+)", ocr_text, re.IGNORECASE)
    country = re.search(r"Country\s*(\w+)", ocr_text, re.IGNORECASE)

    return {
        'Exhibitor Name': exhibitor_name.group(1) if exhibitor_name else "",
        'Hall': hall.group(1) if hall else "",
        'Pavilion': pavilion.group(1) if pavilion else "",
        'Country': country.group(1) if country else ""
    }

# Process each image
results = []
for file_path in file_paths:
    try:
        with open(file_path, 'rb') as image_file:
            image_data = image_file.read()

        InputImage = {
            'fileName': file_path.split('\\')[-1],
            'fileData': image_data,
        }

        # Perform OCR recognition
        result = client.service.OCRWebServiceRecognize(
            user_name=LOGIN, license_code=LICENSE, 
            OCRWSInputImage=InputImage, OCRWSSetting=OCRSettings
        )

        if result.errorMessage:
            print(f"Recognition Error for {file_path}: {result.errorMessage}")
        else:
            # Extracted text from all pages
            extracted_text = []
            for page in result.ocrText.ArrayOfString:
                extracted_text.extend(page.string)
            full_text = " ".join(filter(None, extracted_text))  # Ensure no None values in extracted_text
            fields = extract_fields(full_text)
            results.append(fields)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Export results to Excel
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Exhibitors"

# Write header
header = ["Exhibitor Name", "Hall", "Pavilion", "Country"]
sheet.append(header)

# Write data
for result in results:
    sheet.append([result[field] for field in header])

# Save Excel file
output_path = r"C:\Users\lolz\Downloads\Exhibitors.xlsx"
workbook.save(output_path)
print(f"Results exported to {output_path}")
