from PIL import Image, ImageColor


def num_to_color(num):
    color_hex = "#" + f"{int(num):#010x}".removeprefix("0x")
    # print(color_hex)
    return ImageColor.getcolor(color_hex, "RGBA")


def make_images(filename):
    sections = open(filename).read().strip().split("\n\n")

    # make initial state image
    seeds = sections[0].removeprefix("seeds: ").strip().split(" ")
    print(seeds)
    im = Image.new("RGBA", (len(seeds), 1))
    for x, seed in enumerate(seeds):
        im.putpixel((x, 0), num_to_color(seed))
    im.save("seeds.png")

    # make mapping images
    for idx, section in enumerate(sections[1:]):
        map_name = section.split("\n")[0].replace(" map:", "")
        map_entries = section.split("\n")[1:]
        print(map_name, f"height={len(map_entries)}")
        im = Image.new("RGBA", (3, len(map_entries)))
        for y, entry in enumerate(map_entries):
            nums = [int(num) for num in entry.split(" ")]
            for x, num in enumerate(nums):
                im.putpixel((x, y), num_to_color(num))

        im.save(f"map_{idx+1}.png")


make_images("input")
# make_images("input_test")
