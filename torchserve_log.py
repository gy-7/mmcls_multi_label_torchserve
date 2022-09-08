'''
ERROR1

File "/opt/conda/lib/python3.7/site-packages/ts/service.py", line 102, in predict
  ret = self._entry_point(input_batch, self.context)
File "/opt/conda/lib/python3.7/site-packages/ts/torch_handler/base_handler.py", line 233, in handle
  output = self.postprocess(output)
File "/home/model-server/tmp/models/d137f1361e83454ea2e7fb93acd201c7/mmcls_handler.py", line 50, in postprocess
  result['pred_label'] = int(result['pred_label'])
TypeError: only size-1 arrays can be converted to Python scalars





ERROR2:

File "/opt/conda/lib/python3.7/site-packages/ts/protocol/otf_message_handler.py", line 130, in create_predict_response
  json_value = json.dumps(val, indent=2).encode("utf-8")
File "/opt/conda/lib/python3.7/json/__init__.py", line 238, in dumps
  **kw).encode(obj)
File "/opt/conda/lib/python3.7/json/encoder.py", line 201, in encode
  chunks = list(chunks)
File "/opt/conda/lib/python3.7/json/encoder.py", line 431, in _iterencode
  yield from _iterencode_dict(o, _current_indent_level)
File "/opt/conda/lib/python3.7/json/encoder.py", line 405, in _iterencode_dict
  yield from chunks
File "/opt/conda/lib/python3.7/json/encoder.py", line 325, in _iterencode_list
  yield from chunks
File "/opt/conda/lib/python3.7/json/encoder.py", line 438, in _iterencode
  o = _default(o)
File "/opt/conda/lib/python3.7/json/encoder.py", line 179, in default
  raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type ndarray is not JSON serializable

'''


"""
# single label res:
{
    "pred_label": 0,
    "pred_score": 0.6702142953872681,
    "pred_class": "benign"
}

# multi label res:
{
    "pred_label": [
        0,
        0,
        1,
        0,
        0
    ],
    "pred_score": [
        [
            0.0873648151755333,
            0.1539262980222702,
            0.36885952949523926,
            0.009535334073007107,
            0.2623801827430725
        ]
    ],
    "pred_class": [
        "strong_echos3"
    ]
}

"""



