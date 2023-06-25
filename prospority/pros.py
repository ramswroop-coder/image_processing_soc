from PIL import Image

def calculate_porosity(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Get the pixel data
    pixel_data = grayscale_image.load()

    # Initialize counters
    total_pixels = 0
    pore_pixels = 0

    # Iterate over each pixel in the image
    width, height = grayscale_image.size
    for y in range(height):
        for x in range(width):
            # Check if the pixel is dark (representing a pore)
            if pixel_data[x, y] < 60:
                pore_pixels += 1
            total_pixels += 1

    # Calculate the percentage porosity
    porosity = (pore_pixels / total_pixels) * 100

    return porosity

# Provide the path to your image file
image_path = 'pros.jpg'

# Call the function to calculate porosity
porosity_percentage = calculate_porosity(image_path)

# Print the porosity percentage
print('Porosity: {:.2f}%'.format(porosity_percentage))
