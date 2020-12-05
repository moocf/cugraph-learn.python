#!/usr/bin/env bash
# Install RAPIDS (Colaboratory)
git clone https://github.com/rapidsai/rapidsai-csp-utils.git
bash rapidsai-csp-utils/colab/rapids-colab.sh stable
python3 setup.py
