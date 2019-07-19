import cv2, imutils, os
import numpy as np
np.set_printoptions(suppress=True)

num_images = 760

#COMPILES image paths, move images to this file directory and change the folder name to yours
image_paths = []
for i in range(num_images):
    path_to_img = os.path.join(os.getcwd(),'shards-hughes20_3f2c46','shard-{}.png'.format(i))
    image_paths.append(path_to_img)

for i in range(num_images):
    img = cv2.imread(image_paths[i])
    if i==0:
        images = np.zeros((num_images,)+img.shape)
    images[i,:,:,:] = img

#finds the error between image j's top and image i's bottom
top_errors = np.zeros((num_images,num_images))
for j in range(num_images):
    for i in range(num_images):
        top_errors[j,i] = np.sum((images[j,0,:,:]-images[i,-1,:,:])**2)
np.fill_diagonal(top_errors, float("inf")) #image can not be ontop of itself

#finds the error between image j's left side and image i's right side
side_errors = np.zeros((num_images,num_images))
for j in range(num_images):
    for i in range(num_images):
        side_errors[j,i] = np.sum((images[j,:,0,:]-images[i,:,-1,:])**2)
np.fill_diagonal(side_errors, float("inf")) #image can not be next to itself

# print(np.min(side_errors, axis=1))
no_top_threshold = 10000
min = np.min(top_errors,axis=1)
print((min > no_top_threshold).sum()) #theoretical number of image columns

# """
# This part is probably going to have to change, binning needs to take into account
# more information
# """
# img = images[0]
# img_ind = 0
# bins = [[0]]
# bin_index = 0
# for i in range(num_images):
#     value = np.min(top_errors[img_ind])
#     print(bin_index, img_ind, value)
#
#     img_ind = np.argmin(top_errors[img_ind])
#     top_errors[:,img_ind] = float("inf") #can not choose this index again
#
#     #if this image has no image above, make a new bin
#     if value > no_top_threshold:
#         bin_index += 1
#         bins.append([img_ind])
#     else:
#         bins[bin_index].append(img_ind)
#
# print(len(bins))
#
# for i,bin in enumerate(bins):
#
#     img = images[bin[0]]
#     for image_ind in bin[1:]:
#         img = np.concatenate((images[image_ind], img), axis=0)
#     cv2.imshow("test{}".format(i),img/255.)
#     if i==10:
#         break
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
