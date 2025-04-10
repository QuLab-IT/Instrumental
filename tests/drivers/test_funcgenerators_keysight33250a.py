import pytest
import numpy as np
import os

# Generated test file for Keysight33500B class
# This file is auto-generated. Do not edit manually.

# Add the parent directory to the Python path to import the driver
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class TestKeysight33500B:
    @pytest.fixture(scope='class')
    def instrument(self):
        # Get the VISA address from environment variable or use default
        visa_address = os.getenv('TEST_VISA_ADDRESS', 'TCPIP0::192.168.1.1::inst0::INSTR')
        from instrumental.drivers.funcgenerators.keysight33500b import Keysight33500B
        inst = Keysight33500B(visa_address)
        yield inst
        # Clean up after all tests
        inst.close()

    def test_cls(self, instrument):
        # Test Clear the event register in all register groups. This command also clears the error queue and cancels a *OPC operation. 

        # Call the method
        instrument.cls()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_ese(self, instrument):
        # Test Enable bits in the Standard Event Status Register to be reported in the Status Byte. The selected bits are summarized in the "Standard Event" bit (bit 5) of the Status Byte Register. 

        # Call the method
        result = instrument.get_ese()

        # Verify the response is not None
        assert result is not None

    def test_set_ese(self, instrument):
        # Test Enable bits in the Standard Event Status Register to be reported in the Status Byte. The selected bits are summarized in the "Standard Event" bit (bit 5) of the Status Byte Register. 

        # Call the method
        instrument.set_ese()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_esr(self, instrument):
        # Test Query the Standard Event Status Register. Once a bit is set, it remains set until cleared by a *CLS (clear status) command or queried by this command. 

        # Call the method
        result = instrument.get_esr()

        # Verify the response is not None
        assert result is not None

    def test_get_idn(self, instrument):
        # Test Read the function generator's identification string which contains four fields separated by commas. The first field is the manufacturer's name, the second field is the model number, the third field is the serial number, and the fourth field is a revision code which contains four numbers separated by dashes. 

        # Call the method
        result = instrument.get_idn()

        # Verify the response is not None
        assert result is not None

    def test_get_lrn(self, instrument):
        # Test Query the function generator and return a string of SCPI commands containing the current settings (learn string). You can then send the string back to the instrument to restore this state at a later time. 

        # Call the method
        result = instrument.get_lrn()

        # Verify the response is not None
        assert result is not None

    def test_get_opc(self, instrument):
        # Test Set the "Operation Complete" bit (bit 0) in the Standard Event register after the previous commands have completed. When used with a bus-triggered sweep or burst, you may have the opportunity to execute commands after the *OPC command and before the "Operation Complete" bit is set in the register. 

        # Call the method
        result = instrument.get_opc()

        # Verify the response is not None
        assert result is not None

    def test_opc(self, instrument):
        # Test Set the "Operation Complete" bit (bit 0) in the Standard Event register after the previous commands have completed. When used with a bus-triggered sweep or burst, you may have the opportunity to execute commands after the *OPC command and before the "Operation Complete" bit is set in the register. 

        # Call the method
        instrument.opc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_psc(self, instrument):
        # Test Power-On Status Clear. Clear the Standard Event enable register and Status Byte condition register at power on (*PSC 1). When *PSC 0 is in effect, these two registers are not cleared at power on. 

        # Call the method
        result = instrument.get_psc()

        # Verify the response is not None
        assert result is not None

    def test_set_psc(self, instrument):
        # Test Power-On Status Clear. Clear the Standard Event enable register and Status Byte condition register at power on (*PSC 1). When *PSC 0 is in effect, these two registers are not cleared at power on. 

        # Call the method
        instrument.set_psc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_rcl(self, instrument):
        # Test Recall the instrument state stored in the specified non-volatile storage location. You cannot recall the instrument state from a storage location that is empty. 

        # Call the method
        instrument.set_rcl()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_rst(self, instrument):
        # Test Reset the function generator to its factory default state.

        # Call the method
        instrument.rst()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_sav(self, instrument):
        # Test Store (save) the current instrument state in the specified non-volatile storage location. Any state previously stored in the same location will be overwritten (and no error will be generated). 

        # Call the method
        instrument.set_sav()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_sre(self, instrument):
        # Test Enable bits in the Status Byte to generate a Service Request. The selected bits are summarized in the "Master Summary" bit (bit 6) of the Status Byte Register. If any of the selected bits change from "0" to "1", a Service Request signal is generated. 

        # Call the method
        result = instrument.get_sre()

        # Verify the response is not None
        assert result is not None

    def test_set_sre(self, instrument):
        # Test Enable bits in the Status Byte to generate a Service Request. The selected bits are summarized in the "Master Summary" bit (bit 6) of the Status Byte Register. If any of the selected bits change from "0" to "1", a Service Request signal is generated. 

        # Call the method
        instrument.set_sre()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_stb(self, instrument):
        # Test Query the summary (condition) register in this register group. This command is similar to a Serial Poll but it is processed like any other instrument command. This command returns the same result as a Serial Poll but the "Master Summary" bit (bit 6) is not cleared by the *STB? command. 

        # Call the method
        result = instrument.get_stb()

        # Verify the response is not None
        assert result is not None

    def test_trg(self, instrument):
        # Test Trigger a sweep or burst from the remote interface only if the bus (software) trigger source is currently selected (TRIG:SOUR BUS command). 

        # Call the method
        instrument.trg()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_tst(self, instrument):
        # Test Perform a complete self-test of the function generator. Returns "+0" (PASS) or "+1" (FAIL). If the test fails, one or more error messages will be generated to provide additional information on the failure. 

        # Call the method
        result = instrument.get_tst()

        # Verify the response is not None
        assert result is not None

    def test_wai(self, instrument):
        # Test Wait for all pending operations to complete before executing any additional commands over the interface. 

        # Call the method
        instrument.wai()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_apply(self, instrument):
        # Test Query the function generator's current configuration and return a quoted string.

        # Call the method
        result = instrument.get_apply()

        # Verify the response is not None
        assert result is not None

    def test_set_apply_dc(self, instrument):
        # Test Output a dc voltage with the level specified by the offset parameter. The dc voltage is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_dc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_apply_noise(self, instrument):
        # Test Output Gaussian noise with the specified amplitude and dc offset. The waveform is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_noise()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_apply_pulse(self, instrument):
        # Test Output a pulse wave with the specified frequency, amplitude, and dc offset. The waveform is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_pulse()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_apply_ramp(self, instrument):
        # Test Output a ramp wave with the specified frequency, amplitude, and dc offset. This command overrides the current symmetry setting and automatically selects 100%. The waveform is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_ramp()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_apply_sinusoid(self, instrument):
        # Test Output a sine wave with the specified frequency, amplitude, and dc offset. The waveform is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_sinusoid()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_apply_square(self, instrument):
        # Test Output a square wave with the specified frequency, amplitude, and dc offset. This command overrides the current duty cycle setting and automatically selects 50%. The waveform is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_square()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_apply_user(self, instrument):
        # Test Output the arbitrary waveform currently selected by the FUNC:USER command. The waveform is output using the specified frequency, amplitude, and dc offset. The waveform is output as soon as the command is executed. 

        # Call the method
        instrument.set_apply_user()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibrate_all(self, instrument):
        # Test Perform a calibration of the instrument using the specified calibration value (CAL:VAL command). Before you can calibrate the function generator, you must unsecure it by entering the correct security code. 

        # Call the method
        result = instrument.get_calibrate_all()

        # Verify the response is not None
        assert result is not None

    def test_get_calibrate_count(self, instrument):
        # Test Query the instrument to determine the number of times it has been calibrated. 

        # Call the method
        result = instrument.get_calibrate_count()

        # Verify the response is not None
        assert result is not None

    def test_set_calibrate_secure_code(self, instrument):
        # Test Enter a new security code. To change the security code, you must first unsecure the function generator using the old security code, and then enter a new code. The security code is stored in non-volatile memory. 

        # Call the method
        instrument.set_calibrate_secure_code()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibrate_secure_state(self, instrument):
        # Test Unsecure or secure the instrument for calibration. 

        # Call the method
        result = instrument.get_calibrate_secure_state()

        # Verify the response is not None
        assert result is not None

    def test_set_calibrate_secure_state(self, instrument):
        # Test Unsecure or secure the instrument for calibration. 

        # Call the method
        instrument.set_calibrate_secure_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibrate_setup(self, instrument):
        # Test Configure the function generator's internal state for each of the calibration steps to be performed. 

        # Call the method
        result = instrument.get_calibrate_setup()

        # Verify the response is not None
        assert result is not None

    def test_set_calibrate_setup(self, instrument):
        # Test Configure the function generator's internal state for each of the calibration steps to be performed. 

        # Call the method
        instrument.set_calibrate_setup()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibrate_string(self, instrument):
        # Test Store a message in non-volatile calibration memory. Storing a message will overwrite any message previously stored in memory. 

        # Call the method
        result = instrument.get_calibrate_string()

        # Verify the response is not None
        assert result is not None

    def test_set_calibrate_string(self, instrument):
        # Test Store a message in non-volatile calibration memory. Storing a message will overwrite any message previously stored in memory. 

        # Call the method
        instrument.set_calibrate_string()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibrate_value(self, instrument):
        # Test Specify the value of the known calibration signal as outlined in the calibration procedures in the Agilent 33250A Service Guide. 

        # Call the method
        result = instrument.get_calibrate_value()

        # Verify the response is not None
        assert result is not None

    def test_set_calibrate_value(self, instrument):
        # Test Specify the value of the known calibration signal as outlined in the calibration procedures in the Agilent 33250A Service Guide. 

        # Call the method
        instrument.set_calibrate_value()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_window_state(self, instrument):
        # Test Disable or enable the function generator front-panel display. When it is disabled, the front-panel display is blanked (however, the bulb used to backlight the display remains enabled). 

        # Call the method
        result = instrument.get_display_window_state()

        # Verify the response is not None
        assert result is not None

    def test_set_display_window_state(self, instrument):
        # Test Disable or enable the function generator front-panel display. When it is disabled, the front-panel display is blanked (however, the bulb used to backlight the display remains enabled). 

        # Call the method
        instrument.set_display_window_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_display_window_text_clear(self, instrument):
        # Test Clear the text message currently shown on the function generator's front-panel display. 

        # Call the method
        instrument.display_window_text_clear()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_window_text_data(self, instrument):
        # Test Display a text message on the function generator's front-panel display. Sending a text message to the display overrides the display state as set by the DISP command. 

        # Call the method
        result = instrument.get_display_window_text_data()

        # Verify the response is not None
        assert result is not None

    def test_set_display_window_text_data(self, instrument):
        # Test Display a text message on the function generator's front-panel display. Sending a text message to the display overrides the display state as set by the DISP command. 

        # Call the method
        instrument.set_display_window_text_data()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_format_border(self, instrument):
        # Test Used for binary block transfers only. Select the byte order for binary transfers in the block mode using the DATA:DAC command. 

        # Call the method
        result = instrument.get_format_border()

        # Verify the response is not None
        assert result is not None

    def test_set_format_border(self, instrument):
        # Test Used for binary block transfers only. Select the byte order for binary transfers in the block mode using the DATA:DAC command. 

        # Call the method
        instrument.set_format_border()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_nstates(self, instrument):
        # Test Query the total number of memory locations available for state storage. 

        # Call the method
        result = instrument.get_memory_nstates()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_delete(self, instrument):
        # Test Delete the contents of the specified storage location. If you have assigned a user-defined name to a location (MEM:STAT:NAME command), this command also removes the name that you assigned and restores the default name ("AUTO_RECALL", "STATE_1", "STATE_2", etc.). 

        # Call the method
        instrument.set_memory_state_delete()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_name(self, instrument):
        # Test Assign a custom name to the specified storage location.

        # Call the method
        result = instrument.get_memory_state_name()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_name(self, instrument):
        # Test Assign a custom name to the specified storage location.

        # Call the method
        instrument.set_memory_state_name()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_recall_auto(self, instrument):
        # Test Disable or enable the automatic recall of the power-down state from storage location "0" when power is turned on. 

        # Call the method
        result = instrument.get_memory_state_recall_auto()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_recall_auto(self, instrument):
        # Test Disable or enable the automatic recall of the power-down state from storage location "0" when power is turned on. 

        # Call the method
        instrument.set_memory_state_recall_auto()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_valid(self, instrument):
        # Test Query the specified storage location to determine if a valid state is currently stored in that location. 

        # Call the method
        result = instrument.get_memory_state_valid()

        # Verify the response is not None
        assert result is not None

    def test_get_output_load(self, instrument):
        # Test Select the desired output termination (i.e., the impedance of the load attached to the output of the Agilent 33250A). The specified value is used for amplitude, offset, and high/low level settings. 

        # Call the method
        result = instrument.get_output_load()

        # Verify the response is not None
        assert result is not None

    def test_set_output_load(self, instrument):
        # Test Select the desired output termination (i.e., the impedance of the load attached to the output of the Agilent 33250A). The specified value is used for amplitude, offset, and high/low level settings. 

        # Call the method
        instrument.set_output_load()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_polarity(self, instrument):
        # Test Invert the waveform relative to the offset voltage. In the normal mode (default), the waveform goes positive during the first part of the cycle. In the inverted mode, the waveform goes negative during the first part of the cycle. 

        # Call the method
        result = instrument.get_output_polarity()

        # Verify the response is not None
        assert result is not None

    def test_set_output_polarity(self, instrument):
        # Test Invert the waveform relative to the offset voltage. In the normal mode (default), the waveform goes positive during the first part of the cycle. In the inverted mode, the waveform goes negative during the first part of the cycle. 

        # Call the method
        instrument.set_output_polarity()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_state(self, instrument):
        # Test Disable or enable the front-panel Output connector. The default is "OFF". 

        # Call the method
        result = instrument.get_output_state()

        # Verify the response is not None
        assert result is not None

    def test_set_output_state(self, instrument):
        # Test Disable or enable the front-panel Output connector. The default is "OFF". 

        # Call the method
        instrument.set_output_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_state(self, instrument):
        # Test Disable or enable the front-panel Sync connector. At lower amplitudes, you can reduce output distortion by disabling the Sync signal. 

        # Call the method
        result = instrument.get_output_sync_state()

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_state(self, instrument):
        # Test Disable or enable the front-panel Sync connector. At lower amplitudes, you can reduce output distortion by disabling the Sync signal. 

        # Call the method
        instrument.set_output_sync_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger_slope(self, instrument):
        # Test Select a rising or falling edge for the "trigger out" signal. When enabled using the OUTP:TRIG command (see below), a TTL-compatible square waveform with the specified edge is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 

        # Call the method
        result = instrument.get_output_trigger_slope()

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger_slope(self, instrument):
        # Test Select a rising or falling edge for the "trigger out" signal. When enabled using the OUTP:TRIG command (see below), a TTL-compatible square waveform with the specified edge is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 

        # Call the method
        instrument.set_output_trigger_slope()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger_state(self, instrument):
        # Test Disable or enable the "trigger out" signal (used for sweep and burst only). When enabled, a TTL-compatible square waveform with the specified edge (OUTP:TRIG:SLOP command) is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 

        # Call the method
        result = instrument.get_output_trigger_state()

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger_state(self, instrument):
        # Test Disable or enable the "trigger out" signal (used for sweep and burst only). When enabled, a TTL-compatible square waveform with the specified edge (OUTP:TRIG:SLOP command) is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 

        # Call the method
        instrument.set_output_trigger_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_depth(self, instrument):
        # Test Set the internal modulation depth (or "percent modulation") in percent. 

        # Call the method
        result = instrument.get_source_am_depth()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_depth(self, instrument):
        # Test Set the internal modulation depth (or "percent modulation") in percent. 

        # Call the method
        instrument.set_source_am_depth()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_internal_frequency(self, instrument):
        # Test Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 

        # Call the method
        result = instrument.get_source_am_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_internal_frequency(self, instrument):
        # Test Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 

        # Call the method
        instrument.set_source_am_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_internal_function_shape(self, instrument):
        # Test Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 

        # Call the method
        result = instrument.get_source_am_internal_function_shape()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_internal_function_shape(self, instrument):
        # Test Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 

        # Call the method
        instrument.set_source_am_internal_function_shape()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_source(self, instrument):
        # Test Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 

        # Call the method
        result = instrument.get_source_am_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_source(self, instrument):
        # Test Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 

        # Call the method
        instrument.set_source_am_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_state(self, instrument):
        # Test Disable or enable AM. To avoid multiple waveform changes, you can enable AM after you have set up the other modulation parameters. 

        # Call the method
        result = instrument.get_source_am_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_state(self, instrument):
        # Test Disable or enable AM. To avoid multiple waveform changes, you can enable AM after you have set up the other modulation parameters. 

        # Call the method
        instrument.set_source_am_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_gate_polarity(self, instrument):
        # Test Select whether the function generator uses true-high or true-low logic levels on the rear-panel Trig In connector for an externally-gated burst. 

        # Call the method
        result = instrument.get_source_burst_gate_polarity()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_gate_polarity(self, instrument):
        # Test Select whether the function generator uses true-high or true-low logic levels on the rear-panel Trig In connector for an externally-gated burst. 

        # Call the method
        instrument.set_source_burst_gate_polarity()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_internal_period(self, instrument):
        # Test Set the burst period for internally-triggered bursts. 

        # Call the method
        result = instrument.get_source_burst_internal_period()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_internal_period(self, instrument):
        # Test Set the burst period for internally-triggered bursts. 

        # Call the method
        instrument.set_source_burst_internal_period()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_mode(self, instrument):
        # Test Select the burst mode.

        # Call the method
        result = instrument.get_source_burst_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_mode(self, instrument):
        # Test Select the burst mode.

        # Call the method
        instrument.set_source_burst_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_ncycles(self, instrument):
        # Test Set the number of cycles to be output per burst (triggered burst mode only).

        # Call the method
        result = instrument.get_source_burst_ncycles()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_ncycles(self, instrument):
        # Test Set the number of cycles to be output per burst (triggered burst mode only).

        # Call the method
        instrument.set_source_burst_ncycles()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_phase(self, instrument):
        # Test Set the starting phase for the burst in degrees or radians as specified by the previous UNIT:ANGL command. 

        # Call the method
        result = instrument.get_source_burst_phase()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_phase(self, instrument):
        # Test Set the starting phase for the burst in degrees or radians as specified by the previous UNIT:ANGL command. 

        # Call the method
        instrument.set_source_burst_phase()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_state(self, instrument):
        # Test Disable or enable the burst mode. 

        # Call the method
        result = instrument.get_source_burst_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_state(self, instrument):
        # Test Disable or enable the burst mode. 

        # Call the method
        instrument.set_source_burst_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_deviation(self, instrument):
        # Test Set the peak frequency deviation in hertz. This value represents the peak variation in frequency of the modulated waveform from the carrier frequency. 

        # Call the method
        result = instrument.get_source_fm_deviation()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_deviation(self, instrument):
        # Test Set the peak frequency deviation in hertz. This value represents the peak variation in frequency of the modulated waveform from the carrier frequency. 

        # Call the method
        instrument.set_source_fm_deviation()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_internal_frequency(self, instrument):
        # Test Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 

        # Call the method
        result = instrument.get_source_fm_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_internal_frequency(self, instrument):
        # Test Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 

        # Call the method
        instrument.set_source_fm_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_internal_function_shape(self, instrument):
        # Test Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 

        # Call the method
        result = instrument.get_source_fm_internal_function_shape()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_internal_function_shape(self, instrument):
        # Test Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 

        # Call the method
        instrument.set_source_fm_internal_function_shape()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_source(self, instrument):
        # Test Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 

        # Call the method
        result = instrument.get_source_fm_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_source(self, instrument):
        # Test Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 

        # Call the method
        instrument.set_source_fm_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_state(self, instrument):
        # Test Disable or enable FM. To avoid multiple waveform changes, you can enable FM after you have set up the other modulation parameters. 

        # Call the method
        result = instrument.get_source_fm_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_state(self, instrument):
        # Test Disable or enable FM. To avoid multiple waveform changes, you can enable FM after you have set up the other modulation parameters. 

        # Call the method
        instrument.set_source_fm_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_center(self, instrument):
        # Test Set the center frequency (used in conjunction with the frequency span). 

        # Call the method
        result = instrument.get_source_frequency_center()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_center(self, instrument):
        # Test Set the center frequency (used in conjunction with the frequency span). 

        # Call the method
        instrument.set_source_frequency_center()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_cw(self, instrument):
        # Test Set the output frequency. 

        # Call the method
        result = instrument.get_source_frequency_cw()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_cw(self, instrument):
        # Test Set the output frequency. 

        # Call the method
        instrument.set_source_frequency_cw()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_span(self, instrument):
        # Test Set the frequency span (used in conjunction with the center frequency). 

        # Call the method
        result = instrument.get_source_frequency_span()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_span(self, instrument):
        # Test Set the frequency span (used in conjunction with the center frequency). 

        # Call the method
        instrument.set_source_frequency_span()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_start(self, instrument):
        # Test Set the start frequency (used in conjunction with the stop frequency). 

        # Call the method
        result = instrument.get_source_frequency_start()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_start(self, instrument):
        # Test Set the start frequency (used in conjunction with the stop frequency). 

        # Call the method
        instrument.set_source_frequency_start()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_stop(self, instrument):
        # Test Set the stop frequency (used in conjunction with the start frequency).

        # Call the method
        result = instrument.get_source_frequency_stop()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_stop(self, instrument):
        # Test Set the stop frequency (used in conjunction with the start frequency).

        # Call the method
        instrument.set_source_frequency_stop()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_frequency(self, instrument):
        # Test Set the FSK alternate (or "hop") frequency. 

        # Call the method
        result = instrument.get_source_fskey_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_frequency(self, instrument):
        # Test Set the FSK alternate (or "hop") frequency. 

        # Call the method
        instrument.set_source_fskey_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_internal_rate(self, instrument):
        # Test Set the rate at which the output frequency "shifts" between the carrier and hop frequency. 

        # Call the method
        result = instrument.get_source_fskey_internal_rate()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_internal_rate(self, instrument):
        # Test Set the rate at which the output frequency "shifts" between the carrier and hop frequency. 

        # Call the method
        instrument.set_source_fskey_internal_rate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_source(self, instrument):
        # Test Select an internal or external FSK source. 

        # Call the method
        result = instrument.get_source_fskey_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_source(self, instrument):
        # Test Select an internal or external FSK source. 

        # Call the method
        instrument.set_source_fskey_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_state(self, instrument):
        # Test Disable or enable FSK modulation. To avoid multiple waveform changes, you can enable FSK after you have set up the other modulation parameters. 

        # Call the method
        result = instrument.get_source_fskey_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_state(self, instrument):
        # Test Disable or enable FSK modulation. To avoid multiple waveform changes, you can enable FSK after you have set up the other modulation parameters. 

        # Call the method
        instrument.set_source_fskey_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_shape(self, instrument):
        # Test Select the output function. The selected waveform is output using the previously selected frequency, amplitude, and offset voltage settings. 

        # Call the method
        result = instrument.get_source_function_shape()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_shape(self, instrument):
        # Test Select the output function. The selected waveform is output using the previously selected frequency, amplitude, and offset voltage settings. 

        # Call the method
        instrument.set_source_function_shape()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_shape_ramp_symmetry(self, instrument):
        # Test Set the symmetry percentage for ramp waves. Symmetry represents the amount of time per cycle that the ramp wave is rising (assuming that the waveform polarity is not inverted). 

        # Call the method
        result = instrument.get_source_function_shape_ramp_symmetry()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_shape_ramp_symmetry(self, instrument):
        # Test Set the symmetry percentage for ramp waves. Symmetry represents the amount of time per cycle that the ramp wave is rising (assuming that the waveform polarity is not inverted). 

        # Call the method
        instrument.set_source_function_shape_ramp_symmetry()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_shape_square_dcycle(self, instrument):
        # Test Set the duty cycle percentage for square waves. Duty cycle represents the amount of time per cycle that the square wave is at a high level (assuming that the waveform polarity is not inverted). 

        # Call the method
        result = instrument.get_source_function_shape_square_dcycle()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_shape_square_dcycle(self, instrument):
        # Test Set the duty cycle percentage for square waves. Duty cycle represents the amount of time per cycle that the square wave is at a high level (assuming that the waveform polarity is not inverted). 

        # Call the method
        instrument.set_source_function_shape_square_dcycle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_shape_user(self, instrument):
        # Test Select one of the five built-in arbitrary waveforms, one of four user-defined waveforms, or the waveform currently downloaded to volatile memory. 

        # Call the method
        result = instrument.get_source_function_shape_user()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_shape_user(self, instrument):
        # Test Select one of the five built-in arbitrary waveforms, one of four user-defined waveforms, or the waveform currently downloaded to volatile memory. 

        # Call the method
        instrument.set_source_function_shape_user()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_marker_frequency(self, instrument):
        # Test Set the marker frequency. This is the frequency at which the signal on the front-panel Sync connector goes to a logic low during the sweep. The Sync signal always goes from low to high at the beginning of the sweep. 

        # Call the method
        result = instrument.get_source_marker_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_frequency(self, instrument):
        # Test Set the marker frequency. This is the frequency at which the signal on the front-panel Sync connector goes to a logic low during the sweep. The Sync signal always goes from low to high at the beginning of the sweep. 

        # Call the method
        instrument.set_source_marker_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_marker_state(self, instrument):
        # Test Disable or enable the frequency marker. When the frequency marker is disabled, the signal output from the Sync connector is the normal Sync signal for the carrier waveform.

        # Call the method
        result = instrument.get_source_marker_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_state(self, instrument):
        # Test Disable or enable the frequency marker. When the frequency marker is disabled, the signal output from the Sync connector is the normal Sync signal for the carrier waveform.

        # Call the method
        instrument.set_source_marker_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_phase_adjust(self, instrument):
        # Test Adjust the phase offset of the output waveform in degrees or radians as specified by the previous UNIT:ANGL command 

        # Call the method
        result = instrument.get_source_phase_adjust()

        # Verify the response is not None
        assert result is not None

    def test_set_source_phase_adjust(self, instrument):
        # Test Adjust the phase offset of the output waveform in degrees or radians as specified by the previous UNIT:ANGL command 

        # Call the method
        instrument.set_source_phase_adjust()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_phase_reference(self, instrument):
        # Test Immediately sets a new zero-phase reference point without changing the output of the function generator. That is, this command resets the phase value returned by the PHAS? command but does not affect the output waveform.

        # Call the method
        instrument.source_phase_reference()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_phase_unlock_error_state(self, instrument):
        # Test Disable or enable the function generator from generating an error if the phase-lock is ever lost. 

        # Call the method
        result = instrument.get_source_phase_unlock_error_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_phase_unlock_error_state(self, instrument):
        # Test Disable or enable the function generator from generating an error if the phase-lock is ever lost. 

        # Call the method
        instrument.set_source_phase_unlock_error_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pulse_period(self, instrument):
        # Test Set the period for pulses. 

        # Call the method
        result = instrument.get_source_pulse_period()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pulse_period(self, instrument):
        # Test Set the period for pulses. 

        # Call the method
        instrument.set_source_pulse_period()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pulse_width(self, instrument):
        # Test Set the pulse width in seconds. 

        # Call the method
        result = instrument.get_source_pulse_width()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pulse_width(self, instrument):
        # Test Set the pulse width in seconds. 

        # Call the method
        instrument.set_source_pulse_width()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_spacing(self, instrument):
        # Test Select linear or logarithmic spacing for the sweep. 

        # Call the method
        result = instrument.get_source_sweep_spacing()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_spacing(self, instrument):
        # Test Select linear or logarithmic spacing for the sweep. 

        # Call the method
        instrument.set_source_sweep_spacing()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_state(self, instrument):
        # Test Disable or enable the sweep mode. To avoid multiple waveform changes, you can enable the sweep mode after you have set up the other sweep parameters. 

        # Call the method
        result = instrument.get_source_sweep_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_state(self, instrument):
        # Test Disable or enable the sweep mode. To avoid multiple waveform changes, you can enable the sweep mode after you have set up the other sweep parameters. 

        # Call the method
        instrument.set_source_sweep_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_time(self, instrument):
        # Test Set the number of seconds required to sweep from the start frequency to the stop frequency. 

        # Call the method
        result = instrument.get_source_sweep_time()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_time(self, instrument):
        # Test Set the number of seconds required to sweep from the start frequency to the stop frequency. 

        # Call the method
        instrument.set_source_sweep_time()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_level_immediate_amplitude(self, instrument):
        # Test Set the output amplitude. The default amplitude is 100 mVpp (into 50W) for all functions.

        # Call the method
        result = instrument.get_source_voltage_level_immediate_amplitude()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_level_immediate_amplitude(self, instrument):
        # Test Set the output amplitude. The default amplitude is 100 mVpp (into 50W) for all functions.

        # Call the method
        instrument.set_source_voltage_level_immediate_amplitude()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_level_immediate_high(self, instrument):
        # Test Set the high voltage level. 

        # Call the method
        result = instrument.get_source_voltage_level_immediate_high()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_level_immediate_high(self, instrument):
        # Test Set the high voltage level. 

        # Call the method
        instrument.set_source_voltage_level_immediate_high()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_level_immediate_low(self, instrument):
        # Test Set the low voltage level.

        # Call the method
        result = instrument.get_source_voltage_level_immediate_low()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_level_immediate_low(self, instrument):
        # Test Set the low voltage level.

        # Call the method
        instrument.set_source_voltage_level_immediate_low()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_level_immediate_offset(self, instrument):
        # Test Set the dc offset voltage. 

        # Call the method
        result = instrument.get_source_voltage_level_immediate_offset()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_level_immediate_offset(self, instrument):
        # Test Set the dc offset voltage. 

        # Call the method
        instrument.set_source_voltage_level_immediate_offset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_level_immediate_unit_voltage(self, instrument):
        # Test Select the units for output amplitude (does not affect offset voltage or high/low levels).

        # Call the method
        result = instrument.get_source_voltage_level_immediate_unit_voltage()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_level_immediate_unit_voltage(self, instrument):
        # Test Select the units for output amplitude (does not affect offset voltage or high/low levels).

        # Call the method
        instrument.set_source_voltage_level_immediate_unit_voltage()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_range_auto(self, instrument):
        # Test Disable or enable voltage autoranging for all functions. In the default mode, autoranging is enabled ("ON") and the function generator automatically selects the optimal settings for the output amplifier and attenuators. 

        # Call the method
        result = instrument.get_source_voltage_range_auto()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_range_auto(self, instrument):
        # Test Disable or enable voltage autoranging for all functions. In the default mode, autoranging is enabled ("ON") and the function generator automatically selects the optimal settings for the output amplifier and attenuators. 

        # Call the method
        instrument.set_source_voltage_range_auto()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_questionable_condition(self, instrument):
        # Test Query the condition register in this group. This is a read-only register and bits are not cleared when you read the register. 

        # Call the method
        result = instrument.get_status_questionable_condition()

        # Verify the response is not None
        assert result is not None

    def test_get_status_questionable_enable(self, instrument):
        # Test Enable bits in the enable register in this register group. 

        # Call the method
        result = instrument.get_status_questionable_enable()

        # Verify the response is not None
        assert result is not None

    def test_set_status_questionable_enable(self, instrument):
        # Test Enable bits in the enable register in this register group. 

        # Call the method
        instrument.set_status_questionable_enable()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_questionable_event(self, instrument):
        # Test Query the event register in this register group. 

        # Call the method
        result = instrument.get_status_questionable_event()

        # Verify the response is not None
        assert result is not None

    def test_status_preset(self, instrument):
        # Test Clear all bits in the Questionable Data enable register and the Standard Operation enable register. 

        # Call the method
        instrument.status_preset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_system_beeper_immediate(self, instrument):
        # Test Issue a single beep immediately. 

        # Call the method
        instrument.system_beeper_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_beeper_state(self, instrument):
        # Test Disable or enable the tone heard when an error is generated from the front-panel or over the remote interface. The current selection is stored in non-volatile memory. 

        # Call the method
        result = instrument.get_system_beeper_state()

        # Verify the response is not None
        assert result is not None

    def test_set_system_beeper_state(self, instrument):
        # Test Disable or enable the tone heard when an error is generated from the front-panel or over the remote interface. The current selection is stored in non-volatile memory. 

        # Call the method
        instrument.set_system_beeper_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_error_next(self, instrument):
        # Test Read and clear one error from the function generator's error queue. A record of up to 20 command syntax or hardware errors can be stored in the error queue.

        # Call the method
        result = instrument.get_system_error_next()

        # Verify the response is not None
        assert result is not None

    def test_system_local(self, instrument):
        # Test Sets the instrument state to local (the normal power-on default state). Removes any annunciator and unlocks the front panel keyboard. 

        # Call the method
        instrument.system_local()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_system_rwlock(self, instrument):
        # Test Sets the instrument state to remote with lock. Displays the rwl annunciator and locks the keyboard.

        # Call the method
        instrument.system_rwlock()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_version(self, instrument):
        # Test Query the function generator to determine the present SCPI version. 

        # Call the method
        result = instrument.get_system_version()

        # Verify the response is not None
        assert result is not None

    def test_get_data_attribute_average(self, instrument):
        # Test Query the arithmetic average of all data points for the specified arbitrary waveform. 

        # Call the method
        result = instrument.get_data_attribute_average()

        # Verify the response is not None
        assert result is not None

    def test_get_data_attribute_cfactor(self, instrument):
        # Test Query the crest factor of all data points for the specified arbitrary waveform. Crest factor is the ratio of the peak value to the RMS value of the waveform. 

        # Call the method
        result = instrument.get_data_attribute_cfactor()

        # Verify the response is not None
        assert result is not None

    def test_get_data_attribute_points(self, instrument):
        # Test Query the number of points in the specified arbitrary waveform. 

        # Call the method
        result = instrument.get_data_attribute_points()

        # Verify the response is not None
        assert result is not None

    def test_get_data_attribute_ptpeak(self, instrument):
        # Test Query the peak-to-peak value of all data points for the specified arbitrary waveform. 

        # Call the method
        result = instrument.get_data_attribute_ptpeak()

        # Verify the response is not None
        assert result is not None

    def test_get_data_catalog(self, instrument):
        # Test List the names of all waveforms currently available for selection. 

        # Call the method
        result = instrument.get_data_catalog()

        # Verify the response is not None
        assert result is not None

    def test_set_data_copy(self, instrument):
        # Test Copy the waveform from volatile memory to the specified name in 
