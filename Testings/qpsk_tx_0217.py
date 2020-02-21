#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Qpsk Tx 0217
# Generated: Thu Feb 20 20:35:13 2020
##################################################


from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class qpsk_tx_0217(gr.top_block):

    def __init__(self, freq=5000, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0), input_file="test_input.txt"):
        gr.top_block.__init__(self, "Qpsk Tx 0217")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.hdr_format = hdr_format
        self.input_file = input_file

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 50
        self.nfilts = nfilts = 32
        self.excess_bw = excess_bw = 1
        self.samp_rate = samp_rate = 44100
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), excess_bw, 11*sps*nfilts)

        self.qpsk = qpsk = digital.constellation_qpsk().base()

        self.excess_bw_0 = excess_bw_0 = 1
        self.carrier_freq = carrier_freq = freq

        ##################################################
        # Blocks
        ##################################################
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, 'len_key')
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=qpsk,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.7,
          verbose=False,
          log=False,
          )
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/peter/Desktop/out.wav', 1, samp_rate, 8)
        self.blocks_vector_source_x_0 = blocks.vector_source_b((0,3,2,1), True, 1, [])
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 35, "len_key")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 20, "len_key")
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, input_file, True)
        self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_char*1, '/home/peter/Desktop/acoustic_radio/Testings/Debugs/input.txt', False)
        self.blocks_file_sink_2.set_unbuffered(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, 9e3, 15e3, 100, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, carrier_freq, -1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrier_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_tagged_stream_mux_0_0, 1))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.blocks_file_sink_2, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_carrier_freq(self.freq)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_input_file(self):
        return self.input_file

    def set_input_file(self, input_file):
        self.input_file = input_file
        self.blocks_file_source_0.open(self.input_file, True)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excess_bw, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excess_bw, 11*self.sps*self.nfilts))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.excess_bw, 11*self.sps*self.nfilts))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 9e3, 15e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_excess_bw_0(self):
        return self.excess_bw_0

    def set_excess_bw_0(self, excess_bw_0):
        self.excess_bw_0 = excess_bw_0

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_0_0.set_frequency(self.carrier_freq)
        self.analog_sig_source_x_0.set_frequency(self.carrier_freq)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-f", "--freq", dest="freq", type="intx", default=5000,
        help="Set freq [default=%default]")
    parser.add_option(
        "-i", "--input-file", dest="input_file", type="string", default="test_input.txt",
        help="Set input_file [default=%default]")
    return parser


def main(top_block_cls=qpsk_tx_0217, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(freq=options.freq, input_file=options.input_file)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
