#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import numpy
from qpsk_demod_v2 import qpsk_demod_v2

class qa_qpsk_demod_v2 (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        gray_code = False
        src_data = ((-1-1j), (-1+1j), (1+1j), (1-1j))
        expected_result = (2, 3, 0, 1)
        src = blocks.vector_source_c (src_data)
        qpsk = qpsk_demod_v2 (gray_code)
        dst = blocks.vector_sink_b ()
        self.tb.connect (src, qpsk)
        self.tb.connect (qpsk, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

    def test_002_t (self):
        gray_code = True
        src_data = ((-1-1j), (-1+1j), (1+1j), (1-1j))
        expected_result = (3, 2, 0, 1)
        src = blocks.vector_source_c (src_data)
        qpsk = qpsk_demod_v2 (gray_code)
        dst = blocks.vector_sink_b ()
        self.tb.connect (src, qpsk)
        self.tb.connect (qpsk, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

if __name__ == '__main__':
    gr_unittest.run(qa_qpsk_demod_v2, "qpsk_demod_v2.xml")