!pip install easyocr
import easyocr

# Initialize the EasyOCR reader with the model and language
reader = easyocr.Reader(['en'])

# Path to the input image
image_path = 'car_image.jpg'

# Read the number plate from the image
result = reader.readtext(image_path)

# Extract the detected text from the result
number_plate_text = result[0][1] if len(result) > 0 else "No number plate detected"

# Print the extracted text
print("Number Plate:", number_plate_text)
