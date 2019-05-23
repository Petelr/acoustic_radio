#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Packet Encoder Decoder
# Generated: Thu May 23 14:57:21 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import display
import pmt
import sip
import wx


class packet_encoder_decoder(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Packet Encoder Decoder")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32E3
        self.code2 = code2 = '11011010110111011000110011110101100010010011110111'
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'

        ##################################################
        # Blocks
        ##################################################
        self.show_text_0 = display.show_text()
        self._show_text_0_win = sip.wrapinstance(self.show_text_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._show_text_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\peter\\Desktop\\acoustic_radio\\README.md', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=1,
        		bits_per_symbol=2,
        		preamble='',
        		access_code='',
        		pad_for_usrp=False,
        	),
        	payload_length=4,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.show_text_0, 0))
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_code2(self):
        return self.code2

    def set_code2(self, code2):
        self.code2 = code2

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1


def main(top_block_cls=packet_encoder_decoder, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
