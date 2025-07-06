from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def print_large_char(char, size=56):
    """
    Renders a single character as large text in the terminal.

    Args:
        char (str): The single character to render.
        font_path (str): The file path to the .ttf or .otf font file.
        size (int): The desired font size in points, which affects output dimensions.
    """

    font_path = "fonts/NotoSerifCJKtc-Regular.otf"
    try:
        # Load the font. The size here is the pixel size for rendering.
        font = ImageFont.truetype(font_path, size)
    except IOError:
        print(f"'NotoSerifCJKtc-Regular' could not be found at '{font_path}'")
        return

    # Determine the bounding box of the character to create a tight image
    # The first two values of the bbox are often negative, so we use them to offset
    bbox = font.getbbox(char)
    image_width = bbox[2] - bbox[0]
    image_height = bbox[3] - bbox[1]

    # Create a blank image in 'L' (luminance/grayscale) mode
    img = Image.new("L", (image_width, image_height), color=0)  # Black background
    draw = ImageDraw.Draw(img)

    # Draw the character onto the image.
    # The offset (-bbox[0], -bbox[1]) ensures the character starts at the top-left.
    draw.text((-bbox[0], -bbox[1]), char, font=font, fill=255)  # White text

    # Build the output string by converting pixels to characters
    output = ""
    for y in range(image_height):
        for x in range(image_width):
            # If the pixel is brighter than a threshold, consider it part of the character
            if img.getpixel((x, y)) > 128:
                output += "██"  # Use two blocks for better aspect ratio
            else:
                output += "  "  # Two spaces
        output += "\n"
    print(output)
