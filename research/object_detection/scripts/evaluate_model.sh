#!/bin/bash
#let i="3"
#echo $i
for i in {0..7};
do
PIPELINE_CONFIG_PATH="/home/tensorflow/models/research/object_detection/models/checkpoints/detection/efficientdet_d"${i}"_coco17_tpu-32/pipeline_eval.config"
MODEL_DIR="/home/tensorflow/models/research/object_detection/models/checkpoints/detection/efficientdet_d${i}_coco17_tpu-32/checkpoint/"
CHECKPOINT_DIR=${MODEL_DIR}
python ../model_main_tf2.py \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --model_dir=${MODEL_DIR} \
    --checkpoint_dir=${CHECKPOINT_DIR} \
    --eval_timeout=5 \
    --alsologtostderr
done
