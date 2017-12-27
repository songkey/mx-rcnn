network=resnet_fpn
model=save/resnet18-171226-fpn
epoch=1
image_path=/Users/songkey/Workspace/data-set/head-example/VOC2007/JPEGImages/mpii_train_images_000275100.jpg
json_save_path=resnet18-171226-fpn.json

--network $network --prefix $model --epoch $epoch --image $image_path --vis --save_json $json_save_path
