## Run SSD in Caffe
Clone the files
```shell
git clone https://github.com/weiliu89/caffe.git
cd caffe
git checkout ssd
```
Build the file <i>(refer to Install caffe)</i>
```
# Modify Makefile.config according to your Caffe installation.
cp Makefile.config.example Makefile.config
make -j8
# Make sure to include $CAFFE_ROOT/python to your PYTHONPATH.
make py
make test -j8
# (Optional)
make runtest -j8
```

Edit enironment variable
```shell
exprot $HOME_SSD=/media/harddrive/github/caffe_ssd
exprot $PYTHONPATH=$HOME_SSD/python:$PYTHONPATH
```
Create links (<b>Note</b>: remember tochange the dir in `.sh` files )
```
cd $CAFFE_ROOT
# Create the trainval.txt, test.txt, and test_name_size.txt in data/VOC0712/
./data/VOC0712/create_list.sh
# You can modify the parameters in create_data.sh if needed.
# It will create lmdb files for trainval and test with encoded original image:
#   - $HOME/data/VOCdevkit/VOC0712/lmdb/VOC0712_trainval_lmdb
#   - $HOME/data/VOCdevkit/VOC0712/lmdb/VOC0712_test_lmdb
# and make soft links at examples/VOC0712/
./data/VOC0712/create_data.sh
```

Dependency
```
sudo apt-get install python-sklearn python-skimage python-protobuf
```
Strongly recommend this package
```
sudo apt-get install ipython
(Optical: ipython-notebook)
```

[Reference1](https://github.com/weiliu89/caffe/tree/ssd)

[Reference2](http://lib.csdn.net/article/deeplearning/53859)

SSD: Single Shot MultiBox Detector 训练KITTI数据集
http://blog.csdn.net/jesse_mx/article/details/65634482
http://blog.csdn.net/jesse_mx/article/details/70048255
