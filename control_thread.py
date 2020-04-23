from gnss_flowgraph import GNSSFlowgraph

configuration_ = {
######### GLOBAL OPTIONS ##################
'GNSS-SDR.internal_fs_sps': 2000000,
######### SIGNAL_SOURCE CONFIG ############
'SignalSource.implementation': 'File_Signal_Source',
'SignalSource.filename': r'C:\Users\F074018\Documents\2013_04_04_GNSS_SIGNAL_at_CTTC_SPAIN\2013_04_04_GNSS_SIGNAL_at_CTTC_SPAIN.dat',
'SignalSource.item_type': 'ishort',
'SignalSource.sampling_frequency': 4000000,
'SignalSource.freq': 1575420000,
'SignalSource.samples': 0,
######### SIGNAL_CONDITIONER CONFIG ############
'SignalConditioner.implementation': 'Signal_Conditioner',
'DataTypeAdapter.implementation': 'Ishort_To_Complex',
'InputFilter.implementation': 'Pass_Through',
'InputFilter.item_type': 'gr_complex',
'Resampler.implementation': 'Direct_Resampler',
'Resampler.sample_freq_in': 4000000,
'Resampler.sample_freq_out': 2000000,
'Resampler.item_type': 'gr_complex',
######### CHANNELS GLOBAL CONFIG ############
'Channels_1C.count': 8,
'Channels.in_acquisition': 1,
'Channel.signal': '1C',
######### ACQUISITION GLOBAL CONFIG ############
'Acquisition_1C.implementation': 'GPS_L1_CA_PCPS_Acquisition',
'Acquisition_1C.item_type': 'gr_complex',
'Acquisition_1C.pfa': 0.01,
'Acquisition_1C.doppler_max': 10000,
'Acquisition_1C.doppler_step': 250,
######### TRACKING GLOBAL CONFIG ############
'Tracking_1C.implementation': 'GPS_L1_CA_DLL_PLL_Tracking',
'Tracking_1C.item_type': 'gr_complex',
'Tracking_1C.pll_bw_hz': '40.0;',
'Tracking_1C.dll_bw_hz': '4.0;',
######### TELEMETRY DECODER GPS CONFIG ############
'TelemetryDecoder_1C.implementation': 'GPS_L1_CA_Telemetry_Decoder',
######### OBSERVABLES CONFIG ############
'Observables.implementation': 'Hybrid_Observables',
######### PVT CONFIG ############
'PVT.implementation': 'RTKLIB_PVT',
'PVT.positioning_mode': 'Single',
'PVT.output_rate_ms': 100,
'PVT.display_rate_ms': 500,
'PVT.iono_model': 'Broadcast',
'PVT.trop_model': 'Saastamoinen',
'PVT.flag_rtcm_server': True,
'PVT.flag_rtcm_tty_port': False,
'PVT.rtcm_dump_devname': '/dev/pts/1',
'PVT.rtcm_tcp_port': 2101,
'PVT.rtcm_MT1019_rate_ms': 5000,
'PVT.rtcm_MT1077_rate_ms': 1000,
'PVT.rinex_version': 2
}

# init

control_queue_ = []
flowgraph_ = GNSSFlowgraph(configuration_, control_queue_)

# run

flowgraph_.connect()
flowgraph_.start()