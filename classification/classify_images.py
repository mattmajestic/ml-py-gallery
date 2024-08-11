from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define a function to preprocess and extract text from an image
def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    
    # Apply sharpening filter
    image = image.filter(ImageFilter.SHARPEN)
    
    # Apply thresholding
    image = image.point(lambda p: p > 128 and 255)
    return image

# Define a function to extract text from a cropped image
def extract_pokemon_name(image_path):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Crop the image to the region where the Pokémon name is likely located
        width, height = image.size
        # Expanding the crop area to include more space around the name
        cropped_image = image.crop((int(width * 0.05), int(height * 0.02), int(width * 0.95), int(height * 0.25)))
        
        # Preprocess the image
        processed_image = preprocess_image(cropped_image)
        
        # Use Tesseract to do OCR on the image with specific configuration
        custom_config = r'--oem 3 --psm 7'  # PSM 7 is for single line text
        text = pytesseract.image_to_string(processed_image, config=custom_config)

        # Return the extracted text directly
        return text.strip()
    except Exception as e:
        return str(e)

# Paths to the images
image_paths = [
    "./output/card_one_1.jpg",
    "./output/card_one_2.jpg"
]

# Extract Pokémon names from the images
pokemon_names = [extract_pokemon_name(image_path) for image_path in image_paths]

# Print the extracted names
for i, name in enumerate(pokemon_names):
    print(f"Pokémon name from card {i + 1}:", name)
