import easyocr
import cv2

src = cv2.imread('./car.JPG')
gray =  cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
cv2.imwrite('car_gray.JPG', gray)

blur = cv2.medianBlur(src, 7)
cv2.imwrite('car_blur.JPG', blur)

height, width, _ = src.shape
print (height, width)

crop_height = 200
crop_width = 250

center_x, center_y = width // 2, height //2

x_start = center_x - (crop_width // 2)
x_end = center_x + (crop_width // 2)

y_start = center_y - (crop_height // 2)
y_end = center_y + (crop_height // 2)

cropped = src[y_start:y_end, x_start:x_end]
cv2.imwrite('car_cropped.jpg', cropped)

reader = easyocr.Reader(['en', 'ko'], gpu=False)
results = reader.readtext('./car_cropped.JPG')

for result in results:
    # if result[2] > 0.4:
        print(result[1])