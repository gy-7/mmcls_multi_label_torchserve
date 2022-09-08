import requests

cls_slice_url = "http://192.168.13.77:8080/predictions/cls_slice_resnet50"

cls_thyroid_url = "http://192.168.13.77:8080/predictions/cls_thyroid_resnet50"

cls_componente_url = "http://192.168.13.77:8080/predictions/cls_componente_resnet50"
cls_echoes_url = "http://192.168.13.77:8080/predictions/cls_echoes_resnet50"
cls_edges_url = "http://192.168.13.77:8080/predictions/cls_edges_resnet50"

# 多标签分类
cls_strong_echoes_url = "http://192.168.13.77:8080/predictions/cls_strong_echoes_resnet50"
# img_fp = 'F:\\imgs\\thyroid\\demo1.jpg'
img_fp = 'F:\\imgs\\thyroid\\nodule (1).jpg'

file = {'data': open(img_fp, 'rb')}
cls_res = requests.post(cls_slice_url, files=file)
print(cls_res.json())

file = {'data': open(img_fp, 'rb')}
cls_res = requests.post(cls_thyroid_url, files=file)
print(cls_res.json())

file = {'data': open(img_fp, 'rb')}
cls_res = requests.post(cls_componente_url, files=file)
print(cls_res.json())

file = {'data': open(img_fp, 'rb')}
cls_res = requests.post(cls_echoes_url, files=file)
print(cls_res.json())

file = {'data': open(img_fp, 'rb')}
cls_res = requests.post(cls_edges_url, files=file)
print(cls_res.json())

file = {'data': open(img_fp, 'rb')}
cls_res = requests.post(cls_strong_echoes_url, files=file)
print(cls_res.json())
