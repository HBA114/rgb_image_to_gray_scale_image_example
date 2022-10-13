import cv2 as cv

fp_jpg = "images/profile.jpg"

image_jpg = cv.imread(fp_jpg, 1)

image_gray_scale = image_jpg.copy()

height = len(image_jpg)
width = len(image_jpg[0])

print(f"width {width}")
print(f"height {height}")

for i in range(height):
    for j in range(width):
        sum = 0
        mean = 0
        for pixelVal in image_jpg[i][j]: sum += pixelVal
        mean = sum / len(image_jpg[i][j])
        image_gray_scale[i][j][0] = mean
        image_gray_scale[i][j][1] = mean
        image_gray_scale[i][j][2] = mean


cv.imshow("rgb", image_jpg)    
cv.imshow("gray_scale", image_gray_scale)

cv.waitKey(0)
cv.destroyAllWindows()