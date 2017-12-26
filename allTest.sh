img_dir=/mnt/hdisk1/dh-proj/testSet/2nd_test/pic
save_dir=/mnt/hdisk1/dh-proj/testSet/2nd_test/pic-out_05
model=/home/yanhaonan/Workspace/mxnet/train-dir/rcnn/save/1024/dh1024-res34-s8-more

#img_dir=/mnt/hdisk1/dh-proj/testSet/sample1090/1020_filterd
#save_dir=/mnt/hdisk1/dh-proj/testSet/sample1090/1020_ori_out
#model=/home/yanhaonan/Workspace/mxnet/train-dir/rcnn/save/1023/dh1023-res34-s8-again
network=resnet
epoch=8
th=0.5

python demo_save.py --threshold $th --image_dir $img_dir --save_dir $save_dir --prefix $model --epoch $epoch --gpu $1 
