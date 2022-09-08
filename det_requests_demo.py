import cv2
import requests

det_thyroid_url = "http://192.168.13.77:8083/predictions/det_thyroid_yolox"
img_fp = 'imgs\\demo.jpg'

file = {'data': open(img_fp, 'rb')}
det_thyroid_res = requests.post(det_thyroid_url, files=file)
print(det_thyroid_res.json())

bbox = []
for i in det_thyroid_res.json():
    bbox.append([int(j) for j in i['bbox']])

img = cv2.imread(img_fp)
for i in bbox:
    cv2.rectangle(img, (i[0], i[1]), (i[2], i[3]), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
