#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BFSK
# Author: John Mortimore
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import audio
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0)):
        gr.top_block.__init__(self, "BFSK")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BFSK")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.hdr_format = hdr_format

        ##################################################
        # Variables
        ##################################################
        self.freq_symbol_1 = freq_symbol_1 = 10584
        self.freq_symbol_0 = freq_symbol_0 = 8820
        self.samp_rate = samp_rate = 44.1e3
        self.fsk_deviation_hz = fsk_deviation_hz = freq_symbol_1-freq_symbol_0
        self.filter_taps = filter_taps = firdes.low_pass(1.0,samp_rate,fsk_deviation_hz,400)
        self.SPS = SPS = 200

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcf(1, filter_taps, (freq_symbol_1+freq_symbol_0)/2, samp_rate)
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, 'len_key')
        self.digital_correlate_access_code_xx_ts_1_0_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          6, 'len_key2')
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(SPS, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_vector_source_x_0 = blocks.vector_source_b((1,0), True, 1, [])
        self.blocks_tagged_stream_to_pdu_0_0_0_0_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'len_key2')
        self.blocks_tagged_stream_mux_1 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 147, 'len_key')
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 100, 'len_key')
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, SPS)
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key2', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_not_xx_0 = blocks.not_bb()
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.6)
        self.blocks_message_debug_0_0_0_0_0 = blocks.message_debug()
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/peter/Desktop/acoustic_radio/Testings/test_input.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/peter/Desktop/output.txt', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_char_to_float_2 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(2)
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                freq_symbol_1-100,
                freq_symbol_1+100,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                freq_symbol_0-100,
                freq_symbol_0+100,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_source_0 = audio.source(44100, '', True)
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_symbol_1, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq_symbol_0, 1, 0, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz/8.0))



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0_0_0_0_0, 'pdus'), (self.blocks_message_debug_0_0_0_0_0, 'print'))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.audio_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_char_to_float_2, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_not_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_not_xx_0, 0), (self.blocks_char_to_float_2, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_tagged_stream_mux_1, 1))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.blocks_tagged_stream_to_pdu_0_0_0_0_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_1, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_correlate_access_code_xx_ts_1_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0_0, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_freq_symbol_1(self):
        return self.freq_symbol_1

    def set_freq_symbol_1(self, freq_symbol_1):
        self.freq_symbol_1 = freq_symbol_1
        self.set_fsk_deviation_hz(self.freq_symbol_1-self.freq_symbol_0)
        self.analog_sig_source_x_1.set_frequency(self.freq_symbol_1)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_symbol_1-100, self.freq_symbol_1+100, 100, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq((self.freq_symbol_1+self.freq_symbol_0)/2)

    def get_freq_symbol_0(self):
        return self.freq_symbol_0

    def set_freq_symbol_0(self, freq_symbol_0):
        self.freq_symbol_0 = freq_symbol_0
        self.set_fsk_deviation_hz(self.freq_symbol_1-self.freq_symbol_0)
        self.analog_sig_source_x_0.set_frequency(self.freq_symbol_0)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_symbol_0-100, self.freq_symbol_0+100, 100, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq((self.freq_symbol_1+self.freq_symbol_0)/2)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_filter_taps(firdes.low_pass(1.0,self.samp_rate,self.fsk_deviation_hz,400))
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_symbol_0-100, self.freq_symbol_0+100, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.freq_symbol_1-100, self.freq_symbol_1+100, 100, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.set_filter_taps(firdes.low_pass(1.0,self.samp_rate,self.fsk_deviation_hz,400))
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.filter_taps)

    def get_SPS(self):
        return self.SPS

    def set_SPS(self, SPS):
        self.SPS = SPS
        self.blocks_repeat_0.set_interpolation(self.SPS)
        self.digital_clock_recovery_mm_xx_0.set_omega(self.SPS)


def argument_parser():
    parser = ArgumentParser()
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
