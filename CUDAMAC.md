# FILENAME CUDAMAC.md
# SOURCE https://www.cs.rochester.edu/u/kautz/Installing-Pytorch-Cuda-on-Macbook.html

# Contents
## Install

###Installing Pytorch with CUDA on a 2012 Macbook Pro Retina 15
The best laptop ever produced was the 2012-2014 Macbook Pro Retina with 15 inch display. It has a CUDA-capable GPU, the NVIDIA GeForce GT 650M. This GPU has 384 cores and 1 GB of VRAM, and is CUDA capability 3. Although puny by modern standards, it provides about a 4X speedup over the cpu for Pytorch, and is fine for learning Pytorch and prototyping. If you have a newer MacBook Pro you are out of luck, because it either has a Radeon GPU or none at all.

The standard Mac distribution of Pytorch does not support CUDA, but it is supported if you compile Pytorch from source. There are numerous preliminary steps and "gotchas". Here is what you need to do. Thanks to Jack Dyson for this write up based on an earlier version that I published earlier. These instructions have been tested for:

OS : MacOS High Sierra 10.13.6 (17G14042)
GPU Driver: NVIDIA Web Driver 387.10.10.10.4.140
GPU CUDA Driver Version: 418.163
Xcode Version: 10.1 (10B61)
Downgrade to High Sierra

Check that you are running Mac OS X High Sierra (10.13.6). If you have an older version, upgrade. If you have a newer version you will need to downgrade; Apple banished CUDA with Mojave and later versions of the OS. Downgrading OS X requires creating a bootable USB memory stick installer and erasing your laptop's hard disk.

Install Xcode

Check that you have installed Xcode version 10.1. If you have a newer version or none at all, download it from the Apple Developer site. Rename any other version of Xcode you have installed, and then copy it to /Applications. Open Xcode, and under preferences, select the 10.1 command line tools. Close Xcode and open a terminal. Run

xcode-select --install
to reinstall the command line tools, because sometimes the Xcode application fails to install certain header files.
Install NVIDIA Drivers

Install the NVIDIA Quadro and Geforce OS X Driver 387.10.10.10.40.140.

Add to your .profile and reboot:

export PATH=/Developer/NVIDIA/CUDA-10.0/bin${PATH:+:${PATH}}
export DYLD_LIBRARY_PATH=/usr/local/cuda/lib:$DYLD_LIBRARY_PATH
xport DYLD_LIBRARY_PATH=/usr/local/cuda/lib:$DYLD_LIBRARY_PATH.

Install Conda

Install Anaconda. Create an environment named ptc that includes pip, activate it, and install libraries:
conda create --name ptc python=3.7
conda activate ptc
conda install numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
conda install pkg-config libuv
Build Pytorch

Now you are ready to build Pytorch with Cuda!

conda activate ptc
git clone --recursive https://github.com/pytorch/pytorch
Finally you build:

cd pytorch
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ python setup.py install
Post Installation

conda activate ptc
pip install torchvision

Reboot and test that pytorch with CUDA is working:

conda activate ptc
python
import torch
torch.cuda.is_available()
If python does not print "true", something has gone wrong.
Install ptc as a kernel for jupyter notebooks.

conda deactivate
conda install ipykernel
python -m ipykernel install --user --name ptc --display-name "Python 3.7 (ptc)"
When a program first invokes CUDA, a warning message will be printing stating that the GPU is too old. The message can be ignored - CUDA will indeed work! In order to eliminate the message, edit the file

~/anaconda3/envs/ptc/lib/python3.6/site-packages/torch/cuda/__init__.py
and in the definition of the function _check_capability() eliminate the string
capability==(3,0) or
Download Pytorch examples and compare time required with and without cuda. Note that these examples require Torchvision.

git clone https://github.com/pytorch/examples
cd examples/mnist
conda activate ptc
time python main.py >/dev/null
real 1m38.430s
user 2m6.163s
sys 0m7.762s
time python main.py --no-cuda >/dev/null
real 5m47.750s
user 37m22.609s
sys 1m23.813s
For the non-CUDA case, user time is greater than real time because Pytorch makes use of all 8 cpu hyperthread cores.

Congratulations, you are ready to set the deep learning world on fire!

Henry Kautz, 21 December 2020