"""
2022-09-08T01:49:47,831 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_METRICS - HandlerTime.Milliseconds:164.09|#ModelName:cls_strong_echoes_resnet50,Level:Model|#hostname:c833a8d176a3,requestID:fdc4b154-d84c-42ec-9b1e-33980e2993ab,timestamp:1662601787
2022-09-08T01:49:47,831 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_METRICS - PredictionTime.Milliseconds:164.12|#ModelName:cls_strong_echoes_resnet50,Level:Model|#hostname:c833a8d176a3,requestID:fdc4b154-d84c-42ec-9b1e-33980e2993ab,timestamp:1662601787
2022-09-08T01:49:47,832 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 ACCESS_LOG - /192.168.11.105:63807 "POST /predictions/cls_strong_echoes_resnet50 HTTP/1.1" 503 192
2022-09-08T01:49:47,832 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 TS_METRICS - Requests5XX.Count:1|#Level:Host|#hostname:c833a8d176a3,timestamp:1662601787
2022-09-08T01:49:47,832 [DEBUG] W-9003-cls_strong_echoes_resnet50_1.0 org.pytorch.serve.job.Job - Waiting time ns: 115696, Inference time ns: 168606560
2022-09-08T01:49:47,832 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 TS_METRICS - WorkerThreadTime.ms:3|#Level:Host|#hostname:c833a8d176a3,timestamp:1662601787
2022-09-08T01:49:51,083 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1662601791083
2022-09-08T01:49:51,084 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662601791
2022-09-08T01:49:51,093 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result['pred_label']: [0 0 0 0 0]
2022-09-08T01:49:51,093 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Unable to serialize model output.
2022-09-08T01:49:51,093 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T01:49:51,093 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/protocol/otf_message_handler.py", line 130, in create_predict_response
2022-09-08T01:49:51,093 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     json_value = json.dumps(val, indent=2).encode("utf-8")
2022-09-08T01:49:51,093 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/__init__.py", line 238, in dumps
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     **kw).encode(obj)
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 201, in encode
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     chunks = list(chunks)
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 431, in _iterencode
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from _iterencode_dict(o, _current_indent_level)
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 405, in _iterencode_dict
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from chunks
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 438, in _iterencode
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     o = _default(o)
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 179, in default
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     raise TypeError(f'Object of type {o.__class__.__name__} '
2022-09-08T01:49:51,094 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - TypeError: Object of type ndarray is not JSON serializable






2022-09-08T02:14:21,027 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662603261
2022-09-08T02:14:21,207 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result['pred_label']: [0 0 0 0 0]
2022-09-08T02:14:21,208 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Unable to serialize model output.
2022-09-08T02:14:21,208 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T02:14:21,208 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/protocol/otf_message_handler.py", line 130, in create_predict_response
2022-09-08T02:14:21,208 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     json_value = json.dumps(val, indent=2).encode("utf-8")
2022-09-08T02:14:21,208 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/__init__.py", line 238, in dumps
2022-09-08T02:14:21,208 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 182
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     **kw).encode(obj)
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 201, in encode
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     chunks = list(chunks)
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 431, in _iterencode
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from _iterencode_dict(o, _current_indent_level)
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 405, in _iterencode_dict
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from chunks
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 438, in _iterencode
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     o = _default(o)
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 179, in default
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     raise TypeError(f'Object of type {o.__class__.__name__} '
2022-09-08T02:14:21,209 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - TypeError: Object of type ndarray is not JSON serializable


2022-09-08T02:41:34,269 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662604894

2022-09-08T02:41:34,277 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - ------------------------------
2022-09-08T02:41:34,278 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': array([0, 0, 0, 0, 0]), 'pred_score': array([0.46634966, 0.07801823, 0.26852003, 0.01605533, 0.13444863],
2022-09-08T02:41:34,278 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -       dtype=float32), 'pred_class': []}
2022-09-08T02:41:34,278 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'numpy.ndarray'>
2022-09-08T02:41:34,278 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>
2022-09-08T02:41:34,278 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>
2022-09-08T02:41:34,279 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - ------------------------------
2022-09-08T02:41:34,279 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - after postprocess
2022-09-08T02:41:34,279 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': [0, 0, 0, 0, 0], 'pred_score': array([0.46634966, 0.07801823, 0.26852003, 0.01605533, 0.13444863],
2022-09-08T02:41:34,279 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -       dtype=float32), 'pred_class': []}
2022-09-08T02:41:34,280 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'list'>
2022-09-08T02:41:34,280 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>
2022-09-08T02:41:34,280 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>


2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Unable to serialize model output.
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/protocol/otf_message_handler.py", line 130, in create_predict_response
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     json_value = json.dumps(val, indent=2).encode("utf-8")
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/__init__.py", line 238, in dumps
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     **kw).encode(obj)
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 201, in encode
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     chunks = list(chunks)
2022-09-08T02:41:34,282 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 431, in _iterencode
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from _iterencode_dict(o, _current_indent_level)
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 405, in _iterencode_dict
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from chunks
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 438, in _iterencode
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     o = _default(o)
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 179, in default
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     raise TypeError(f'Object of type {o.__class__.__name__} '
2022-09-08T02:41:34,283 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - TypeError: Object of type ndarray is not JSON serializable



2022-09-08T02:44:53,637 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662605093
2022-09-08T02:44:53,817 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - ------------------------------
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': array([0, 0, 0, 0, 0]), 'pred_score': array([0.46634966, 0.07801823, 0.26852003, 0.01605533, 0.13444863],
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -       dtype=float32), 'pred_class': []}
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'numpy.ndarray'>
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - ------------------------------
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - after postprocess
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': [0, 0, 0, 0, 0], 'pred_score': array([0.46634966, 0.07801823, 0.26852003, 0.01605533, 0.13444863],
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -       dtype=float32), 'pred_class': []}
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'list'>
2022-09-08T02:44:53,818 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>

2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Unable to serialize model output.
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/protocol/otf_message_handler.py", line 130, in create_predict_response
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     json_value = json.dumps(val, indent=2).encode("utf-8")
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/__init__.py", line 238, in dumps
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     **kw).encode(obj)
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 201, in encode
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     chunks = list(chunks)
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 431, in _iterencode
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from _iterencode_dict(o, _current_indent_level)
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 405, in _iterencode_dict
2022-09-08T02:44:53,819 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     yield from chunks
2022-09-08T02:44:53,820 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 438, in _iterencode
2022-09-08T02:44:53,820 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 183
2022-09-08T02:44:53,820 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     o = _default(o)
2022-09-08T02:44:53,820 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/json/encoder.py", line 179, in default
2022-09-08T02:44:53,820 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -     raise TypeError(f'Object of type {o.__class__.__name__} '
2022-09-08T02:44:53,820 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - TypeError: Object of type ndarray is not JSON serializable


2022-09-08T02:48:45,931 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662605325
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - Invoking custom service failed.
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/service.py", line 102, in predict
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG -     ret = self._entry_point(input_batch, self.context)
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/torch_handler/base_handler.py", line 233, in handle
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG -     output = self.postprocess(output)
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/7f530cc9473e47c8aba84f916b279343/mmcls_handler.py", line 50, in postprocess
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG -     result['pred_label'] = int(result['pred_label'])
2022-09-08T02:48:45,941 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - TypeError: only size-1 arrays can be converted to Python scalars


2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - ---------- before process ----------
2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'numpy.ndarray'>
2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>
2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>
2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - ---------- after process ----------
2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': [1, 0, 0], 'pred_score': [0.9329271912574768, 0.06698808073997498, 8.470565808238462e-05], 'pred_class': ['horizontal']}
2022-09-08T02:58:08,052 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'list'>
2022-09-08T02:58:08,053 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'list'>
2022-09-08T02:58:08,053 [INFO ] W-9005-cls_slice_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>


2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - ---------- before process ----------
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': array([0, 0, 1, 0, 0]), 'pred_score': array([0.01471758, 0.05931407, 0.9632461 , 0.0797285 , 0.07844918],
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -       dtype=float32), 'pred_class': ['strong_echos3']}
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'numpy.ndarray'>
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - ---------- after process ----------
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 178
2022-09-08T03:00:32,752 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': [0, 0, 1, 0, 0], 'pred_score': [0.014717579819262028, 0.059314072132110596, 0.9632461071014404, 0.07972849905490875, 0.07844918221235275], 'pred_class': ['strong_echos3']}
2022-09-08T03:00:32,753 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'list'>
2022-09-08T03:00:32,753 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'list'>
2022-09-08T03:00:32,753 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_class <class 'list'>


2022-09-08T07:56:07,481 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662623767
2022-09-08T07:56:07,541 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - pred_label.shape: (2,)
2022-09-08T07:56:07,541 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - len(pred_label): 2
2022-09-08T07:56:07,541 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - len(class_name): 1
2022-09-08T07:56:07,541 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - class_name: ['benign']
2022-09-08T07:56:07,541 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - Invoking custom service failed.
2022-09-08T07:56:07,541 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/service.py", line 102, in predict
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -     ret = self._entry_point(input_batch, self.context)
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 62
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/torch_handler/base_handler.py", line 232, in handle
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -     output = self.inference(data_preprocess)
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/f178b53b6fb5466e89c45e94c85579b6/mmcls_handler.py", line 45, in inference
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0 ACCESS_LOG - /192.168.11.105:51171 "POST /predictions/cls_thyroid_resnet50 HTTP/1.1" 503 63
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -     results.append(inference_model(self.model, image))
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0 TS_METRICS - Requests5XX.Count:1|#Level:Host|#hostname:843c8e0c3c69,timestamp:1662623698
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/mmcls/apis/inference.py", line 107, in inference_model
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG -     pred_class.append(np.array(class_name)[i])
2022-09-08T07:56:07,542 [DEBUG] W-9002-cls_thyroid_resnet50_1.0 org.pytorch.serve.job.Job - Waiting time ns: 81760, Inference time ns: 62059047
2022-09-08T07:56:07,542 [INFO ] W-9002-cls_thyroid_resnet50_1.0-stdout MODEL_LOG - IndexError: index 1 is out of bounds for axis 0 with size 1


2022-09-08T07:57:04,864 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - Backend received inference at: 1662623824
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - pred_label.shape: (6,)
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - len(pred_label): 6
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - len(class_name): 1
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - class_name: ['componentes_0']
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - Invoking custom service failed.
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - Traceback (most recent call last):
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/service.py", line 102, in predict
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -     ret = self._entry_point(input_batch, self.context)
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/ts/torch_handler/base_handler.py", line 232, in handle
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0 org.pytorch.serve.wlm.WorkerThread - Backend response time: 40
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -     output = self.inference(data_preprocess)
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/a219ae77bc734e86b11d121d5ca55182/mmcls_handler.py", line 45, in inference
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -     results.append(inference_model(self.model, image))
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0 ACCESS_LOG - /192.168.11.105:51199 "POST /predictions/cls_componente_resnet50 HTTP/1.1" 503 43
2022-09-08T07:57:04,903 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -   File "/opt/conda/lib/python3.7/site-packages/mmcls/apis/inference.py", line 107, in inference_model
2022-09-08T07:57:04,904 [INFO ] W-9004-cls_componente_resnet50_1.0 TS_METRICS - Requests5XX.Count:1|#Level:Host|#hostname:843c8e0c3c69,timestamp:1662623698
2022-09-08T07:57:04,904 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG -     pred_class.append(np.array(class_name)[i])
2022-09-08T07:57:04,904 [INFO ] W-9004-cls_componente_resnet50_1.0-stdout MODEL_LOG - IndexError: index 4 is out of bounds for axis 0 with size 1


2022-09-08T08:12:20,447 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - result: {'pred_label': array([0, 0, 1, 0, 0]), 'pred_score': array([0.01471758, 0.05931407, 0.9632461 , 0.0797285 , 0.07844918],
2022-09-08T08:12:20,447 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG -       dtype=float32)}
2022-09-08T08:12:20,447 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_label <class 'numpy.ndarray'>
2022-09-08T08:12:20,448 [INFO ] W-9003-cls_strong_echoes_resnet50_1.0-stdout MODEL_LOG - pred_score <class 'numpy.ndarray'>


"""
