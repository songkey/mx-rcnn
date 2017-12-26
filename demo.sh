img_dir=/home/songkey/doc/data-set/knife/gaojing-knife-1117/JPEGImages
save_dir=/home/songkey/doc/data-set/knife/gaojing-knife-1117/JPEGImages-out
#model=/home/yanhaonan/Workspace/mxnet/train-dir/rcnn/save/1007/dh1007res34-s8

# test
#img_dir=/home/songkey/doc/data-set/zh-projs/zh1010/VOC2007/JPEGImages
#save_dir=/home/songkey/doc/data-set/zh-projs/zh1010-out
model=save/head1202/head-sk1202-32s16
#model=save/head/head-anchor1120
#img_dir=/mnt/hdisk1/dh-proj/testSet/sample1090/1020_filterd
#save_dir=/mnt/hdisk1/dh-proj/testSet/sample1090/1020_ori_out
#model=/home/yanhaonan/Workspace/mxnet/train-dir/rcnn/save/1023/dh1023-res34-s8-again
network=resnet
epoch=2
th=0.9

python demo_save3.py --threshold $th --image_dir $img_dir --save_dir $save_dir --prefix $model --epoch $epoch --gpu $1 
