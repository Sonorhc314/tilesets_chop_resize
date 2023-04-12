import os
from PIL import Image

# Define the path to the folder containing the images
# folder_path = "../../../Desktop/player/NinjaAdventure/Backgrounds/Vehicles"
folder_path = "../witchling/graphics/map"
# ==================================================================
# uses resample=Image.NEAREST to keep the resolution of pixel art
# ===================================================================


# chop an image into n 16x16(resize_from parameter) images and then scale them to 64x64(resize_to parameter)
def chop_and_resize(folder_path, resize_to, resize_from):
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image file
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Get the size of the image
            width, height = image.size

            # Calculate the number of 16x16 tiles that can fit in the image
            num_tiles_x = width // resize_from
            num_tiles_y = height // resize_from

            # Iterate over each tile and save it as a separate image
            for i in range(num_tiles_x):
                for j in range(num_tiles_y):
                    # Calculate the coordinates of the current tile
                    x0 = i * resize_from
                    y0 = j * resize_from
                    x1 = x0 + resize_from
                    y1 = y0 + resize_from

                    # Crop the tile from the image
                    tile = image.crop((x0, y0, x1, y1))

                    tile = tile.resize((resize_to, resize_to), resample=Image.NEAREST)

                    # Save the tile as a separate image
                    tile_filename = f"{filename}_{i}_{j}.png"
                    tile_path = os.path.join(folder_path, tile_filename)
                    tile.save(tile_path)


# scale image by parameter scale_by
def resize(folder_path, scale_by):
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image file
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            width, height = image.size
            image = image.resize(
                (width * scale_by, height * scale_by), resample=Image.NEAREST
            )

            # Save the tile as a separate image
            image_filename = f"{filename[0:-4]}_{scale_by}.png"
            image_path = os.path.join(folder_path, image_filename)
            image.save(image_path)
