# Importing a library that is not in Colaboratory
!pip install -q matplotlib-venn
!apt-get -qq install -y libfluidsynth1

# Upgrading TensorFlow
# To determine which version you're using:
!pip show tensorflow

# For the current version:
!pip install --upgrade tensorflow

# For a specific version:
!pip install tensorflow==1.2

# For the latest nightly build:
!pip install tf-nightly

# Install Pytorch
from os import path
from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag
platform = '{}{}-{}'.format(get_abbr_impl(), get_impl_ver(), get_abi_tag())

accelerator = 'cu80' if path.exists('/opt/bin/nvidia-smi') else 'cpu'

!pip install -q http://download.pytorch.org/whl/{accelerator}/torch-0.4.0-{platform}-linux_x86_64.whl torchvision

# Install 7zip reader libarchive
# https://pypi.python.org/pypi/libarchive
!apt-get -qq install -y libarchive-dev && pip install -q -U libarchive
import libarchive

# Install GraphViz & PyDot
# https://pypi.python.org/pypi/pydot
!apt-get -qq install -y graphviz && pip install -q pydot
import pydot

# Install cartopy
!apt-get -qq install python-cartopy python3-cartopy
import cartopy
