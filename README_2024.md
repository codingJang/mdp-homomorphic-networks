# Cloning MDP Homomorphic Networks repository in 2024

## Installation
* **Note:** Only tested for Linux, no guarantees for other operating systems. Atari doesn't work for now.
* Create Conda environment and install the stable PyTorch build 2.1.2 along with CUDA 11.8:
  * ``` conda create -n rlpyt python=3.11.5 ```
  * ``` source activate rlpyt ```
  * ``` conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia ```
  * ``` conda install numpy matplotlib psutil```
  * ``` pip install pyprind ```
* Install the RLPYT framework within the current repo:
  * ```clone``` the current repo and ```cd``` into it
  * ``` pip install -e . ```
* Install the [Symmetrizer](https://github.com/ElisevanderPol/symmetrizer "Symmetrizer Gitub") in the same rlpyt env:
  * ```clone``` the Symmetrizer repo and ```cd``` into it
  * ``` pip install gym==0.17 ```
  * ``` pip install -e . ```
* Optionally: Install the [grid world environment](https://github.com/ElisevanderPol/gridworld "Grid world environment") in the same rlpyt env:
  * ```clone``` the grid world environment and ```cd``` into it
  * ``` pip install -e . ```
* See if the Symmetrizer works: **
  * ``` ./tests.sh ```