root_dir=~/Documents/data-set/mxnet-cache-head
dataset_dir=/home/songkey/doc/data-set/head
prefix=save/resnet18-171226-fpn
network=resnet_fpn
epoch=1
th=0.5
python test.py --root_path $root_dir --dataset_path $dataset_dir  --image_set 2007_test --gpus $1 --prefix $prefix --epoch $epoch --network $network --thresh $th
