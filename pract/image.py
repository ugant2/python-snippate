#
#
# # Compute and display the (digital) negative of an image
#
# from PIL import Image
# import numpy as np
#
# image = Image.open('dmz4.png')
#
# source = image.split()
# r, g, b, a = 0, 1, 2, 3
#
# negate = lambda i: 255 - i
#
# transform = [source[band].point(negate) for band in (r, g, b)]
# if len(source) == 4:  ## should have 4 bands for images with alpha channel
#     transform.append(source[a])  # add alpha channel
#
# out = Image.merge(image.mode, transform)
# out.save('outputfile.png')
# out.show()
#
