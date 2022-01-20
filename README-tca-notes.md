# Additions to this repo

To get per-class COCO eval metrics for validation and test data, need to install separate evaluation code, based on [this colab notebook](https://colab.research.google.com/drive/1h9fJm6D6VhGpJqpCxOklEWmtH-luLtCM?usp=sharing#scrollTo=U7wVe_nICeWa). Did following installation steps first few steps from [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html)

1. Conda Python 3.9 environment
2. Tensorflow version 2.7.0
3. Originally, installed tensorflow models experimental repo from fork: `git clone --depth 1 https://github.com/qraleq/models`
  a. Subsequent times I've installed from my forked repo: `git clone https://github.com/tarlen5/models`
4. Copy COCO eval tools from new repo into install location in `site-packages`:
  a. `cp object_detection/metrics/cocoeval.py /home/timarlen/anaconda3/envs/tf_models/lib/python3.9/site-packages/pycocotools`
  b. `cp object_detection/metrics/cocoeval.py /home/timarlen/anaconda3/envs/tf_models/lib/python3.9/site-packages/object_detection/metrics`
5. Compile protos: `protoc object_detection/protos/*.proto --python_out=.`
6. Install Tensorflow 2 Object Detection API: `cp object_detection/packages/tf2/setup.py .; python -m pip install .`

(Make sure all tests pass, then should be ready).

## Detailed Notes for Ubuntu 18.04 GCP VM Instance with K80 GPU

(Correct as of 20220117) see file `detailed_install_notes.md`
