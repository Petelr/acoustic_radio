#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Qpsk Rx 0217
# Generated: Wed Mar  4 17:30:37 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class qpsk_rx_0217(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Qpsk Rx 0217")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Qpsk Rx 0217")
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

        self.settings = Qt.QSettings("GNU Radio", "qpsk_rx_0217")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 10

        self.qpsk = qpsk = digital.constellation_qpsk().base()

        self.excess_bw = excess_bw = 0.7
        self.rxmod = rxmod = digital.generic_mod(qpsk, False, sps, True, excess_bw, False, False)
        self.nfilts = nfilts = 32
        self.samp_rate = samp_rate = 44100
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), excess_bw, 11*sps*nfilts)
        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(rxmod .to_basic_block(), ([0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]), ([1]))
        self.lpf_transition_width = lpf_transition_width = 100
        self.lpf_cutoff_freq = lpf_cutoff_freq = 3e3
        self.carrier_freq = carrier_freq = 5e3

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=50/sps,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	512, #size
        	1, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-100, 4000)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 15, 0, 'corr_est')
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	128, #size
        	samp_rate, #samp_rate
        	"End", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 150)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "len_key2")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	128, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.05)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, lpf_cutoff_freq, lpf_transition_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, lpf_cutoff_freq, lpf_transition_width, firdes.WIN_HAMMING, 6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 62.8e-3, (rrc_taps), nfilts, nfilts/2, 1.5, 11)
        self.digital_lms_dd_equalizer_cc_0 = digital.lms_dd_equalizer_cc(15, 10E-3, 11, qpsk)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(4)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(62.8e-3, 4, False)
        self.digital_correlate_access_code_xx_ts_1_0_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          12, "len_key2")
        self.digital_corr_est_cc_0 = digital.corr_est_cc((modulated_sync_word), sps, 156, 0.99)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(qpsk)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/peter/Desktop/acoustic_radio/Testings/Debugs/output2.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/peter/Desktop/acoustic_radio/Testings/Debugs/output1.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_char*1,
        	addr='127.0.0.1',
        	port=9989,
        	server=False,
        )
        self.audio_source_0 = audio.source(44100, '', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, carrier_freq, -1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrier_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blks2_tcp_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.digital_correlate_access_code_xx_ts_1_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_corr_est_cc_0, 1), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_1_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_lms_dd_equalizer_cc_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_corr_est_cc_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qpsk_rx_0217")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excess_bw, 11*self.sps*self.nfilts))
        self.set_rxmod(digital.generic_mod(self.qpsk, False, self.sps, True, self.excess_bw, False, False))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.set_rxmod(digital.generic_mod(self.qpsk, False, self.sps, True, self.excess_bw, False, False))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excess_bw, 11*self.sps*self.nfilts))
        self.set_rxmod(digital.generic_mod(self.qpsk, False, self.sps, True, self.excess_bw, False, False))

    def get_rxmod(self):
        return self.rxmod

    def set_rxmod(self, rxmod):
        self.rxmod = rxmod

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excess_bw, 11*self.sps*self.nfilts))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff_freq, self.lpf_transition_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff_freq, self.lpf_transition_width, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_modulated_sync_word(self):
        return self.modulated_sync_word

    def set_modulated_sync_word(self, modulated_sync_word):
        self.modulated_sync_word = modulated_sync_word

    def get_lpf_transition_width(self):
        return self.lpf_transition_width

    def set_lpf_transition_width(self, lpf_transition_width):
        self.lpf_transition_width = lpf_transition_width
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff_freq, self.lpf_transition_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff_freq, self.lpf_transition_width, firdes.WIN_HAMMING, 6.76))

    def get_lpf_cutoff_freq(self):
        return self.lpf_cutoff_freq

    def set_lpf_cutoff_freq(self, lpf_cutoff_freq):
        self.lpf_cutoff_freq = lpf_cutoff_freq
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff_freq, self.lpf_transition_width, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff_freq, self.lpf_transition_width, firdes.WIN_HAMMING, 6.76))

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_0_0.set_frequency(self.carrier_freq)
        self.analog_sig_source_x_0.set_frequency(self.carrier_freq)


def main(top_block_cls=qpsk_rx_0217, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
