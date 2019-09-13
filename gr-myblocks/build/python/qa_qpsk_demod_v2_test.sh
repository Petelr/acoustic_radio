#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/peter/Desktop/acoustic_radio/gr-myblocks/python
export PATH=/home/peter/Desktop/acoustic_radio/gr-myblocks/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/peter/Desktop/acoustic_radio/gr-myblocks/build/swig:$PYTHONPATH
/usr/bin/python2 /home/peter/Desktop/acoustic_radio/gr-myblocks/python/qa_qpsk_demod_v2.py 