non-volatile memory. 

        # Call the method
        instrument.set_data_copy()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_data_data(self, instrument):
        # Test Download floating-point values from -1 to +1 into volatile memory. You can download from 1 to 65,536 (64K) points per waveform. The function generator takes the specified number of points and expands them to fill waveform memory. 

        # Call the method
        instrument.set_data_data()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_data_data_dac_valuelist(self, instrument):
        # Test Download binary or decimal integer values from -8191 to +8191 into volatile memory.  with ValueList syntax

        # Call the method with ValueList syntax
        instrument.set_data_data_dac(syntax=syntax.VALUELIST)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_data_data_dac_binaryblock(self, instrument):
        # Test Download binary or decimal integer values from -8191 to +8191 into volatile memory.  with BinaryBlock syntax

        # Call the method with BinaryBlock syntax
        instrument.set_data_data_dac(syntax=syntax.BINARYBLOCK)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_data_delete_all(self, instrument):
        # Test Delete all user-defined arbitrary waveforms from memory. This command deletes the waveform in volatile memory and all user-defined waveforms in non-volatile memory. The five built-in waveforms in non-volatile memory are not deleted. 

        # Call the method
        instrument.data_delete_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_data_delete_name(self, instrument):
        # Test Delete the specified arbitrary waveform from memory. You can delete the waveform in volatile memory or any of the four user-defined waveforms in non-volatile memory. 

        # Call the method
        instrument.set_data_delete_name()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_data_nvolatile_catalog(self, instrument):
        # Test List the names of all user-defined arbitrary waveforms downloaded to non-volatile memory. Returns the names of up to four waveforms. 

        # Call the method
        result = instrument.get_data_nvolatile_catalog()

        # Verify the response is not None
        assert result is not None

    def test_get_data_nvolatile_free(self, instrument):
        # Test Query the number of non-volatile memory slots available to store user-defined waveforms. Returns the number of memory slots available to store user-defined waveforms.

        # Call the method
        result = instrument.get_data_nvolatile_free()

        # Verify the response is not None
        assert result is not None

    def test_get_trigger_sequence_delay(self, instrument):
        # Test Insert a time delay between the receipt of the trigger and the start of the burst waveform 

        # Call the method
        result = instrument.get_trigger_sequence_delay()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_sequence_delay(self, instrument):
        # Test Insert a time delay between the receipt of the trigger and the start of the burst waveform 

        # Call the method
        instrument.set_trigger_sequence_delay()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_trigger_sequence_immediate(self, instrument):
        # Test Trigger a sweep or burst from the remote interface. This command can be used with any of the available trigger sources (TRIG:SOUR command). 

        # Call the method
        instrument.trigger_sequence_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_sequence_slope(self, instrument):
        # Test Select whether the function generator uses the rising edge or falling edge of the trigger signal on the rear-panel Trig In connector. 

        # Call the method
        result = instrument.get_trigger_sequence_slope()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_sequence_slope(self, instrument):
        # Test Select whether the function generator uses the rising edge or falling edge of the trigger signal on the rear-panel Trig In connector. 

        # Call the method
        instrument.set_trigger_sequence_slope()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_sequence_source(self, instrument):
        # Test Select the source from which the function generator will accept a trigger. 

        # Call the method
        result = instrument.get_trigger_sequence_source()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_sequence_source(self, instrument):
        # Test Select the source from which the function generator will accept a trigger. 

        # Call the method
        instrument.set_trigger_sequence_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_unit_angle(self, instrument):
        # Test Select degrees or radians to set the phase offset value using the PHAS command (remote interface only). 

        # Call the method
        result = instrument.get_unit_angle()

        # Verify the response is not None
        assert result is not None

    def test_set_unit_angle(self, instrument):
        # Test Select degrees or radians to set the phase offset value using the PHAS command (remote interface only). 

        # Call the method
        instrument.set_unit_angle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters
