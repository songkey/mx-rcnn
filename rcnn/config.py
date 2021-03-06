import numpy as np
from easydict import EasyDict as edict

config = edict()

# network related params
config.PIXEL_MEANS = np.array([103.939, 116.779, 123.68])
config.IMAGE_STRIDE = 0
config.RPN_FEAT_STRIDE = 16
config.RCNN_FEAT_STRIDE = 16
config.FIXED_PARAMS = ['conv1', 'conv2']
config.FIXED_PARAMS_SHARED = ['conv1', 'conv2', 'conv3', 'conv4', 'conv5']

# dataset related params
config.NUM_CLASSES = 2
config.SCALES = [(512, 1024)]  # first is scale (the shorter side); second is max size
config.ANCHOR_SCALES = (8, 16, 32)
config.ANCHOR_RATIOS = (0.5, 1, 2)
config.NUM_ANCHORS = len(config.ANCHOR_SCALES) * len(config.ANCHOR_RATIOS)
config.CLASS_ID = [0, 24, 25, 26, 27, 28, 31, 32, 33]

config.TRAIN = edict()

config.TRAIN.IMAGE_BLOB = None

# R-CNN and RPN
# size of images for each device, 2 for rcnn, 1 for rpn and e2e
config.TRAIN.BATCH_IMAGES = 2
# e2e changes behavior of anchor loader and metric
config.TRAIN.END2END = False
# group images with similar aspect ratio
config.TRAIN.ASPECT_GROUPING = True

# R-CNN
# rcnn rois batch size
config.TRAIN.BATCH_ROIS = 128
# rcnn rois sampling params
config.TRAIN.FG_FRACTION = 0.25
config.TRAIN.FG_THRESH = 0.5
config.TRAIN.BG_THRESH_HI = 0.5
config.TRAIN.BG_THRESH_LO = 0.0
# rcnn bounding box regression params
config.TRAIN.BBOX_REGRESSION_THRESH = 0.5
config.TRAIN.BBOX_WEIGHTS = np.array([1.0, 1.0, 1.0, 1.0])

# RPN anchor loader
# rpn anchors batch size
config.TRAIN.RPN_BATCH_SIZE = 256
# rpn anchors sampling params
config.TRAIN.RPN_FG_FRACTION = 0.5
config.TRAIN.RPN_POSITIVE_OVERLAP = 0.7
config.TRAIN.RPN_NEGATIVE_OVERLAP = 0.3
config.TRAIN.RPN_CLOBBER_POSITIVES = False
# rpn bounding box regression params
config.TRAIN.RPN_BBOX_WEIGHTS = (1.0, 1.0, 1.0, 1.0)
config.TRAIN.RPN_POSITIVE_WEIGHT = -1.0

# used for end2end training
# RPN proposal
config.TRAIN.CXX_PROPOSAL = True
config.TRAIN.RPN_NMS_THRESH = 0.7
config.TRAIN.RPN_PRE_NMS_TOP_N = 12000
config.TRAIN.RPN_POST_NMS_TOP_N = 2000
# approximate bounding box regression
config.TRAIN.BBOX_NORMALIZATION_PRECOMPUTED = True
config.TRAIN.BBOX_MEANS = (0.0, 0.0, 0.0, 0.0)
config.TRAIN.BBOX_STDS = (0.1, 0.1, 0.2, 0.2)
# config.TRAIN.BBOX_STDS = (1, 1, 1, 1)

config.TEST = edict()

# R-CNN testing
# use rpn to generate proposal
config.TEST.HAS_RPN = False
# size of images for each device
config.TEST.BATCH_IMAGES = 1

# RPN proposal
config.TEST.CXX_PROPOSAL = True
config.TEST.RPN_NMS_THRESH = 0.7
config.TEST.RPN_PRE_NMS_TOP_N = 6000
config.TEST.RPN_POST_NMS_TOP_N = 300

# RPN generate proposal
config.TEST.PROPOSAL_NMS_THRESH = 0.7
config.TEST.PROPOSAL_PRE_NMS_TOP_N = 20000
config.TEST.PROPOSAL_POST_NMS_TOP_N = 2000

# RCNN nms
config.TEST.NMS = 0.3

# default settings
default = edict()

# default network
default.network = 'vgg'
default.pretrained = 'model/vgg16'
default.pretrained_epoch = 0
default.base_lr = 0.004
# default dataset
default.dataset = 'PascalVOC'
default.image_set = '2007_trainval'
default.test_image_set = '2007_test'
default.root_path = 'data'
default.dataset_path = 'data/VOCdevkit'
# default training
default.frequent = 20
default.kvstore = 'device'
# default e2e
default.e2e_prefix = 'model/e2e'
default.e2e_epoch = 10
default.e2e_lr = default.base_lr
default.e2e_lr_step = '7'
# default rpn
default.rpn_prefix = 'model/rpn'
default.rpn_epoch = 8
default.rpn_lr = default.base_lr
default.rpn_lr_step = '6'
# default rcnn
default.rcnn_prefix = 'model/rcnn'
default.rcnn_epoch = 8
default.rcnn_lr = default.base_lr
default.rcnn_lr_step = '6'

# network settings
network = edict()

network.vgg = edict()

network.vgg_fpn = edict()
network.vgg_fpn.pretrained = 'model/vgg16'
network.vgg_fpn.pretrained_epoch = 0
network.vgg_fpn.ANCHOR_SCALES = (8,)
network.vgg_fpn.ANCHOR_RATIOS = (0.5, 1, 2)
network.vgg_fpn.NUM_ANCHORS = len(network.vgg_fpn.ANCHOR_SCALES) * len(network.vgg_fpn.ANCHOR_RATIOS)
network.vgg_fpn.RPN_FEAT_STRIDE = [32, 16, 8, 4]
network.vgg_fpn.RCNN_FEAT_STRIDE = [32, 16, 8, 4]
network.vgg_fpn.FIXED_PARAMS = ['conv1', 'conv2']
network.vgg_fpn.FIXED_PARAMS_SHARED = ['conv1', 'conv2', 'conv3', 'conv4', 'conv5']

network.resnet = edict()
network.resnet.pretrained = 'model/resnet-34'
network.resnet.pretrained_epoch = 0
network.resnet.PIXEL_MEANS = np.array([0, 0, 0])
network.resnet.IMAGE_STRIDE = 0
network.resnet.RPN_FEAT_STRIDE = 16
network.resnet.RCNN_FEAT_STRIDE = 16
network.resnet.FIXED_PARAMS = ['conv0', 'stage1', 'gamma', 'beta']
network.resnet.FIXED_PARAMS_SHARED = ['conv0', 'stage1', 'stage2', 'stage3', 'gamma', 'beta']

network.resnet_fpn = edict()
network.resnet_fpn.pretrained = 'model/resnet-34'
network.resnet_fpn.pretrained_epoch = 0
network.resnet_fpn.PIXEL_MEANS = np.array([0, 0, 0])
network.resnet_fpn.IMAGE_STRIDE = 0
network.resnet_fpn.ANCHOR_SCALES = (8, 16, )
network.resnet_fpn.ANCHOR_RATIOS = (0.5, 1, 2)
network.resnet_fpn.NUM_ANCHORS = len(network.resnet_fpn.ANCHOR_SCALES) * len(network.resnet_fpn.ANCHOR_RATIOS)
network.resnet_fpn.RPN_FEAT_STRIDE = [32, 16, 8, 4]
network.resnet_fpn.RCNN_FEAT_STRIDE = [32, 16, 8, 4]
network.resnet_fpn.FIXED_PARAMS = ['conv0', 'stage1', 'gamma', 'beta']
network.resnet_fpn.FIXED_PARAMS_SHARED = ['conv0', 'stage1', 'stage2', 'stage3', 'gamma', 'beta']

# dataset settings
dataset = edict()

dataset.PascalVOC = edict()

dataset.coco = edict()
dataset.coco.dataset = 'coco'
dataset.coco.image_set = 'train2014'
dataset.coco.test_image_set = 'val2014'
dataset.coco.root_path = 'data'
dataset.coco.dataset_path = 'data/coco'
dataset.coco.NUM_CLASSES = 81

dataset.Cityscape = edict()
dataset.Cityscape.image_set = 'train'
dataset.Cityscape.test_image_set = 'val'
dataset.Cityscape.root_path = 'data'
dataset.Cityscape.dataset_path = 'data/cityscape'
dataset.Cityscape.NUM_CLASSES = 9
dataset.Cityscape.SCALES = [(1024, 2048)]
dataset.Cityscape.ANCHOR_SCALES = (8,)
dataset.Cityscape.ANCHOR_RATIOS = (0.5, 1, 2)
dataset.Cityscape.NUM_ANCHORS = len(dataset.Cityscape.ANCHOR_SCALES) * len(dataset.Cityscape.ANCHOR_RATIOS)
dataset.Cityscape.CLASS_ID = [0, 24, 25, 26, 27, 28, 31, 32, 33]

dataset.AiChallenge = edict()
dataset.AiChallenge.NUM_CLASSES = 2
dataset.AiChallenge.image_set = 'val'
dataset.AiChallenge.test_image_set = 'val'
dataset.AiChallenge.dataset_path = r'E:\ai_challenger'

def generate_config(_network, _dataset):
    for k, v in network[_network].items():
        if k in config:
            config[k] = v
        elif k in default:
            default[k] = v
    if _dataset is not None:
        for k, v in dataset[_dataset].items():
            if k in config:
                config[k] = v
            elif k in default:
                default[k] = v

