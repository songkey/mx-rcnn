root_dir=~/Documents/data-set/mxnet-cache
#dataset_dir=/home/songkey/doc/data-set/zh-projs/test1014
dataset_dir=~/Documents/data-set/zh-projs/zh1030
#model=save/model1021/zh1021-600x600
model=save/model1028/zh1028-4deg-8
#model=save/model1023/zh1023-2
network=resnet
epoch=247
th=0.85
python test.py --thresh $th --root_path $root_dir --network $network --dataset_path $dataset_dir  --image_set 2007_test --gpu $1 --prefix $model --epoch $epoch
