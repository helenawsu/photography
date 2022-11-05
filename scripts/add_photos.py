from pathlib import Path
import glob
import shutil
import os
photos_folder = Path(__file__).parent / "../public/photos"
archive_path = Path(__file__).parent / "../src/create_img.js"

more = True

while more:
    jpgfile = input('What is the image?\n').strip("'")
    if jpgfile == "exit":
        break
    dst_dir = photos_folder

    file_path = shutil.copy(jpgfile, dst_dir)
    print(file_path)
    file_relative_path = os.path.relpath(file_path, "/Users/helena/svelte/svelte-photography/public")
    print(file_relative_path)

    print("original image added")

    convert_command = "convert " + file_path+ " -resize 1000x1000 " + file_path[:-3] + "webp"
    os.system(convert_command)
    print("image is compressed")


    with open(archive_path, 'r') as photo_archive:
        original = photo_archive.readlines()
        for index,line in enumerate(original):
            if '  //add here\n' in line :
                break
    src_big = "./" + file_relative_path
    src = src_big[:-3] + "webp"
    title = input("what do you want to title the image? *･゜ﾟ･*:.｡..｡.:*･'(*ﾟ▽ﾟ*)'･*:.｡. .｡.:*･゜ﾟ･*\n")
    raw_tags = input("what are the tags? (ex: green, yellow)（；゜０゜）\n")
    tags = raw_tags.split(", ")
    raw_time = input("what is the time? (ex: 2022, Aug, 22)（＾ν＾）\n")
    time = raw_time.split(", ")
    hv = input("Is the image horizontal? type true or false (╯3╰)\n")
    rating = input("How do you rate the image? ♪───Ｏ（≧∇≦）Ｏ────♪\n")
    original.insert(index,'  },\n')
    original.insert(index,'    rating: '+rating+',\n')
    original.insert(index,'    hv: ' + hv + ',\n')
    original.insert(index,"    time: " + str(time) + ",\n")
    original.insert(index,"    tags: " + str(tags) + ",\n")
    original.insert(index,"    original_path: '" + str(src_big) + "',\n")
    original.insert(index,"    src: '" + str(src) + "',\n")
    original.insert(index,"    alt: '" + str(title) + "',\n")
    original.insert(index,'  {\n')

    with open(archive_path, 'w') as photo_archive:
        photo_archive.writelines( original )
