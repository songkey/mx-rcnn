root_dir=~/Documents/data-set/mxnet-cache-head
dataset_dir=/home/songkey/doc/data-set/head
prefix=save/resnet18-171226-fpn
prefix=save/resnet18-171226-fpn
network=resnet_fpn
epoch=1
end_epoch=999
python train_end2end.py --root_path $root_dir --dataset_path $dataset_dir  --image_set 2007_trainval --gpus $1 --prefix $prefix --pretrained $model --pretrained_epoch $epoch --network $network 

