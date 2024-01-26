import numpy as np
from PIL import Image

def floste(image_array):
     for y in range(image_array.shape[0] - 1):
          for x in range(1, image_array.shape[1] - 1):
               old_pixel = image_array[y, x]
               new_pixel = np.round(old_pixel / 255) * 255
               image_array[y, x] = new_pixel
               error = old_pixel - new_pixel
               image_array[y, x + 1] += error * 7 / 16
               image_array[y + 1, x - 1] += error * 3 / 16
               image_array[y + 1, x] += error * 5 / 16
               image_array[y + 1, x + 1] += error * 1 / 16
     return image_array


img = Image.open('lesmis.jpeg')
img_gray = img.convert('L')  #See comment below, please :)
image_array = np.array(img_gray, dtype=np.float64)
dithered_image = floste(image_array)
Image.fromarray(dithered_image.astype(np.uint8)).save('floste-lesmis.jpeg')


'''
Hi, Mr. Oswald! For this part, I have more questions than ever. I found the Source 2
on how there are different ways to make an image gray by using different libraries.
In this case, I decided to work with Pillow, and I found an example in which they used 
the code from line 19. Do you recommend me working with the greyscale code I worked with
on the Hannibal Images, or shall I stick to this line with Lesmis?

Thank you for your time! 
'''