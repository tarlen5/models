#!/bin/bash
for i in {0}
do
  #echo "$i"
  curl "http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d${i}_coco17_tpu-32.tar.gz" -o "efficientdet_d${i}_coco17_tpu-32.tar.gz"
  tar -xzf "efficientdet_d${i}_coco17_tpu-32.tar.gz"
done
