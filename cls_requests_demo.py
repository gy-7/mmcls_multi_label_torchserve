import requests

# 单标签分类模型
cls_slice_url = "http://192.168.13.77:8080/predictions/cls_slice_resnet50"
cls_thyroid_url = "http://192.168.13.77:8080/predictions/cls_thyroid_resnet50"
cls_componente_url = "http://192.168.13.77:8080/predictions/cls_componente_resnet50"
cls_echoes_url = "http://192.168.13.77:8080/predictions/cls_echoes_resnet50"
cls_edges_url = "http://192.168.13.77:8080/predictions/cls_edges_resnet50"

# 多标签分类模型
cls_strong_echoes_url = "http://192.168.13.77:8080/predictions/cls_strong_echoes_resnet50"

img_fp = 'F:\\imgs\\thyroid\\demo1.jpg'

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


"""
{'pred_label': 0, 'pred_score': 0.9329271912574768, 'pred_class': 'horizontal'}
{'pred_label': 1, 'pred_score': 0.7967439293861389, 'pred_class': 'malignant'}
{'pred_label': 4, 'pred_score': 0.9904775619506836, 'pred_class': 'componentes_4'}
{'pred_label': 3, 'pred_score': 0.6424677968025208, 'pred_class': 'echoes_3'}
{'pred_label': 1, 'pred_score': 0.45823922753334045, 'pred_class': 'edges_1'}
{'pred_label': [0, 0, 1, 0, 0], 'pred_score': [0.014717579819262028, 0.059314072132110596, 0.9632461071014404, 0.07972849905490875, 0.07844918221235275], 'pred_class': ['strong_echos3']}
"""