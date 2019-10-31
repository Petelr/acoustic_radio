#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Delay Test
# Generated: Wed Oct 30 21:54:57 2019
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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class delay_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Delay Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Delay Test")
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

        self.settings = Qt.QSettings("GNU Radio", "delay_test")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.samp_rate = samp_rate = 6e6
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)

        self.constel = constel = digital.constellation_calcdist((digital.psk_4()[0]), (digital.psk_4()[1]), 4, 1).base()

        self.constel.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1_0_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Filter", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_1_0.disable_legend()

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

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_1_0_win)
        self.qtgui_time_sink_x_1_0_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Before and After Down Conversion", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_1.enable_grid(False)
        self.qtgui_time_sink_x_1_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_1.disable_legend()

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

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_1_win)
        self.qtgui_time_sink_x_1_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Imaginary", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0.disable_legend()

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
                self.qtgui_time_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Real", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()

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
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.filter_delay_fc_0 = filter.filter_delay_fc((rrc_taps))
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=constel,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.blocks_vector_source_x_0 = blocks.vector_source_b((255, 127, 0), True, 1, [])
        self.blocks_multiply_xx_0_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10e4, 1, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10e4, -1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 10e4, -1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10e4, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_2, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_1_0_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.qtgui_time_sink_x_1_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.qtgui_time_sink_x_1_0_1, 1))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.qtgui_time_sink_x_1_0_1_0, 1))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.qtgui_time_sink_x_1_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.filter_delay_fc_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_2, 0), (self.filter_delay_fc_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.filter_delay_fc_0, 0), (self.blocks_complex_to_float_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "delay_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel


def main(top_block_cls=delay_test, options=None):

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
