import random

TOTAL_IMAGES = 11000

all_images = []


def create_new_image():
    new_image = {}

    new_image["Background"] = random.choices(range(1, 26))[0]
    new_image["Body"] = random.choices(range(1, 9))[0]
    new_image["Left Strand"] = random.choices(range(1, 4))[0]
    new_image["Face"] = random.choices(range(1, 7))[0]
    new_image["Right Strand"] = random.choices(range(1, 4))[0]
    new_image["Left Eye"] = random.choices(range(1, 14))[0]
    new_image["Nose"] = random.choices(range(1, 8))[0]
    new_image["Right Eye"] = random.choices(range(1, 8))[0]
    new_image["Print"] = random.choices(range(1, 14))[0]
    new_image["Lips"] = random.choices(range(1, 21))[0]
    new_image["Flowers"] = random.choices(range(0, 24))[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


def create_new_rare_image():
    new_image = {}

    new_image["Background"] = random.choices(range(1, 26))[0]
    new_image["Hair"] = random.choices(range(1, 7))[0]
    new_image["Body"] = random.choices(range(1, 9))[0]
    new_image["Face"] = random.choices(range(1, 8))[0]
    new_image["Nose"] = random.choices(range(9, 12))[0]
    new_image["Left Eye"] = random.choices(range(1, 14))[0]
    new_image["Right Eye"] = random.choices(range(1, 8))[0]
    new_image["Print"] = random.choices(range(1, 13))[0]
    new_image["Lips"] = random.choices(range(1, 27))[0]
    new_image["Flowers"] = random.choices(range(1, 18))[0]

    if new_image in all_images:
        return create_new_rare_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    create_image_func, path = random.choices(
        [(create_new_image, "01"), (create_new_rare_image, "02")], [80, 20]
    )[0]
    new_trait_image = create_image_func()
    new_trait_image["path"] = path

    all_images.append(new_trait_image)
