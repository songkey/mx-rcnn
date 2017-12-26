root_dir=~/Documents/data-set/mxnet-cache-head
dataset_dir=/home/songkey/doc/data-set/head
model=resnet-18
prefix=save/171226fpn
network=resnet_fpn
epoch=0
end_epoch=999
python train_end2end.py --root_path $root_dir --dataset_path $dataset_dir  --image_set 2007_trainval --gpus $1 --prefix $prefix --pretrained $model --pretrained_epoch $epoch --network $network --reset_anchors
# --lr $lr
#--data_argument --neg_data_dir $neg_dir 
#--reset_anchors 
#--lr $lr
#--resume

