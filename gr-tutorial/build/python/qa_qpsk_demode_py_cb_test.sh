#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/mnt/c/Users/peter/Desktop/acoustic_radio/gr-tutorial/python
export PATH=/mnt/c/Users/peter/Desktop/acoustic_radio/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/mnt/c/Users/peter/Desktop/acoustic_radio/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /mnt/c/Users/peter/Desktop/acoustic_radio/gr-tutorial/python/qa_qpsk_demode_py_cb.py 
