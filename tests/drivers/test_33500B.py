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
        # Test Clears the event registers in all register groups. Also clears the error queue.

        # Call the method
        instrument.cls()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_ese(self, instrument):
        # Test Enables bits in the enable register for the Standard Event Register group.

        # Call the method
        result = instrument.get_ese()

        # Verify the response is not None
        assert result is not None

    def test_set_ese(self, instrument):
        # Test Enables bits in the enable register for the Standard Event Register group.

        # Call the method
        instrument.set_ese()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_esr(self, instrument):
        # Test Standard Event Status Register Query. Queries the event register for the Standard Event Register group. 

        # Call the method
        result = instrument.get_esr()

        # Verify the response is not None
        assert result is not None

    def test_get_idn(self, instrument):
        # Test instrument’s identification string.

        # Call the method
        result = instrument.get_idn()

        # Verify the response is not None
        assert result is not None

    def test_get_opc(self, instrument):
        # Test Sets "Operation Complete" (bit 0) in the Standard Event register at the completion of the current operation. Returns 1 to the output buffer after all pending commands complete.

        # Call the method
        result = instrument.get_opc()

        # Verify the response is not None
        assert result is not None

    def test_opc(self, instrument):
        # Test Sets "Operation Complete" (bit 0) in the Standard Event register at the completion of the current operation. Returns 1 to the output buffer after all pending commands complete.

        # Call the method
        instrument.opc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_opt(self, instrument):
        # Test Returns a quoted string identifying any installed options.

        # Call the method
        result = instrument.get_opt()

        # Verify the response is not None
        assert result is not None

    def test_get_psc(self, instrument):
        # Test Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.

        # Call the method
        result = instrument.get_psc()

        # Verify the response is not None
        assert result is not None

    def test_set_psc(self, instrument):
        # Test Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.

        # Call the method
        instrument.set_psc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_rcl(self, instrument):
        # Test Recalls (*RCL) instrument state in specified non-volatile location.

        # Call the method
        instrument.set_rcl()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_rst(self, instrument):
        # Test Resets instrument to factory default state.

        # Call the method
        instrument.rst()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_sav(self, instrument):
        # Test saves (*SAV) instrument state in specified non-volatile location. 

        # Call the method
        instrument.set_sav()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_sre(self, instrument):
        # Test Service Request Enable. This command enables bits in the enable register for the Status Byte Register group.

        # Call the method
        result = instrument.get_sre()

        # Verify the response is not None
        assert result is not None

    def test_set_sre(self, instrument):
        # Test Service Request Enable. This command enables bits in the enable register for the Status Byte Register group.

        # Call the method
        instrument.set_sre()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_stb(self, instrument):
        # Test Read Status Byte Query. This command queries the condition register for the Status Byte Register group.

        # Call the method
        result = instrument.get_stb()

        # Verify the response is not None
        assert result is not None

    def test_trg(self, instrument):
        # Test Trigger Command. Triggers a sweep, burst, arbitrary waveform advance, or LIST advance from the remote interface if the bus (software) trigger source is currently selected.

        # Call the method
        instrument.trg()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_tst(self, instrument):
        # Test Self-Test Query. Performs a complete instrument self-test.

        # Call the method
        result = instrument.get_tst()

        # Verify the response is not None
        assert result is not None

    def test_wai(self, instrument):
        # Test Configures the instrument to wait for all pending operations to complete before executing any additional commands over the interface.

        # Call the method
        instrument.wai()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_abort(self, instrument):
        # Test Halts a sequence, list, sweep, or burst, even an infinite burst. 

        # Call the method
        instrument.abort()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_all(self, instrument):
        # Test Performs a calibration using the calibration value (CALibration:VALue). 

        # Call the method
        result = instrument.get_calibration_all()

        # Verify the response is not None
        assert result is not None

    def test_get_calibration_count(self, instrument):
        # Test Returns the number of calibrations performed.

        # Call the method
        result = instrument.get_calibration_count()

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_secure_code(self, instrument):
        # Test Sets the security code to prevent unauthorized calibrations.

        # Call the method
        instrument.set_calibration_secure_code()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_secure_state(self, instrument):
        # Test Unsecures or secures the instrument for calibration. 

        # Call the method
        result = instrument.get_calibration_secure_state()

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_secure_state(self, instrument):
        # Test Unsecures or secures the instrument for calibration. 

        # Call the method
        instrument.set_calibration_secure_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_setup(self, instrument):
        # Test Configures the calibration step (default 1) to be performed. 

        # Call the method
        result = instrument.get_calibration_setup()

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_setup(self, instrument):
        # Test Configures the calibration step (default 1) to be performed. 

        # Call the method
        instrument.set_calibration_setup()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_string(self, instrument):
        # Test Stores a message of up to 40 characters in calibration memory.

        # Call the method
        result = instrument.get_calibration_string()

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_string(self, instrument):
        # Test Stores a message of up to 40 characters in calibration memory.

        # Call the method
        instrument.set_calibration_string()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_value(self, instrument):
        # Test Specifies the value of the known calibration signal.

        # Call the method
        result = instrument.get_calibration_value()

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_value(self, instrument):
        # Test Specifies the value of the known calibration signal.

        # Call the method
        instrument.set_calibration_value()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display(self, instrument):
        # Test Disables or enables the front-panel display.

        # Call the method
        result = instrument.get_display()

        # Verify the response is not None
        assert result is not None

    def test_set_display(self, instrument):
        # Test Disables or enables the front-panel display.

        # Call the method
        instrument.set_display()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_focus(self, instrument):
        # Test selects the channel displayed "in front" on a two-channel instrument 

        # Call the method
        result = instrument.get_display_focus()

        # Verify the response is not None
        assert result is not None

    def test_set_display_focus(self, instrument):
        # Test selects the channel displayed "in front" on a two-channel instrument 

        # Call the method
        instrument.set_display_focus()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_text(self, instrument):
        # Test Displays a text message on the front-panel display.   

        # Call the method
        result = instrument.get_display_text()

        # Verify the response is not None
        assert result is not None

    def test_set_display_text(self, instrument):
        # Test Displays a text message on the front-panel display.   

        # Call the method
        instrument.set_display_text()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_display_text_clear(self, instrument):
        # Test Clears the text message from the front-panel display.

        # Call the method
        instrument.display_text_clear()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_arbrate(self, instrument):
        # Test Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).

        # Call the method
        result = instrument.get_display_unit_arbrate()

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_arbrate(self, instrument):
        # Test Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).

        # Call the method
        instrument.set_display_unit_arbrate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_pulse(self, instrument):
        # Test Selects the method for specifying pulse duration.

        # Call the method
        result = instrument.get_display_unit_pulse()

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_pulse(self, instrument):
        # Test Selects the method for specifying pulse duration.

        # Call the method
        instrument.set_display_unit_pulse()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_rate(self, instrument):
        # Test Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).

        # Call the method
        result = instrument.get_display_unit_rate()

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_rate(self, instrument):
        # Test Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).

        # Call the method
        instrument.set_display_unit_rate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_sweep(self, instrument):
        # Test Selects the method for specifying sweep frequency range.

        # Call the method
        result = instrument.get_display_unit_sweep()

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_sweep(self, instrument):
        # Test Selects the method for specifying sweep frequency range.

        # Call the method
        instrument.set_display_unit_sweep()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_voltage(self, instrument):
        # Test Selects the method for specifying voltage ranges.

        # Call the method
        result = instrument.get_display_unit_voltage()

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_voltage(self, instrument):
        # Test Selects the method for specifying voltage ranges.

        # Call the method
        instrument.set_display_unit_voltage()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_view(self, instrument):
        # Test Selects the screen layout.

        # Call the method
        result = instrument.get_display_view()

        # Verify the response is not None
        assert result is not None

    def test_set_display_view(self, instrument):
        # Test Selects the screen layout.

        # Call the method
        instrument.set_display_view()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_format_border(self, instrument):
        # Test Sets the byte order used in binary data point transfers in the block mode.

        # Call the method
        result = instrument.get_format_border()

        # Verify the response is not None
        assert result is not None

    def test_set_format_border(self, instrument):
        # Test Sets the byte order used in binary data point transfers in the block mode.

        # Call the method
        instrument.set_format_border()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_hcopy_sdump_data(self, instrument):
        # Test Returns the front panel display image ("screen shot")

        # Call the method
        result = instrument.get_hcopy_sdump_data()

        # Verify the response is not None
        assert result is not None

    def test_get_hcopy_sdump_data_format(self, instrument):
        # Test Specifies the image format for images returned by HCOPy:SDUMp:DATA?.

        # Call the method
        result = instrument.get_hcopy_sdump_data_format()

        # Verify the response is not None
        assert result is not None

    def test_set_hcopy_sdump_data_format(self, instrument):
        # Test Specifies the image format for images returned by HCOPy:SDUMp:DATA?.

        # Call the method
        instrument.set_hcopy_sdump_data_format()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_initiate_continuous(self, instrument):
        # Test Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        # Call the method
        result = instrument.get_initiate_continuous()

        # Verify the response is not None
        assert result is not None

    def test_set_initiate_continuous(self, instrument):
        # Test Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        # Call the method
        instrument.set_initiate_continuous()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_initiate_continuous_all(self, instrument):
        # Test Specifies whether the trigger system for both channels (ALL) always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        # Call the method
        instrument.set_initiate_continuous_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_initiate_immediate(self, instrument):
        # Test Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt.

        # Call the method
        instrument.initiate_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_initiate_immediate_all(self, instrument):
        # Test Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt

        # Call the method
        instrument.initiate_immediate_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_identify_state(self, instrument):
        # Test Turns the LXI Identify Indicator on the display on or off.

        # Call the method
        result = instrument.get_lxi_identify_state()

        # Verify the response is not None
        assert result is not None

    def test_set_lxi_identify_state(self, instrument):
        # Test Turns the LXI Identify Indicator on the display on or off.

        # Call the method
        instrument.set_lxi_identify_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_mdns_enable(self, instrument):
        # Test Disables or enables the Multicast Domain Name System (mDNS).

        # Call the method
        result = instrument.get_lxi_mdns_enable()

        # Verify the response is not None
        assert result is not None

    def test_set_lxi_mdns_enable(self, instrument):
        # Test Disables or enables the Multicast Domain Name System (mDNS).

        # Call the method
        instrument.set_lxi_mdns_enable()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_mdns_hname_resolved(self, instrument):
        # Test Returns the resolved (unique) mDNS hostname in the form <mDNS Hostname>-N. 

        # Call the method
        result = instrument.get_lxi_mdns_hname_resolved()

        # Verify the response is not None
        assert result is not None

    def test_get_lxi_mdns_sname_desired(self, instrument):
        # Test Sets the desired mDNS service name.

        # Call the method
        result = instrument.get_lxi_mdns_sname_desired()

        # Verify the response is not None
        assert result is not None

    def test_set_lxi_mdns_sname_desired(self, instrument):
        # Test Sets the desired mDNS service name.

        # Call the method
        instrument.set_lxi_mdns_sname_desired()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_mdns_sname_resolved(self, instrument):
        # Test Returns the resolved (unique) mDNS service name in the form <Desired mDNS Service Name>(N). 

        # Call the method
        result = instrument.get_lxi_mdns_sname_resolved()

        # Verify the response is not None
        assert result is not None

    def test_lxi_reset(self, instrument):
        # Test Resets LAN settings to a known operating state, beginning with DHCP. 

        # Call the method
        instrument.lxi_reset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_lxi_restart(self, instrument):
        # Test Restarts the LAN with the current settings as specified by the SYSTem:COMM:LAN commands. 

        # Call the method
        instrument.lxi_restart()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_nstates(self, instrument):
        # Test Returns the total number of memory locations available for state storage 

        # Call the method
        result = instrument.get_memory_nstates()

        # Verify the response is not None
        assert result is not None

    def test_get_memory_state_catalog(self, instrument):
        # Test Returns the names assigned to locations 0 through 4.

        # Call the method
        result = instrument.get_memory_state_catalog()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_delete(self, instrument):
        # Test Deletes a state storage location.

        # Call the method
        instrument.set_memory_state_delete()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_name(self, instrument):
        # Test Names a storage location. 

        # Call the method
        result = instrument.get_memory_state_name()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_name(self, instrument):
        # Test Names a storage location. 

        # Call the method
        instrument.set_memory_state_name()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_recall_auto(self, instrument):
        # Test Disables or enables automatic recall of instrument state in storage location "0" at power on.

        # Call the method
        result = instrument.get_memory_state_recall_auto()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_recall_auto(self, instrument):
        # Test Disables or enables automatic recall of instrument state in storage location "0" at power on.

        # Call the method
        instrument.set_memory_state_recall_auto()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_valid(self, instrument):
        # Test Indicates whether a valid state is currently stored in a storage location.

        # Call the method
        result = instrument.get_memory_state_valid()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_catalog_all(self, instrument):
        # Test Returns a list of all files in the current mass storage directory, including internal storage and the USB drive.

        # Call the method
        result = instrument.get_mmemory_catalog_all()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_catalog_data_arbitrary(self, instrument):
        # Test Returns a list of all the arbitrary sequence (.seq) files and folders, as well as arbitrary waveform (.arb/.barb) files in a folder.

        # Call the method
        result = instrument.get_mmemory_catalog_data_arbitrary()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_catalog_state(self, instrument):
        # Test Lists all state files (.sta file extension) in a folder. 

        # Call the method
        result = instrument.get_mmemory_catalog_state()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_cdirectory(self, instrument):
        # Test MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        # Call the method
        result = instrument.get_mmemory_cdirectory()

        # Verify the response is not None
        assert result is not None

    def test_set_mmemory_cdirectory(self, instrument):
        # Test MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        # Call the method
        instrument.set_mmemory_cdirectory()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_copy(self, instrument):
        # Test Copies <file1> to <file2>. 

        # Call the method
        instrument.set_mmemory_copy()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_copy_sequence(self, instrument):
        # Test Copies a sequence from <source> to <destination>. 

        # Call the method
        instrument.set_mmemory_copy_sequence()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_delete(self, instrument):
        # Test Deletes a file. 

        # Call the method
        instrument.set_mmemory_delete()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_download_data(self, instrument):
        # Test Downloads data from the host computer to a file in the instrument.

        # Call the method
        instrument.set_mmemory_download_data()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_mmemory_download_fname(self, instrument):
        # Test Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        # Call the method
        result = instrument.get_mmemory_download_fname()

        # Verify the response is not None
        assert result is not None

    def test_set_mmemory_download_fname(self, instrument):
        # Test Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        # Call the method
        instrument.set_mmemory_download_fname()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_all(self, instrument):
        # Test Loads a complete instrument setup, using a named file on the mass storage.

        # Call the method
        instrument.set_mmemory_load_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_data(self, instrument):
        # Test Loads the specified arb segment(.arb/.barb) or arb sequence (.seq) file in INTERNAL or USB memory into volatile memory for the specified channel.

        # Call the method
        instrument.set_mmemory_load_data()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_list(self, instrument):
        # Test Loads a frequency list file (.lst).

        # Call the method
        instrument.set_mmemory_load_list()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_state(self, instrument):
        # Test Stores the current instrument state to a state file. 

        # Call the method
        instrument.set_mmemory_load_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_mdirectory(self, instrument):
        # Test MMEMory:MDIRectory makes a new directory (folder) on the mass storage medium.

        # Call the method
        instrument.set_mmemory_mdirectory()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_move(self, instrument):
        # Test Moves and/or renames <file1> to <file2>. 

        # Call the method
        instrument.set_mmemory_move()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_rdirectory(self, instrument):
        # Test MMEMory:RDIRectory removes a directory (folder) on the mass storage medium.

        # Call the method
        instrument.set_mmemory_rdirectory()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_all(self, instrument):
        # Test Loads or saves a complete instrument setup, using a named file on the mass storage.

        # Call the method
        instrument.set_mmemory_store_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_data(self, instrument):
        # Test Stores the specified arb segment(.arb/.barb) or arb sequence (.seq) data in the channel specified volatile memory (default, channel 1) in INTERNAL or USB memory.

        # Call the method
        instrument.set_mmemory_store_data()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_list(self, instrument):
        # Test Loads or stores a frequency list file (.lst).

        # Call the method
        instrument.set_mmemory_store_list()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_state(self, instrument):
        # Test Stores the current instrument state to a state file. 

        # Call the method
        instrument.set_mmemory_store_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_mmemory_upload(self, instrument):
        # Test Uploads the contents of a file from the instrument to the host computer.

        # Call the method
        result = instrument.get_mmemory_upload()

        # Verify the response is not None
        assert result is not None

    def test_get_output(self, instrument):
        # Test Enables or disables the front-panel output connector.

        # Call the method
        result = instrument.get_output()

        # Verify the response is not None
        assert result is not None

    def test_set_output(self, instrument):
        # Test Enables or disables the front-panel output connector.

        # Call the method
        instrument.set_output()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_load(self, instrument):
        # Test Sets expected output termination.

        # Call the method
        result = instrument.get_output_load()

        # Verify the response is not None
        assert result is not None

    def test_set_output_load(self, instrument):
        # Test Sets expected output termination.

        # Call the method
        instrument.set_output_load()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_mode(self, instrument):
        # Test Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        # Call the method
        result = instrument.get_output_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_output_mode(self, instrument):
        # Test Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        # Call the method
        instrument.set_output_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_polarity(self, instrument):
        # Test Inverts waveform relative to the offset voltage.

        # Call the method
        result = instrument.get_output_polarity()

        # Verify the response is not None
        assert result is not None

    def test_set_output_polarity(self, instrument):
        # Test Inverts waveform relative to the offset voltage.

        # Call the method
        instrument.set_output_polarity()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync(self, instrument):
        # Test Disables or enables the front-panel Sync connector.  

        # Call the method
        result = instrument.get_output_sync()

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync(self, instrument):
        # Test Disables or enables the front-panel Sync connector.  

        # Call the method
        instrument.set_output_sync()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_mode(self, instrument):
        # Test Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        # Call the method
        result = instrument.get_output_sync_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_mode(self, instrument):
        # Test Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        # Call the method
        instrument.set_output_sync_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_polarity(self, instrument):
        # Test Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        # Call the method
        result = instrument.get_output_sync_polarity()

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_polarity(self, instrument):
        # Test Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        # Call the method
        instrument.set_output_sync_polarity()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_source(self, instrument):
        # Test Sets the source for the Sync output connector.

        # Call the method
        result = instrument.get_output_sync_source()

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_source(self, instrument):
        # Test Sets the source for the Sync output connector.

        # Call the method
        instrument.set_output_sync_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger(self, instrument):
        # Test Disables or enables the "trigger out" signal for sweep and burst modes.

        # Call the method
        result = instrument.get_output_trigger()

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger(self, instrument):
        # Test Disables or enables the "trigger out" signal for sweep and burst modes.

        # Call the method
        instrument.set_output_trigger()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger_slope(self, instrument):
        # Test Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        # Call the method
        result = instrument.get_output_trigger_slope()

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger_slope(self, instrument):
        # Test Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        # Call the method
        instrument.set_output_trigger_slope()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger_source(self, instrument):
        # Test Selects the source channel used by trigger output on a two-channel instrument. 

        # Call the method
        result = instrument.get_output_trigger_source()

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger_source(self, instrument):
        # Test Selects the source channel used by trigger output on a two-channel instrument. 

        # Call the method
        instrument.set_output_trigger_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_gate_polarity(self, instrument):
        # Test Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        # Call the method
        result = instrument.get_source_burst_gate_polarity()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_gate_polarity(self, instrument):
        # Test Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        # Call the method
        instrument.set_source_burst_gate_polarity()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_internal_period(self, instrument):
        # Test Sets the burst period for internally-triggered bursts.

        # Call the method
        result = instrument.get_source_burst_internal_period()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_internal_period(self, instrument):
        # Test Sets the burst period for internally-triggered bursts.

        # Call the method
        instrument.set_source_burst_internal_period()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_mode(self, instrument):
        # Test Selects the burst mode.

        # Call the method
        result = instrument.get_source_burst_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_mode(self, instrument):
        # Test Selects the burst mode.

        # Call the method
        instrument.set_source_burst_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_ncycles(self, instrument):
        # Test Sets the number of cycles to be output per burst (triggered burst mode only).

        # Call the method
        result = instrument.get_source_burst_ncycles()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_ncycles(self, instrument):
        # Test Sets the number of cycles to be output per burst (triggered burst mode only).

        # Call the method
        instrument.set_source_burst_ncycles()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_phase(self, instrument):
        # Test Sets the starting phase angle for the burst.

        # Call the method
        result = instrument.get_source_burst_phase()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_phase(self, instrument):
        # Test Sets the starting phase angle for the burst.

        # Call the method
        instrument.set_source_burst_phase()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_state(self, instrument):
        # Test Enables or disables burst mode.

        # Call the method
        result = instrument.get_source_burst_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_state(self, instrument):
        # Test Enables or disables burst mode.

        # Call the method
        instrument.set_source_burst_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_depth(self, instrument):
        # Test Sets internal modulation depth ("percent modulation") in percent.

        # Call the method
        result = instrument.get_source_am_depth()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_depth(self, instrument):
        # Test Sets internal modulation depth ("percent modulation") in percent.

        # Call the method
        instrument.set_source_am_depth()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_dssc(self, instrument):
        # Test Selects Amplitude Modulation mode 

        # Call the method
        result = instrument.get_source_am_dssc()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_dssc(self, instrument):
        # Test Selects Amplitude Modulation mode 

        # Call the method
        instrument.set_source_am_dssc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_internal_frequency(self, instrument):
        # Test Sets frequency of modulating waveform.

        # Call the method
        result = instrument.get_source_am_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_internal_frequency(self, instrument):
        # Test Sets frequency of modulating waveform.

        # Call the method
        instrument.set_source_am_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_internal_function(self, instrument):
        # Test Selects shape of modulating waveform.

        # Call the method
        result = instrument.get_source_am_internal_function()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_internal_function(self, instrument):
        # Test Selects shape of modulating waveform.

        # Call the method
        instrument.set_source_am_internal_function()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        result = instrument.get_source_am_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        instrument.set_source_am_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        result = instrument.get_source_am_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        instrument.set_source_am_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_apply(self, instrument):
        # Test Queries the output configuration.

        # Call the method
        result = instrument.get_source_apply()

        # Verify the response is not None
        assert result is not None

    def test_set_source_apply_arbitrary(self, instrument):
        # Test Outputs arbitrary waveform selected by FUNCtion: ARBitrary, using the specified sample rate, amplitude, and offset. 

        # Call the method
        instrument.set_source_apply_arbitrary()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_dc(self, instrument):
        # Test Outputs a DC voltage.

        # Call the method
        instrument.set_source_apply_dc()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_noise(self, instrument):
        # Test Outputs gaussian noise with the specified amplitude and DC offset.

        # Call the method
        instrument.set_source_apply_noise()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_prbs(self, instrument):
        # Test Outputs a pseudo-random binary sequence with the specified bit rate, amplitude and DC offset.

        # Call the method
        instrument.set_source_apply_prbs()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_pulse(self, instrument):
        # Test Outputs a pulse wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        instrument.set_source_apply_pulse()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_ramp(self, instrument):
        # Test Outputs a ramp wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        instrument.set_source_apply_ramp()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_sinusoid(self, instrument):
        # Test Outputs a sine wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        instrument.set_source_apply_sinusoid()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_square(self, instrument):
        # Test Outputs a square wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        instrument.set_source_apply_square()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_triangle(self, instrument):
        # Test Outputs a triangle wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        instrument.set_source_apply_triangle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_internal_rate(self, instrument):
        # Test Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        # Call the method
        result = instrument.get_source_bpsk_internal_rate()

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_internal_rate(self, instrument):
        # Test Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        # Call the method
        instrument.set_source_bpsk_internal_rate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_phase(self, instrument):
        # Test Sets the Binary Phase Shift Keying phase shift in degrees.

        # Call the method
        result = instrument.get_source_bpsk_phase()

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_phase(self, instrument):
        # Test Sets the Binary Phase Shift Keying phase shift in degrees.

        # Call the method
        instrument.set_source_bpsk_phase()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        result = instrument.get_source_bpsk_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        instrument.set_source_bpsk_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        result = instrument.get_source_bpsk_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        instrument.set_source_bpsk_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_combine_feed(self, instrument):
        # Test Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        # Call the method
        result = instrument.get_source_combine_feed()

        # Verify the response is not None
        assert result is not None

    def test_set_source_combine_feed(self, instrument):
        # Test Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        # Call the method
        instrument.set_source_combine_feed()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_blockreal32(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockReal32 syntax

        # Call the method with BlockReal32 syntax
        instrument.set_source_data_arbitrary(syntax=syntax.BLOCKREAL32)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_ascii(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        instrument.set_source_data_arbitrary(syntax=syntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_dac_ascii(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        instrument.set_source_data_arbitrary_dac(syntax=syntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_dac_blockint16(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockInt16 syntax

        # Call the method with BlockInt16 syntax
        instrument.set_source_data_arbitrary_dac(syntax=syntax.BLOCKINT16)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_blockreal32(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockReal32 syntax

        # Call the method with BlockReal32 syntax
        instrument.set_source_data_arbitrary2(syntax=syntax.BLOCKREAL32)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_ascii(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        instrument.set_source_data_arbitrary2(syntax=syntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_dac_ascii(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        instrument.set_source_data_arbitrary2_dac(syntax=syntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_dac_blockint16(self, instrument):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockInt16 syntax

        # Call the method with BlockInt16 syntax
        instrument.set_source_data_arbitrary2_dac(syntax=syntax.BLOCKINT16)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_arbitrary2_format(self, instrument):
        # Test Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        # Call the method
        result = instrument.get_source_data_arbitrary2_format()

        # Verify the response is not None
        assert result is not None

    def test_set_source_data_arbitrary2_format(self, instrument):
        # Test Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        # Call the method
        instrument.set_source_data_arbitrary2_format()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_attribute_average(self, instrument):
        # Test Returns the arithmetic mean of all data points for the specified arbitrary waveform INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = instrument.get_source_data_attribute_average()

        # Verify the response is not None
        assert result is not None

    def test_get_source_data_attribute_cfactor(self, instrument):
        # Test Returns the crest factor of all data points for the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = instrument.get_source_data_attribute_cfactor()

        # Verify the response is not None
        assert result is not None

    def test_get_source_data_attribute_points(self, instrument):
        # Test Returns the number of points in the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = instrument.get_source_data_attribute_points()

        # Verify the response is not None
        assert result is not None

    def test_get_source_data_attribute_ptpeak(self, instrument):
        # Test This query calculates the peak-to-peak value of all data points for the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = instrument.get_source_data_attribute_ptpeak()

        # Verify the response is not None
        assert result is not None

    def test_set_source_data_sequence(self, instrument):
        # Test Defines a sequence of waveforms already loaded into waveform memory via MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        # Call the method
        instrument.set_source_data_sequence()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_volatile_catalog(self, instrument):
        # Test Returns the contents of volatile waveform memory, including arbitrary waveforms and sequences.

        # Call the method
        result = instrument.get_source_data_volatile_catalog()

        # Verify the response is not None
        assert result is not None

    def test_source_data_volatile_clear(self, instrument):
        # Test Clears waveform memory for the specified channel and reloads the default waveform.

        # Call the method
        instrument.source_data_volatile_clear()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_volatile_free(self, instrument):
        # Test Returns number of points available (free) in volatile memory. 

        # Call the method
        result = instrument.get_source_data_volatile_free()

        # Verify the response is not None
        assert result is not None

    def test_get_source_fm_deviation(self, instrument):
        # Test Sets the peak frequency deviation in Hz. 

        # Call the method
        result = instrument.get_source_fm_deviation()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_deviation(self, instrument):
        # Test Sets the peak frequency deviation in Hz. 

        # Call the method
        instrument.set_source_fm_deviation()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_internal_frequency(self, instrument):
        # Test Sets the frequency of the modulating waveform. 

        # Call the method
        result = instrument.get_source_fm_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_internal_frequency(self, instrument):
        # Test Sets the frequency of the modulating waveform. 

        # Call the method
        instrument.set_source_fm_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_internal_function(self, instrument):
        # Test This command selects the shape of the modulating waveform.

        # Call the method
        result = instrument.get_source_fm_internal_function()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_internal_function(self, instrument):
        # Test This command selects the shape of the modulating waveform.

        # Call the method
        instrument.set_source_fm_internal_function()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        result = instrument.get_source_fm_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        instrument.set_source_fm_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        result = instrument.get_source_fm_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        instrument.set_source_fm_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency(self, instrument):
        # Test Sets the output frequency.

        # Call the method
        result = instrument.get_source_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency(self, instrument):
        # Test Sets the output frequency.

        # Call the method
        instrument.set_source_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_center(self, instrument):
        # Test Sets the center frequency.

        # Call the method
        result = instrument.get_source_frequency_center()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_center(self, instrument):
        # Test Sets the center frequency.

        # Call the method
        instrument.set_source_frequency_center()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_mode(self, instrument):
        # Test Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        # Call the method
        result = instrument.get_source_frequency_couple_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_mode(self, instrument):
        # Test Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        # Call the method
        instrument.set_source_frequency_couple_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_offset(self, instrument):
        # Test Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        # Call the method
        result = instrument.get_source_frequency_couple_offset()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_offset(self, instrument):
        # Test Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        # Call the method
        instrument.set_source_frequency_couple_offset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_ratio(self, instrument):
        # Test Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        # Call the method
        result = instrument.get_source_frequency_couple_ratio()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_ratio(self, instrument):
        # Test Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        # Call the method
        instrument.set_source_frequency_couple_ratio()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_state(self, instrument):
        # Test Enables/disables frequency coupling between channels in a two-channel instrument.

        # Call the method
        result = instrument.get_source_frequency_couple_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_state(self, instrument):
        # Test Enables/disables frequency coupling between channels in a two-channel instrument.

        # Call the method
        instrument.set_source_frequency_couple_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_mode(self, instrument):
        # Test Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        # Call the method
        result = instrument.get_source_frequency_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_mode(self, instrument):
        # Test Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        # Call the method
        instrument.set_source_frequency_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_span(self, instrument):
        # Test Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        # Call the method
        result = instrument.get_source_frequency_span()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_span(self, instrument):
        # Test Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        # Call the method
        instrument.set_source_frequency_span()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_start(self, instrument):
        # Test Sets the start frequencies for a frequency sweep.

        # Call the method
        result = instrument.get_source_frequency_start()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_start(self, instrument):
        # Test Sets the start frequencies for a frequency sweep.

        # Call the method
        instrument.set_source_frequency_start()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_stop(self, instrument):
        # Test Sets the stop frequencies for a frequency sweep.

        # Call the method
        result = instrument.get_source_frequency_stop()

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_stop(self, instrument):
        # Test Sets the stop frequencies for a frequency sweep.

        # Call the method
        instrument.set_source_frequency_stop()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_frequency(self, instrument):
        # Test Sets the FSK alternate (or "hop") frequency.

        # Call the method
        result = instrument.get_source_fskey_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_frequency(self, instrument):
        # Test Sets the FSK alternate (or "hop") frequency.

        # Call the method
        instrument.set_source_fskey_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_internal_rate(self, instrument):
        # Test Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        # Call the method
        result = instrument.get_source_fskey_internal_rate()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_internal_rate(self, instrument):
        # Test Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        # Call the method
        instrument.set_source_fskey_internal_rate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        result = instrument.get_source_fskey_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        instrument.set_source_fskey_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        result = instrument.get_source_fskey_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        instrument.set_source_fskey_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function(self, instrument):
        # Test Selects output function.

        # Call the method
        result = instrument.get_source_function()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function(self, instrument):
        # Test Selects output function.

        # Call the method
        instrument.set_source_function()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary(self, instrument):
        # Test Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        # Call the method
        result = instrument.get_source_function_arbitrary()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary(self, instrument):
        # Test Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        # Call the method
        instrument.set_source_function_arbitrary()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_advance(self, instrument):
        # Test Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        # Call the method
        result = instrument.get_source_function_arbitrary_advance()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_advance(self, instrument):
        # Test Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        # Call the method
        instrument.set_source_function_arbitrary_advance()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_gain(self, instrument):
        # Test Sets the gain balance ratio for dual arbitrary waveforms.

        # Call the method
        result = instrument.get_source_function_arbitrary_balance_gain()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_gain(self, instrument):
        # Test Sets the gain balance ratio for dual arbitrary waveforms.

        # Call the method
        instrument.set_source_function_arbitrary_balance_gain()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_offset1(self, instrument):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        result = instrument.get_source_function_arbitrary_balance_offset1()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_offset1(self, instrument):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        instrument.set_source_function_arbitrary_balance_offset1()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_offset2(self, instrument):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        result = instrument.get_source_function_arbitrary_balance_offset2()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_offset2(self, instrument):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        instrument.set_source_function_arbitrary_balance_offset2()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_state(self, instrument):
        # Test Enables or disables channel balancing for dual arbitrary waveforms 

        # Call the method
        result = instrument.get_source_function_arbitrary_balance_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_state(self, instrument):
        # Test Enables or disables channel balancing for dual arbitrary waveforms 

        # Call the method
        instrument.set_source_function_arbitrary_balance_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_filter(self, instrument):
        # Test Specifies the filter setting for an arbitrary waveform.

        # Call the method
        result = instrument.get_source_function_arbitrary_filter()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_filter(self, instrument):
        # Test Specifies the filter setting for an arbitrary waveform.

        # Call the method
        instrument.set_source_function_arbitrary_filter()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_frequency(self, instrument):
        # Test Sets the frequency for the arbitrary waveform.



        # Call the method
        result = instrument.get_source_function_arbitrary_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_frequency(self, instrument):
        # Test Sets the frequency for the arbitrary waveform.



        # Call the method
        instrument.set_source_function_arbitrary_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_period(self, instrument):
        # Test Sets the period for the arbitrary waveform.

        # Call the method
        result = instrument.get_source_function_arbitrary_period()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_period(self, instrument):
        # Test Sets the period for the arbitrary waveform.

        # Call the method
        instrument.set_source_function_arbitrary_period()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_points(self, instrument):
        # Test Returns the number of points in the currently selected arbitrary waveform.

        # Call the method
        result = instrument.get_source_function_arbitrary_points()

        # Verify the response is not None
        assert result is not None

    def test_get_source_function_arbitrary_ptpeak(self, instrument):
        # Test Sets peak to peak voltage.

        # Call the method
        result = instrument.get_source_function_arbitrary_ptpeak()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_ptpeak(self, instrument):
        # Test Sets peak to peak voltage.

        # Call the method
        instrument.set_source_function_arbitrary_ptpeak()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_skew_state(self, instrument):
        # Test Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        # Call the method
        result = instrument.get_source_function_arbitrary_skew_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_skew_state(self, instrument):
        # Test Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        # Call the method
        instrument.set_source_function_arbitrary_skew_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_skew_time(self, instrument):
        # Test Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        # Call the method
        result = instrument.get_source_function_arbitrary_skew_time()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_skew_time(self, instrument):
        # Test Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        # Call the method
        instrument.set_source_function_arbitrary_skew_time()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_srate(self, instrument):
        # Test Sets the sample rate for the arbitrary waveform.

        # Call the method
        result = instrument.get_source_function_arbitrary_srate()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_srate(self, instrument):
        # Test Sets the sample rate for the arbitrary waveform.

        # Call the method
        instrument.set_source_function_arbitrary_srate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_function_arbitrary_synchronize(self, instrument):
        # Test Causes two independent arbitrary waveforms to synchronize to first point of each waveform (two-channel instruments only).

        # Call the method
        instrument.source_function_arbitrary_synchronize()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_noise_bandwidth(self, instrument):
        # Test Sets bandwidth of noise function.

        # Call the method
        result = instrument.get_source_function_noise_bandwidth()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_noise_bandwidth(self, instrument):
        # Test Sets bandwidth of noise function.

        # Call the method
        instrument.set_source_function_noise_bandwidth()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_prbs_brate(self, instrument):
        # Test Sets the pseudo-random binary sequence (PRBS) bit rate.

        # Call the method
        result = instrument.get_source_function_prbs_brate()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_prbs_brate(self, instrument):
        # Test Sets the pseudo-random binary sequence (PRBS) bit rate.

        # Call the method
        instrument.set_source_function_prbs_brate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_prbs_data(self, instrument):
        # Test Sets the pseudo-random binary sequence (PRBS) type. 

        # Call the method
        result = instrument.get_source_function_prbs_data()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_prbs_data(self, instrument):
        # Test Sets the pseudo-random binary sequence (PRBS) type. 

        # Call the method
        instrument.set_source_function_prbs_data()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_prbs_transition_both(self, instrument):
        # Test Sets PRBS transition edge time on both edges of a PRBS transition.

        # Call the method
        result = instrument.get_source_function_prbs_transition_both()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_prbs_transition_both(self, instrument):
        # Test Sets PRBS transition edge time on both edges of a PRBS transition.

        # Call the method
        instrument.set_source_function_prbs_transition_both()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_dcycle(self, instrument):
        # Test Sets pulse duty cycle.

        # Call the method
        result = instrument.get_source_function_pulse_dcycle()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_dcycle(self, instrument):
        # Test Sets pulse duty cycle.

        # Call the method
        instrument.set_source_function_pulse_dcycle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_hold(self, instrument):
        # Test Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        # Call the method
        result = instrument.get_source_function_pulse_hold()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_hold(self, instrument):
        # Test Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        # Call the method
        instrument.set_source_function_pulse_hold()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_period(self, instrument):
        # Test Sets the period for pulse waveforms.

        # Call the method
        result = instrument.get_source_function_pulse_period()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_period(self, instrument):
        # Test Sets the period for pulse waveforms.

        # Call the method
        instrument.set_source_function_pulse_period()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_transition_both(self, instrument):
        # Test Sets the pulse edge time on both edges of a pulse.

        # Call the method
        result = instrument.get_source_function_pulse_transition_both()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_transition_both(self, instrument):
        # Test Sets the pulse edge time on both edges of a pulse.

        # Call the method
        instrument.set_source_function_pulse_transition_both()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_transition_leading(self, instrument):
        # Test Sets the pulse edge time on the leading edges of a pulse.



        # Call the method
        result = instrument.get_source_function_pulse_transition_leading()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_transition_leading(self, instrument):
        # Test Sets the pulse edge time on the leading edges of a pulse.



        # Call the method
        instrument.set_source_function_pulse_transition_leading()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_transition_trailing(self, instrument):
        # Test Sets the pulse edge time on the trailing edges of a pulse.



        # Call the method
        result = instrument.get_source_function_pulse_transition_trailing()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_transition_trailing(self, instrument):
        # Test Sets the pulse edge time on the trailing edges of a pulse.



        # Call the method
        instrument.set_source_function_pulse_transition_trailing()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_width(self, instrument):
        # Test Sets pulse width.

        # Call the method
        result = instrument.get_source_function_pulse_width()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_width(self, instrument):
        # Test Sets pulse width.

        # Call the method
        instrument.set_source_function_pulse_width()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_ramp_symmetry(self, instrument):
        # Test Sets the symmetry percentage for ramp waves.

        # Call the method
        result = instrument.get_source_function_ramp_symmetry()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_ramp_symmetry(self, instrument):
        # Test Sets the symmetry percentage for ramp waves.

        # Call the method
        instrument.set_source_function_ramp_symmetry()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_square_dcycle(self, instrument):
        # Test Sets duty cycle percentage for square wave.

        # Call the method
        result = instrument.get_source_function_square_dcycle()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_square_dcycle(self, instrument):
        # Test Sets duty cycle percentage for square wave.

        # Call the method
        instrument.set_source_function_square_dcycle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_square_period(self, instrument):
        # Test Sets period for square wave.

        # Call the method
        result = instrument.get_source_function_square_period()

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_square_period(self, instrument):
        # Test Sets period for square wave.

        # Call the method
        instrument.set_source_function_square_period()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_list_dwell(self, instrument):
        # Test Sets dwell time, the amount of time each frequency in a frequency list is generated.

        # Call the method
        result = instrument.get_source_list_dwell()

        # Verify the response is not None
        assert result is not None

    def test_set_source_list_dwell(self, instrument):
        # Test Sets dwell time, the amount of time each frequency in a frequency list is generated.

        # Call the method
        instrument.set_source_list_dwell()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_list_frequency(self, instrument):
        # Test Specifies frequency values in a frequency list.

        # Call the method
        result = instrument.get_source_list_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_list_frequency(self, instrument):
        # Test Specifies frequency values in a frequency list.

        # Call the method
        instrument.set_source_list_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_list_frequency_points(self, instrument):
        # Test Returns number of frequencies in current frequency list.

        # Call the method
        result = instrument.get_source_list_frequency_points()

        # Verify the response is not None
        assert result is not None

    def test_get_source_marker_cycle(self, instrument):
        # Test Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        # Call the method
        result = instrument.get_source_marker_cycle()

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_cycle(self, instrument):
        # Test Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        # Call the method
        instrument.set_source_marker_cycle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_marker_frequency(self, instrument):
        # Test Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        # Call the method
        result = instrument.get_source_marker_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_frequency(self, instrument):
        # Test Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        # Call the method
        instrument.set_source_marker_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_marker_point(self, instrument):
        # Test Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        # Call the method
        result = instrument.get_source_marker_point()

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_point(self, instrument):
        # Test Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        # Call the method
        instrument.set_source_marker_point()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_modulation_phase(self, instrument):
        # Test Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        # Call the method
        result = instrument.get_source_modulation_phase()

        # Verify the response is not None
        assert result is not None

    def test_set_source_modulation_phase(self, instrument):
        # Test Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        # Call the method
        instrument.set_source_modulation_phase()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_phase_reference(self, instrument):
        # Test Simultaneously removes the offset set by PHASe and adjusts the primary phase generator by an amount equivalent to the PHASe setting.

        # Call the method
        instrument.source_phase_reference()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_phase_synchronize(self, instrument):
        # Test Simultaneously resets all phase generators in the instrument, including the modulation phase generators, to establish a common, internal phase zero reference point.

        # Call the method
        instrument.source_phase_synchronize()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_phase_unlock_error_state(self, instrument):
        # Test Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        # Call the method
        result = instrument.get_source_phase_unlock_error_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_phase_unlock_error_state(self, instrument):
        # Test Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        # Call the method
        instrument.set_source_phase_unlock_error_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_deviation(self, instrument):
        # Test Sets the phase deviation in degrees. 

        # Call the method
        result = instrument.get_source_pm_deviation()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_deviation(self, instrument):
        # Test Sets the phase deviation in degrees. 

        # Call the method
        instrument.set_source_pm_deviation()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_internal_frequency(self, instrument):
        # Test Sets the frequency of the modulating waveform.

        # Call the method
        result = instrument.get_source_pm_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_internal_frequency(self, instrument):
        # Test Sets the frequency of the modulating waveform.

        # Call the method
        instrument.set_source_pm_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_internal_function(self, instrument):
        # Test Selects shape of modulating waveform.

        # Call the method
        result = instrument.get_source_pm_internal_function()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_internal_function(self, instrument):
        # Test Selects shape of modulating waveform.

        # Call the method
        instrument.set_source_pm_internal_function()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        result = instrument.get_source_pm_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        instrument.set_source_pm_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        result = instrument.get_source_pm_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        instrument.set_source_pm_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_deviation(self, instrument):
        # Test Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        # Call the method
        result = instrument.get_source_pwm_deviation()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_deviation(self, instrument):
        # Test Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        # Call the method
        instrument.set_source_pwm_deviation()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_deviation_dcycle(self, instrument):
        # Test Sets duty cycle deviation in percent of period.

        # Call the method
        result = instrument.get_source_pwm_deviation_dcycle()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_deviation_dcycle(self, instrument):
        # Test Sets duty cycle deviation in percent of period.

        # Call the method
        instrument.set_source_pwm_deviation_dcycle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_internal_frequency(self, instrument):
        # Test Selects frequency at which output pulse width shifts through its pulse width deviation.

        # Call the method
        result = instrument.get_source_pwm_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_internal_frequency(self, instrument):
        # Test Selects frequency at which output pulse width shifts through its pulse width deviation.

        # Call the method
        instrument.set_source_pwm_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_internal_function(self, instrument):
        # Test Selects shape of the internal modulating waveform.

        # Call the method
        result = instrument.get_source_pwm_internal_function()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_internal_function(self, instrument):
        # Test Selects shape of the internal modulating waveform.

        # Call the method
        instrument.set_source_pwm_internal_function()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        result = instrument.get_source_pwm_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_source(self, instrument):
        # Test Select the source of the modulating signal.

        # Call the method
        instrument.set_source_pwm_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        result = instrument.get_source_pwm_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_state(self, instrument):
        # Test Enables or disables modulation.

        # Call the method
        instrument.set_source_pwm_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_mode(self, instrument):
        # Test Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        # Call the method
        result = instrument.get_source_rate_couple_mode()

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_mode(self, instrument):
        # Test Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        # Call the method
        instrument.set_source_rate_couple_mode()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_offset(self, instrument):
        # Test Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        # Call the method
        result = instrument.get_source_rate_couple_offset()

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_offset(self, instrument):
        # Test Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        # Call the method
        instrument.set_source_rate_couple_offset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_ratio(self, instrument):
        # Test Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        # Call the method
        result = instrument.get_source_rate_couple_ratio()

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_ratio(self, instrument):
        # Test Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        # Call the method
        instrument.set_source_rate_couple_ratio()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_state(self, instrument):
        # Test Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        # Call the method
        result = instrument.get_source_rate_couple_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_state(self, instrument):
        # Test Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        # Call the method
        instrument.set_source_rate_couple_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_roscillator_source(self, instrument):
        # Test Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        # Call the method
        result = instrument.get_source_roscillator_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_roscillator_source(self, instrument):
        # Test Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        # Call the method
        instrument.set_source_roscillator_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_roscillator_source_auto(self, instrument):
        # Test Disables or enables automatic selection of the reference oscillator.

        # Call the method
        result = instrument.get_source_roscillator_source_auto()

        # Verify the response is not None
        assert result is not None

    def test_set_source_roscillator_source_auto(self, instrument):
        # Test Disables or enables automatic selection of the reference oscillator.

        # Call the method
        instrument.set_source_roscillator_source_auto()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_roscillator_source_current(self, instrument):
        # Test Indicates which reference oscillator signal is currently in use when ROSC:SOURce:AUTO is ON.

        # Call the method
        result = instrument.get_source_roscillator_source_current()

        # Verify the response is not None
        assert result is not None

    def test_get_source_sum_amplitude(self, instrument):
        # Test Sets internal modulation depth (or "percent modulation") in percent.

        # Call the method
        result = instrument.get_source_sum_amplitude()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_amplitude(self, instrument):
        # Test Sets internal modulation depth (or "percent modulation") in percent.

        # Call the method
        instrument.set_source_sum_amplitude()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_internal_frequency(self, instrument):
        # Test Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        # Call the method
        result = instrument.get_source_sum_internal_frequency()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_internal_frequency(self, instrument):
        # Test Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        # Call the method
        instrument.set_source_sum_internal_frequency()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_internal_function(self, instrument):
        # Test Selects the summing waveform (the waveform added to the primary waveform).

        # Call the method
        result = instrument.get_source_sum_internal_function()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_internal_function(self, instrument):
        # Test Selects the summing waveform (the waveform added to the primary waveform).

        # Call the method
        instrument.set_source_sum_internal_function()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_source(self, instrument):
        # Test Selects source of summing signal.

        # Call the method
        result = instrument.get_source_sum_source()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_source(self, instrument):
        # Test Selects source of summing signal.

        # Call the method
        instrument.set_source_sum_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_state(self, instrument):
        # Test Disables or enables SUM function.

        # Call the method
        result = instrument.get_source_sum_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_state(self, instrument):
        # Test Disables or enables SUM function.

        # Call the method
        instrument.set_source_sum_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_htime(self, instrument):
        # Test Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        # Call the method
        result = instrument.get_source_sweep_htime()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_htime(self, instrument):
        # Test Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        # Call the method
        instrument.set_source_sweep_htime()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_rtime(self, instrument):
        # Test Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        # Call the method
        result = instrument.get_source_sweep_rtime()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_rtime(self, instrument):
        # Test Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        # Call the method
        instrument.set_source_sweep_rtime()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_spacing(self, instrument):
        # Test Selects linear or logarithmic spacing for sweep.

        # Call the method
        result = instrument.get_source_sweep_spacing()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_spacing(self, instrument):
        # Test Selects linear or logarithmic spacing for sweep.

        # Call the method
        instrument.set_source_sweep_spacing()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_state(self, instrument):
        # Test Enables or disables the sweep.

        # Call the method
        result = instrument.get_source_sweep_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_state(self, instrument):
        # Test Enables or disables the sweep.

        # Call the method
        instrument.set_source_sweep_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_time(self, instrument):
        # Test Sets time (seconds) to sweep from start frequency to stop frequency.

        # Call the method
        result = instrument.get_source_sweep_time()

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_time(self, instrument):
        # Test Sets time (seconds) to sweep from start frequency to stop frequency.

        # Call the method
        instrument.set_source_sweep_time()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_track(self, instrument):
        # Test Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        # Call the method
        result = instrument.get_source_track()

        # Verify the response is not None
        assert result is not None

    def test_set_source_track(self, instrument):
        # Test Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        # Call the method
        instrument.set_source_track()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage(self, instrument):
        # Test Sets output amplitude.

        # Call the method
        result = instrument.get_source_voltage()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage(self, instrument):
        # Test Sets output amplitude.

        # Call the method
        instrument.set_source_voltage()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_limit_high(self, instrument):
        # Test Sets the high limits for output voltage.



        # Call the method
        result = instrument.get_source_voltage_limit_high()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_limit_high(self, instrument):
        # Test Sets the high limits for output voltage.



        # Call the method
        instrument.set_source_voltage_limit_high()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_limit_low(self, instrument):
        # Test Sets the low limits for output voltage.



        # Call the method
        result = instrument.get_source_voltage_limit_low()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_limit_low(self, instrument):
        # Test Sets the low limits for output voltage.



        # Call the method
        instrument.set_source_voltage_limit_low()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_limit_state(self, instrument):
        # Test Enables or disables output amplitude voltage limits.

        # Call the method
        result = instrument.get_source_voltage_limit_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_limit_state(self, instrument):
        # Test Enables or disables output amplitude voltage limits.

        # Call the method
        instrument.set_source_voltage_limit_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_range_auto(self, instrument):
        # Test Disables or enables voltage autoranging for all functions.

        # Call the method
        result = instrument.get_source_voltage_range_auto()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_range_auto(self, instrument):
        # Test Disables or enables voltage autoranging for all functions.

        # Call the method
        instrument.set_source_voltage_range_auto()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_unit(self, instrument):
        # Test Selects the units for output amplitude.

        # Call the method
        result = instrument.get_source_voltage_unit()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_unit(self, instrument):
        # Test Selects the units for output amplitude.

        # Call the method
        instrument.set_source_voltage_unit()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_couple_state(self, instrument):
        # Test Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        # Call the method
        result = instrument.get_source_voltage_couple_state()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_couple_state(self, instrument):
        # Test Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        # Call the method
        instrument.set_source_voltage_couple_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_high(self, instrument):
        # Test Set the waveform's high voltage levels.

        # Call the method
        result = instrument.get_source_voltage_high()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_high(self, instrument):
        # Test Set the waveform's high voltage levels.

        # Call the method
        instrument.set_source_voltage_high()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_low(self, instrument):
        # Test Set the waveform's low voltage levels.

        # Call the method
        result = instrument.get_source_voltage_low()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_low(self, instrument):
        # Test Set the waveform's low voltage levels.

        # Call the method
        instrument.set_source_voltage_low()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_offset(self, instrument):
        # Test Sets DC offset voltage.

        # Call the method
        result = instrument.get_source_voltage_offset()

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_offset(self, instrument):
        # Test Sets DC offset voltage.

        # Call the method
        instrument.set_source_voltage_offset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_operation_condition(self, instrument):
        # Test Queries the condition register for the Standard Operation Register group. 

        # Call the method
        result = instrument.get_status_operation_condition()

        # Verify the response is not None
        assert result is not None

    def test_get_status_operation_enable(self, instrument):
        # Test Enables bits in the enable register for the Standard Operation Register group.

        # Call the method
        result = instrument.get_status_operation_enable()

        # Verify the response is not None
        assert result is not None

    def test_set_status_operation_enable(self, instrument):
        # Test Enables bits in the enable register for the Standard Operation Register group.

        # Call the method
        instrument.set_status_operation_enable()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_operation_event(self, instrument):
        # Test Queries the event register for the Standard Operation Register group.

        # Call the method
        result = instrument.get_status_operation_event()

        # Verify the response is not None
        assert result is not None

    def test_status_preset(self, instrument):
        # Test Clears Questionable Data enable register and Standard Operation enable register.

        # Call the method
        instrument.status_preset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_questionable_condition(self, instrument):
        # Test Queries the condition register for the Questionable Data Register group.

        # Call the method
        result = instrument.get_status_questionable_condition()

        # Verify the response is not None
        assert result is not None

    def test_get_status_questionable_enable(self, instrument):
        # Test Enables bits in the enable register for the Questionable Data Register group. 

        # Call the method
        result = instrument.get_status_questionable_enable()

        # Verify the response is not None
        assert result is not None

    def test_set_status_questionable_enable(self, instrument):
        # Test Enables bits in the enable register for the Questionable Data Register group. 

        # Call the method
        instrument.set_status_questionable_enable()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_questionable_event(self, instrument):
        # Test Queries the event register for the Questionable Data Register group. 

        # Call the method
        result = instrument.get_status_questionable_event()

        # Verify the response is not None
        assert result is not None

    def test_system_beeper_immediate(self, instrument):
        # Test Issues a single beep.

        # Call the method
        instrument.system_beeper_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_beeper_state(self, instrument):
        # Test Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        # Call the method
        result = instrument.get_system_beeper_state()

        # Verify the response is not None
        assert result is not None

    def test_set_system_beeper_state(self, instrument):
        # Test Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        # Call the method
        instrument.set_system_beeper_state()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_enable(self, instrument):
        # Test Disables or enables the GPIB, USB, or LAN remote interface.

        # Call the method
        result = instrument.get_system_communicate_enable()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_enable(self, instrument):
        # Test Disables or enables the GPIB, USB, or LAN remote interface.

        # Call the method
        instrument.set_system_communicate_enable()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_gpib_address(self, instrument):
        # Test Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        # Call the method
        result = instrument.get_system_communicate_gpib_address()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_gpib_address(self, instrument):
        # Test Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        # Call the method
        instrument.set_system_communicate_gpib_address()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_control(self, instrument):
        # Test Reads the initial Control connection port number for Sockets communications.

        # Call the method
        result = instrument.get_system_communicate_lan_control()

        # Verify the response is not None
        assert result is not None

    def test_get_system_communicate_lan_dhcp(self, instrument):
        # Test Disables or enables instrument's use of DHCP.

        # Call the method
        result = instrument.get_system_communicate_lan_dhcp()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_dhcp(self, instrument):
        # Test Disables or enables instrument's use of DHCP.

        # Call the method
        instrument.set_system_communicate_lan_dhcp()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_dns(self, instrument):
        # Test Assigns static IP addresses of Domain Name System (DNS) servers.

        # Call the method
        result = instrument.get_system_communicate_lan_dns()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_dns(self, instrument):
        # Test Assigns static IP addresses of Domain Name System (DNS) servers.

        # Call the method
        instrument.set_system_communicate_lan_dns()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_domain(self, instrument):
        # Test Returns the domain name of the LAN to which the instrument is connected.

        # Call the method
        result = instrument.get_system_communicate_lan_domain()

        # Verify the response is not None
        assert result is not None

    def test_get_system_communicate_lan_gateway(self, instrument):
        # Test Assigns a default gateway for the instrument.

        # Call the method
        result = instrument.get_system_communicate_lan_gateway()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_gateway(self, instrument):
        # Test Assigns a default gateway for the instrument.

        # Call the method
        instrument.set_system_communicate_lan_gateway()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_hostname(self, instrument):
        # Test Assigns a hostname to the instrument.

        # Call the method
        result = instrument.get_system_communicate_lan_hostname()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_hostname(self, instrument):
        # Test Assigns a hostname to the instrument.

        # Call the method
        instrument.set_system_communicate_lan_hostname()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_ipaddress(self, instrument):
        # Test Assigns a static Internet Protocol (IP) address for the instrument. 

        # Call the method
        result = instrument.get_system_communicate_lan_ipaddress()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_ipaddress(self, instrument):
        # Test Assigns a static Internet Protocol (IP) address for the instrument. 

        # Call the method
        instrument.set_system_communicate_lan_ipaddress()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_mac(self, instrument):
        # Test Reads the instrument's Media Access Control (MAC) address.

        # Call the method
        result = instrument.get_system_communicate_lan_mac()

        # Verify the response is not None
        assert result is not None

    def test_get_system_communicate_lan_smask(self, instrument):
        # Test Assigns a subnet mask for the instrument. 

        # Call the method
        result = instrument.get_system_communicate_lan_smask()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_smask(self, instrument):
        # Test Assigns a subnet mask for the instrument. 

        # Call the method
        instrument.set_system_communicate_lan_smask()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_telnet_prompt(self, instrument):
        # Test Sets the command prompt seen when communicating with the instrument via Telnet.

        # Call the method
        result = instrument.get_system_communicate_lan_telnet_prompt()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_telnet_prompt(self, instrument):
        # Test Sets the command prompt seen when communicating with the instrument via Telnet.

        # Call the method
        instrument.set_system_communicate_lan_telnet_prompt()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_telnet_wmessage(self, instrument):
        # Test Sets welcome message seen when communicating with instrument via Telnet.

        # Call the method
        result = instrument.get_system_communicate_lan_telnet_wmessage()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_telnet_wmessage(self, instrument):
        # Test Sets welcome message seen when communicating with instrument via Telnet.

        # Call the method
        instrument.set_system_communicate_lan_telnet_wmessage()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_system_communicate_lan_update(self, instrument):
        # Test Stores any changes made to the LAN settings into non-volatile memory and restarts the LAN driver with the updated settings.

        # Call the method
        instrument.system_communicate_lan_update()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_wins(self, instrument):
        # Test Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        # Call the method
        result = instrument.get_system_communicate_lan_wins()

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_wins(self, instrument):
        # Test Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        # Call the method
        instrument.set_system_communicate_lan_wins()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_date(self, instrument):
        # Test Sets system clock date.

        # Call the method
        result = instrument.get_system_date()

        # Verify the response is not None
        assert result is not None

    def test_set_system_date(self, instrument):
        # Test Sets system clock date.

        # Call the method
        instrument.set_system_date()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_error(self, instrument):
        # Test Reads and clears one error from error queue.

        # Call the method
        result = instrument.get_system_error()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_catalog(self, instrument):
        # Test Returns a comma separated list of installed, licensed options.

        # Call the method
        result = instrument.get_system_license_catalog()

        # Verify the response is not None
        assert result is not None

    def test_set_system_license_delete(self, instrument):
        # Test Deletes a license.

        # Call the method
        instrument.set_system_license_delete()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_system_license_delete_all(self, instrument):
        # Test Deletes all licenses.

        # Call the method
        instrument.system_license_delete_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_license_description(self, instrument):
        # Test Returns a description of specified option, regardless of whether it is currently licensed.

        # Call the method
        result = instrument.get_system_license_description()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_error(self, instrument):
        # Test Returns a string of all the errors produced by SYSTem:LICense:INSTall.

        # Call the method
        result = instrument.get_system_license_error()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_error_count(self, instrument):
        # Test Returns the number of license errors generated by SYSTem:LICense:INSTall.

        # Call the method
        result = instrument.get_system_license_error_count()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_install(self, instrument):
        # Test This command installs all licenses from a specified file or from all license files in the specified folder. 

        # Call the method
        result = instrument.get_system_license_install()

        # Verify the response is not None
        assert result is not None

    def test_set_system_license_install(self, instrument):
        # Test This command installs all licenses from a specified file or from all license files in the specified folder. 

        # Call the method
        instrument.set_system_license_install()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_lock_name(self, instrument):
        # Test Returns the current I/O interface (the I/O interface in use by the querying computer).

        # Call the method
        result = instrument.get_system_lock_name()

        # Verify the response is not None
        assert result is not None

    def test_get_system_lock_owner(self, instrument):
        # Test Returns the I/O interface that currently has a lock.

        # Call the method
        result = instrument.get_system_lock_owner()

        # Verify the response is not None
        assert result is not None

    def test_system_lock_release(self, instrument):
        # Test Decrements the lock count by 1 and may release the I/O interface from which the command is executed.

        # Call the method
        instrument.system_lock_release()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_lock_request(self, instrument):
        # Test Requests a lock of the current I/O interface.

        # Call the method
        result = instrument.get_system_lock_request()

        # Verify the response is not None
        assert result is not None

    def test_system_security_immediate(self, instrument):
        # Test Sanitizes all user-accessible instrument memory.

        # Call the method
        instrument.system_security_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_time(self, instrument):
        # Test Sets system clock time.

        # Call the method
        result = instrument.get_system_time()

        # Verify the response is not None
        assert result is not None

    def test_set_system_time(self, instrument):
        # Test Sets system clock time.

        # Call the method
        instrument.set_system_time()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_version(self, instrument):
        # Test Returns version of the SCPI (Standard Commands for Programmable Instruments) that the instrument complies with. 

        # Call the method
        result = instrument.get_system_version()

        # Verify the response is not None
        assert result is not None

    def test_trigger(self, instrument):
        # Test Forces immediate trigger to initiate sequence, sweep, list, or burst.

        # Call the method
        instrument.trigger()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_count(self, instrument):
        # Test Sets trigger count.

        # Call the method
        result = instrument.get_trigger_count()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_count(self, instrument):
        # Test Sets trigger count.

        # Call the method
        instrument.set_trigger_count()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_delay(self, instrument):
        # Test Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        # Call the method
        result = instrument.get_trigger_delay()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_delay(self, instrument):
        # Test Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        # Call the method
        instrument.set_trigger_delay()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_timer(self, instrument):
        # Test Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        # Call the method
        result = instrument.get_trigger_timer()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_timer(self, instrument):
        # Test Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        # Call the method
        instrument.set_trigger_timer()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_slope(self, instrument):
        # Test Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        # Call the method
        result = instrument.get_trigger_slope()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_slope(self, instrument):
        # Test Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        # Call the method
        instrument.set_trigger_slope()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_source(self, instrument):
        # Test Selects the trigger source for sequence, list, burst or sweep. 

        # Call the method
        result = instrument.get_trigger_source()

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_source(self, instrument):
        # Test Selects the trigger source for sequence, list, burst or sweep. 

        # Call the method
        instrument.set_trigger_source()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_unit_angle(self, instrument):
        # Test Specifies the angle units that displayed on the screen and used for specifying angles.

        # Call the method
        result = instrument.get_unit_angle()

        # Verify the response is not None
        assert result is not None

    def test_set_unit_angle(self, instrument):
        # Test Specifies the angle units that displayed on the screen and used for specifying angles.

        # Call the method
        instrument.set_unit_angle()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters
