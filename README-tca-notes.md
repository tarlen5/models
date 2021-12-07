## Additions to this repo

To get per-class COCO eval metrics for validation and test data, need to install separate evaluation code, based on [this colab notebook](https://colab.research.google.com/drive/1h9fJm6D6VhGpJqpCxOklEWmtH-luLtCM?usp=sharing#scrollTo=U7wVe_nICeWa). Did following installation steps first few steps from [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html)

1. Conda Python 3.9 environment
2. tensorflow version 2.7.0
3. Install tensorflow models experimental repo from fork: `git clone --depth 1 https://github.com/qraleq/models`
4. Copy COCO eval tools from new repo into `dist-packages`: `cp models/object_detection/metrics/cocoeval.py /home/timarlen/anaconda3/envs/tf_models/lib/python3.9/site-packages/pycocotools`
(NOTE: And/or possibly destination dir is: `~/anaconda3/envs/tf_models/lib/python3.9/site-packages/object_detection/metrics/` (I believe it's one or the other).
5. compile protos: `protoc object_detection/protos/*.proto --python_out=.`
6. Install Tensorflow 2 Object Detection API: `cp object_detection/packages/tf2/setup.py .; python -m pip install .`

(Make sure all tests pass, then should be ready).
