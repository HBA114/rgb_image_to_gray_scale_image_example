import cv2 as cv

fp_jpg = "images/profile.jpg"

image_jpg = cv.imread(fp_jpg, 1)
# print(image_jpg)

cv.imshow("jpg", image_jpg)

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
        image_jpg[i][j][0] = mean
        image_jpg[i][j][1] = mean
        image_jpg[i][j][2] = mean


    
cv.imshow("new", image_jpg)
cv.waitKey(0)
cv.destroyAllWindows()