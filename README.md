## mmcls ���ǩ



==GitHub�ֿ�==��[gy-7/mmcls_multi_label_torchserve (github.com)](https://github.com/gy-7/mmcls_multi_label_torchserve) 



�����ļ�˵����

> cls_requests_demo������ģ������api�����demo
>
> det_requests_demo�����ģ������api�����demo
>
> inference��Ҫ�޸ĵ�inference����
>
> mmcls_handler��Ҫ�޸ĵ�mmcls_handler����
>
> torchserve_log�������������ı�����



#### :one: �޸� mmcls_handler.py

��������Ҫ�������mmcls_handler.py ��ת�� pytorch ģ��Ϊ torch serve ģ�͵�ʱ���õ��ġ�ת�������а���ߵ�����Ƕ�뵽ת����� torch serve ģ�����ˡ�

������Ҫ�޸ĵ��� mmcls_handler �� postprocess �Ĳ��������ֿ��� mmcls_handler.py �ļ����ݸ��ǵ�mmclassification/tools/deployment/mmcls_handler.py��



#### :two: ����ת�����е�ģ�ͣ�

```powershell
python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_componente_resnet50.py ../torchserve/pytorch_models/cls_componente_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_componente_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_echoes_resnet50.py ../torchserve/pytorch_models/cls_echoes_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_echoes_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_edges_resnet50.py ../torchserve/pytorch_models/cls_edges_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_edges_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_slice_resnet50.py ../torchserve/pytorch_models/cls_slice_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_slice_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_thyroid_resnet50.py ../torchserve/pytorch_models/cls_thyroid_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_thyroid_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_strong_echoes_resnet50.py ../torchserve/pytorch_models/cls_strong_echoes_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_strong_echoes_resnet50
```



#### :three: �޸�inference.py

inference.py �ǵ���api�����ʱ�򣬵��õĽӿڡ�������docker װ�� torch serve������������Ҫ�޸�������ߵ� Դ�롣

����ԭ�ȵķ��񣬽���������

```powershell
docker exec -it --user root 7f0f1ea9e3e8 /bin/bash

# �޸�inference.py
vim /opt/conda/lib/python3.7/site-packages/mmcls/apis/inference.py 

# ���澵��
docker commit -m "fix inference.py" 7f0f1ea9e3e8 mmcls-serve_multi_label:latest
```



#### :four: �������ĳ�������� 

ǰ����ǵ���ǩ�����һ���Ƕ��ǩ��

```powershell
{'pred_label': 2, 'pred_score': 0.9856280088424683, 'pred_class': 'vertical'}
{'pred_label': 0, 'pred_score': 0.9774421453475952, 'pred_class': 'benign'}
{'pred_label': 4, 'pred_score': 0.6918501853942871, 'pred_class': 'componentes_4'}
{'pred_label': 2, 'pred_score': 0.5446202158927917, 'pred_class': 'echoes_2'}
{'pred_label': 1, 'pred_score': 0.4259072542190552, 'pred_class': 'edges_1'}
{'pred_label': [0, 0, 0, 0, 0], 'pred_score': [0.46634966135025024, 0.07801822572946548, 0.2685200273990631, 0.016055332496762276, 0.13444863259792328], 'pred_class': []}
```

