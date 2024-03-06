import cv2
import numpy as np
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
import pytesseract
import re

def convert_pdf(file_path):
    return convert_from_path(file_path, fmt='jpg')[0]

def extract_order_number(thresh):
    # extract purpose of remittance data within particular range
    cropped_image = thresh[480:650, 1620:2640]
    extracted_text = pytesseract.image_to_string(cropped_image, config='--oem 3 --psm 4')
    print(extracted_text)

def extract_sender_data(thresh):
    # extract sender's data within particular range
    cropped_image = thresh[820:1070, 160:1720]
    extracted_text = pytesseract.image_to_string(cropped_image)
    print(extracted_text)

def extract_receiver_data(thresh):
    # extract receiver's data within particular range
    cropped_image = thresh[1630:1900, 160:1720]
    extracted_text = pytesseract.image_to_string(cropped_image)
    print(extracted_text)

def extract_purpose_of_remittance_data(thresh):
    # extract purpose of remittance data within particular range
    cropped_image = thresh[1240:1470, 160:1720]
    extracted_text = pytesseract.image_to_string(cropped_image)
    print(extracted_text)

def extract_sender_bank_account(thresh):
    # extract purpose of remittance data within particular range
    cropped_image = thresh[750:830, 2360:3040]
    extracted_text = pytesseract.image_to_string(cropped_image)
    print(extracted_text)

def extract_receiver_bank_account(thresh):
    # extract purpose of remittance data within particular range
    cropped_image = thresh[910:990, 2360:3040]
    extracted_text = pytesseract.image_to_string(cropped_image)
    print(extracted_text)

def extract_amount(thresh):
    # extract purpose of remittance data within particular range
    cropped_image = thresh[1180:1270, 2350:3100]
    extracted_text = pytesseract.image_to_string(cropped_image, config='--oem 3 --psm 4')
    amountRegex = r'\b\d{2}\,\d{2}\b'    
    print(re.findall(amountRegex, extracted_text)[0])

def extract_payment_date(thresh):
    # extract purpose of remittance data within particular range
    cropped_image = thresh[2120:2200, 620:940]
    extracted_text = pytesseract.image_to_string(cropped_image, config='--oem 3 --psm 4')
    print(extracted_text)

file_path = 'C:/Users/PcCentar/Desktop/repos/bank_statements_ocr/bank_statements/report.pdf'
image = convert_pdf(file_path)
image = np.array(image)

# PREPROCESSING

# Resize the image to improve OCR accuracy and speed
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve accuracy
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
plt.imshow(image)
plt.show()

extractedText = pytesseract.image_to_string(thresh, config='--oem 3 --psm 4')
orderNumber = extract_order_number(thresh)
#paymentDate = extract_payment_date(extractedText)
extract_sender_data(thresh)
extract_receiver_data(thresh)
extract_purpose_of_remittance_data(thresh)
extract_sender_bank_account(thresh)
extract_receiver_bank_account(thresh)
extract_amount(thresh)
extract_payment_date(thresh)

def extract_order_number_(text):
    orderNumberRegex = r'\bDPY\d{15}\b'
    
    return re.findall(orderNumberRegex, text)

def extract_amount_(text):
    amountRegex = r'\b\d{2}\,\d{2}\b'
    
    return re.findall(amountRegex, text)

def extract_payment_date_(text):
    dateRegex = r'\b\d{2}\/\d{2}\/\d{4}\b'

    return re.findall(dateRegex, text)