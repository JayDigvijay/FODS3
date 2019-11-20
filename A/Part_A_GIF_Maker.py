
from PIL import Image
images = []
for j in range(160):
    im = Image.open('Image Data/plot' + str(j+1) + '.png')
    images.append(im)
    

images[0].save('Graphs.gif', save_all=True, append_images=images[1:], optimize=False, duration=100, loop=1)			