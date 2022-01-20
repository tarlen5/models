# 1. SYSTEM INSTALLS
#sudo apt install emacs25-nox
#sudo apt -y install wget
#sudo apt -y install gcc
#sudo apt -y install protobuf-compiler

# 2. CUDA/CUDNN INSTALLS
# Install cuda toolkit v11.2, following these instructions:
# https://developer.nvidia.com/cuda-11.2.2-download-archive?target_os=Linux&target_arch=x86_6\
4&target_distro=Ubuntu&target_version=1804&target_type=deblocal
# Install cudnn library:
# https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-linux

# 3. Python/Anaconda Install
#wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
#bash Anaconda3-2021.11-Linux-x86_64.sh
#echo "Creating tensorflow (tf_models) env:"
#conda create -y -n tf_models pip python=3.9

# > conda activate tf_models

# pip install --ignore-installed --upgrade tensorflow==2.7.0
# User needs to test installation with command in shell:
# python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# 4. Tensorflow models/object_detection API:
# make directory to install models:
#mkdir -p ~/work/Tensorflow
#cd ~/work/Tensorflow
#Install tensorflow models experimental repo from fork:
#git clone https://github.com/tarlen5/models

# Install cocoapi:
#git clone https://github.com/cocodataset/cocoapi.git
#pip install Cython
#cd cocoapi/PythonAPI
#make
#cp -r pycocotools <PATH_TO_TF>/TensorFlow/models/research/

# 5. Protobuf
# Protobuf Installation/Compilation
# From within TensorFlow/models/research/
#protoc object_detection/protos/*.proto --python_out=.

# 6. Install Tensorflow models object detection API and copy over file:
# From within TensorFlow/models/research/
#cp object_detection/packages/tf2/setup.py .
#python -m pip install --use-feature=2020-resolver .

# Now copy cocoeval metrics into two directories:
# 1) cp models/research/object_detection/metrics/cocoeval.py ~/anaconda3/envs/tf_models/lib/p\
ython3.9/site-packages/object_detection/metrics/
# 2) cp models/research/object_detection/metrics/cocoeval.py ~/anaconda3/envs/tf_models/lib/p\
ython3.9/site-packages/pycocotools
