

from PIL import Image
import os
import sys

try:

    if(sys.argv[1] == "resize"):
        if os.path.exists(sys.argv[2]):
            # get image information
            file = sys.argv[2]
            filepath = os.path.dirname(file)
            name = os.path.splitext(os.path.basename(file))[0]
            extension = os.path.splitext(file)[1]
            basewidth = sys.argv[3]

            #load img as object
            img = Image.open(file)
            print("Original size - " + str(img.size[0]) + "px")

            #get new width as percentage of original width
            wpercent = (float(basewidth) / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))

            #resize image and save it
            img = img.resize((int(basewidth), hsize), Image.ANTIALIAS)
            newPic = filepath + "/" + (name + "_resized" + extension)
            img.save(newPic)
            print("image created - " + newPic)
        else:
            print("Error resizing")
    elif(sys.argv[1] == "crop"):
        if os.path.exists(sys.argv[2]):
            file = sys.argv[2]
            # get image information
            filepath = os.path.dirname(file)
            name = os.path.splitext(os.path.basename(file))[0]
            extension = os.path.splitext(file)[1]
            img = Image.open(file)

            # Get dimensions
            width, height = img.size
            new_width = int(sys.argv[3])
            new_height = int(sys.argv[4])
            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = (width + new_width) / 2
            bottom = (height + new_height) / 2
            area = (left, top, right, bottom)

            #crop image and save it
            cropped_img = img.crop(area)
            newPic = filepath + "/" + (name + "_cropped" + extension)
            cropped_img.save(newPic)
            print("image created - " + newPic)
        else:
            print("Error converting")
    else:
        print("command " + sys.argv[1]+ " doesn't exist")

except Exception as e:
    print(e)
    print("something went wrong\n"
          "COMMANDS\n"
          "resize 'FILE' 'WIDTH'\n"
          "crop 'FILE' 'WIDTH" 'HEIGHT')
