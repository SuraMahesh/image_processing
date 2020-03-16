import cv2

img = cv2.imread('rose.jpg')
print("Image Properties")
print("- Nber of Pixels: " + str(img.size))
print("- Shape/Dimension: " + str(img.shape))
