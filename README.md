## mmcls 多标签



==GitHub仓库==：[gy-7/mmcls_multi_label_torchserve (github.com)](https://github.com/gy-7/mmcls_multi_label_torchserve) 



各个文件说明：

> cls_requests_demo：分类模型请求api服务的demo
>
> det_requests_demo：检测模型请求api服务的demo
>
> inference：要修改的inference代码
>
> mmcls_handler：要修改的mmcls_handler代码
>
> torchserve_log：过程中遇到的报错集合



#### :one: 修改 mmcls_handler.py

我们首先要搞清楚，mmcls_handler.py 是转换 pytorch 模型为 torch serve 模型的时候用到的。转换过程中把里边的内容嵌入到转换完的 torch serve 模型里了。

我们主要修改的是 mmcls_handler 中 postprocess 的操作。将仓库中 mmcls_handler.py 文件内容覆盖掉mmclassification/tools/deployment/mmcls_handler.py。



#### :two: 重新转换所有的模型：

```powershell
python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_componente_resnet50.py ../torchserve/pytorch_models/cls_componente_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_componente_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_echoes_resnet50.py ../torchserve/pytorch_models/cls_echoes_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_echoes_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_edges_resnet50.py ../torchserve/pytorch_models/cls_edges_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_edges_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_slice_resnet50.py ../torchserve/pytorch_models/cls_slice_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_slice_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_thyroid_resnet50.py ../torchserve/pytorch_models/cls_thyroid_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_thyroid_resnet50

python tools/deployment/mmcls2torchserve.py ../torchserve/pytorch_models/cls_strong_echoes_resnet50.py ../torchserve/pytorch_models/cls_strong_echoes_resnet50.pth --output-folder ../torchserve/torchserve_models/mmcls/ --model-name cls_strong_echoes_resnet50
```



#### :three: 修改inference.py

inference.py 是调用api服务的时候，调用的接口。我们用docker 装的 torch serve服务，所以我们要修改容器里边的 源码。

启动原先的服务，进入容器。

```powershell
docker exec -it --user root 7f0f1ea9e3e8 /bin/bash

# 修改inference.py
vim /opt/conda/lib/python3.7/site-packages/mmcls/apis/inference.py 

# 保存镜像
docker commit -m "fix inference.py" 7f0f1ea9e3e8 mmcls-serve_multi_label:latest
```



#### :four: 可以愉快的出来结果了 

前五个是单标签，最后一个是多标签。

```powershell
{'pred_label': 2, 'pred_score': 0.9856280088424683, 'pred_class': 'vertical'}
{'pred_label': 0, 'pred_score': 0.9774421453475952, 'pred_class': 'benign'}
{'pred_label': 4, 'pred_score': 0.6918501853942871, 'pred_class': 'componentes_4'}
{'pred_label': 2, 'pred_score': 0.5446202158927917, 'pred_class': 'echoes_2'}
{'pred_label': 1, 'pred_score': 0.4259072542190552, 'pred_class': 'edges_1'}
{'pred_label': [0, 0, 0, 0, 0], 'pred_score': [0.46634966135025024, 0.07801822572946548, 0.2685200273990631, 0.016055332496762276, 0.13444863259792328], 'pred_class': []}
```

