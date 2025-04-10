import pytest
import numpy as np
import os

# Generated test file for Keysight33500B class
# This file is auto-generated. Do not edit manually.

# Add the parent directory to the Python path to import the driver
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import all required enum classes
from instrumental.drivers.funcgenerators.keysight33500b import (
    Keysight33500B,
    DispWindFocusCommandParameter1,
    DispWindUnitArbrateCommandParameter1,
    DispWindUnitPulseCommandParameter1,
    DispWindUnitRateCommandParameter1,
    DispWindUnitSweepCommandParameter1,
    DispWindUnitVoltageCommandParameter1,
    DispWindViewCommandParameter1,
    Enum33500bBoolean,
    Enum33500bEnumminmaxdef,
    Enum33500bEnumminmaxdefinf,
    Enum33500bStdNumEnums,
    Enum33500bStdNumEnumsclone,
    Enum33500bStdNumEnumscloneclone,
    FormBorderCommandParameter1,
    HcopSdumDataFormatCommandParameter1,
    OutpModeCommandParameter1,
    OutpPolarityCommandParameter1,
    OutpSyncModeCommandParameter1,
    OutpSyncPolarityCommandParameter1,
    OutpSyncSourceCommandParameter1,
    OutpTrigSlopeCommandParameter1,
    OutpTrigSourceCommandParameter1,
    SourAmIntFuncShapeCommandParameter1clone,
    SourAmSourceCommandParameter1,
    SourAmSourceCommandParameter1clone,
    SourBursGatePolarityCommandParameter1,
    SourBursModeCommandParameter1,
    SourCombFeedCommandParameter1,
    SourFmSourceCommandParameter1,
    SourFreqCoupModeCommandParameter1,
    SourFreqModeCommandParameter1,
    SourFuncShapArbAdvanceCommandParameter1,
    SourFuncShapArbFilterCommandParameter1,
    SourFuncShapPrbsDataCommandParameter1,
    SourFuncShapPulsHoldCommandParameter1,
    SourFuncShapeCommandParameter1clone,
    SourPmSourceCommandParameter1,
    SourPwmSourceCommandParameter1,
    SourRateCoupModeCommandParameter1,
    SourRoscSourAutoCommandParameter1,
    SourRoscSourceCommandParameter1,
    SourSumIntFunctionCommandParameter1clone,
    SourSweSpacingCommandParameter1,
    SourTrackCommandParameter1,
    SourVoltLevUnitCommandParameter1,
    SourVoltRangAutoCommandParameter1,
    SourceDataArb2FormatCommandParameter1,
    SourceDataArbitrary2DacSyntax,
    SourceDataArbitrary2Syntax,
    SourceDataArbitraryDacSyntax,
    SourceDataArbitrarySyntax,
    SystCommEnableCommandParameter2clone,
    SystCommEnableCommandParameter2clone2,
    TrigSeqSlopeCommandParameter1,
    TrigSeqSourceCommandParameter1,
    UnitAngleCommandParameter1clone
)

class TestKeysight33500B:

    def test_get_ese(self, inst: Keysight33500B):
        # Test Enables bits in the enable register for the Standard Event Register group.

        # Call the method
        result = inst.get_ese(enable_value=1)

        # Verify the response is not None
        assert result is not None

    def test_set_ese(self, inst: Keysight33500B):
        # Test Enables bits in the enable register for the Standard Event Register group.

        # Call the method
        inst.set_ese(enable_value=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_esr(self, inst: Keysight33500B):
        # Test Standard Event Status Register Query. Queries the event register for the Standard Event Register group. 

        # Call the method
        result = inst.get_esr()

        # Verify the response is not None
        assert result is not None

    def test_get_idn(self, inst: Keysight33500B):
        # Test instrument’s identification string.

        # Call the method
        result = inst.get_idn()

        # Verify the response is not None
        assert result is not None

    def test_get_opc(self, inst: Keysight33500B):
        # Test Sets "Operation Complete" (bit 0) in the Standard Event register at the completion of the current operation. Returns 1 to the output buffer after all pending commands complete.

        # Call the method
        result = inst.get_opc()

        # Verify the response is not None
        assert result is not None

    def test_get_opt(self, inst: Keysight33500B):
        # Test Returns a quoted string identifying any installed options.

        # Call the method
        result = inst.get_opt()

        # Verify the response is not None
        assert result is not None

    def test_get_psc(self, inst: Keysight33500B):
        # Test Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.

        # Call the method
        result = inst.get_psc(psc=1)

        # Verify the response is not None
        assert result is not None

    def test_set_psc(self, inst: Keysight33500B):
        # Test Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.

        # Call the method
        inst.set_psc(psc=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_rcl(self, inst: Keysight33500B):
        # Test Recalls (*RCL) instrument state in specified non-volatile location.

        # Call the method
        inst.set_rcl(rcl=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_sav(self, inst: Keysight33500B):
        # Test saves (*SAV) instrument state in specified non-volatile location. 

        # Call the method
        inst.set_sav(sav=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_sre(self, inst: Keysight33500B):
        # Test Service Request Enable. This command enables bits in the enable register for the Status Byte Register group.

        # Call the method
        result = inst.get_sre(enable_value=1)

        # Verify the response is not None
        assert result is not None

    def test_set_sre(self, inst: Keysight33500B):
        # Test Service Request Enable. This command enables bits in the enable register for the Status Byte Register group.

        # Call the method
        inst.set_sre(enable_value=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_stb(self, inst: Keysight33500B):
        # Test Read Status Byte Query. This command queries the condition register for the Status Byte Register group.

        # Call the method
        result = inst.get_stb()

        # Verify the response is not None
        assert result is not None

    def test_get_tst(self, inst: Keysight33500B):
        # Test Self-Test Query. Performs a complete instrument self-test.

        # Call the method
        result = inst.get_tst()

        # Verify the response is not None
        assert result is not None

    def test_abort(self, inst: Keysight33500B):
        # Test Halts a sequence, list, sweep, or burst, even an infinite burst. 

        # Call the method
        inst.abort()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_all(self, inst: Keysight33500B):
        # Test Performs a calibration using the calibration value (CALibration:VALue). 

        # Call the method
        result = inst.get_calibration_all()

        # Verify the response is not None
        assert result is not None

    def test_get_calibration_count(self, inst: Keysight33500B):
        # Test Returns the number of calibrations performed.

        # Call the method
        result = inst.get_calibration_count()

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_secure_code(self, inst: Keysight33500B):
        # Test Sets the security code to prevent unauthorized calibrations.

        # Call the method
        inst.set_calibration_secure_code(new_code=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_secure_state(self, inst: Keysight33500B):
        # Test Unsecures or secures the instrument for calibration. 

        # Call the method
        result = inst.get_calibration_secure_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'], code=1)

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_secure_state(self, inst: Keysight33500B):
        # Test Unsecures or secures the instrument for calibration. 

        # Call the method
        inst.set_calibration_secure_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'], code=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_setup(self, inst: Keysight33500B):
        # Test Configures the calibration step (default 1) to be performed. 

        # Call the method
        result = inst.get_calibration_setup(step=1)

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_setup(self, inst: Keysight33500B):
        # Test Configures the calibration step (default 1) to be performed. 

        # Call the method
        inst.set_calibration_setup(step=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_string(self, inst: Keysight33500B):
        # Test Stores a message of up to 40 characters in calibration memory.

        # Call the method
        result = inst.get_calibration_string(string=1)

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_string(self, inst: Keysight33500B):
        # Test Stores a message of up to 40 characters in calibration memory.

        # Call the method
        inst.set_calibration_string(string=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_calibration_value(self, inst: Keysight33500B):
        # Test Specifies the value of the known calibration signal.

        # Call the method
        result = inst.get_calibration_value(value=1)

        # Verify the response is not None
        assert result is not None

    def test_set_calibration_value(self, inst: Keysight33500B):
        # Test Specifies the value of the known calibration signal.

        # Call the method
        inst.set_calibration_value(value=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display(self, inst: Keysight33500B):
        # Test Disables or enables the front-panel display.

        # Call the method
        result = inst.get_display(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_display(self, inst: Keysight33500B):
        # Test Disables or enables the front-panel display.

        # Call the method
        inst.set_display(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_focus(self, inst: Keysight33500B):
        # Test selects the channel displayed "in front" on a two-channel instrument 

        # Call the method
        result = inst.get_display_focus(focus=['DispWindFocusCommandParameter1.CH1', 'DispWindFocusCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_focus(self, inst: Keysight33500B):
        # Test selects the channel displayed "in front" on a two-channel instrument 

        # Call the method
        inst.set_display_focus(focus=['DispWindFocusCommandParameter1.CH1', 'DispWindFocusCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_text(self, inst: Keysight33500B):
        # Test Displays a text message on the front-panel display.   

        # Call the method
        result = inst.get_display_text(string=1)

        # Verify the response is not None
        assert result is not None

    def test_set_display_text(self, inst: Keysight33500B):
        # Test Displays a text message on the front-panel display.   

        # Call the method
        inst.set_display_text(string=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_display_text_clear(self, inst: Keysight33500B):
        # Test Clears the text message from the front-panel display.

        # Call the method
        inst.display_text_clear()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_arbrate(self, inst: Keysight33500B):
        # Test Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).

        # Call the method
        result = inst.get_display_unit_arbrate(arbrate=['DispWindUnitArbrateCommandParameter1.SRATe', 'DispWindUnitArbrateCommandParameter1.FREQuency', 'DispWindUnitArbrateCommandParameter1.PERiod'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_arbrate(self, inst: Keysight33500B):
        # Test Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).

        # Call the method
        inst.set_display_unit_arbrate(arbrate=['DispWindUnitArbrateCommandParameter1.SRATe', 'DispWindUnitArbrateCommandParameter1.FREQuency', 'DispWindUnitArbrateCommandParameter1.PERiod'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_pulse(self, inst: Keysight33500B):
        # Test Selects the method for specifying pulse duration.

        # Call the method
        result = inst.get_display_unit_pulse(pulse=['DispWindUnitPulseCommandParameter1.WIDTh', 'DispWindUnitPulseCommandParameter1.DUTY'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_pulse(self, inst: Keysight33500B):
        # Test Selects the method for specifying pulse duration.

        # Call the method
        inst.set_display_unit_pulse(pulse=['DispWindUnitPulseCommandParameter1.WIDTh', 'DispWindUnitPulseCommandParameter1.DUTY'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_rate(self, inst: Keysight33500B):
        # Test Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).

        # Call the method
        result = inst.get_display_unit_rate(rate=['DispWindUnitRateCommandParameter1.FREQuency', 'DispWindUnitRateCommandParameter1.PERiod'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_rate(self, inst: Keysight33500B):
        # Test Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).

        # Call the method
        inst.set_display_unit_rate(rate=['DispWindUnitRateCommandParameter1.FREQuency', 'DispWindUnitRateCommandParameter1.PERiod'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_sweep(self, inst: Keysight33500B):
        # Test Selects the method for specifying sweep frequency range.

        # Call the method
        result = inst.get_display_unit_sweep(sweep=['DispWindUnitSweepCommandParameter1.STARtstop', 'DispWindUnitSweepCommandParameter1.CENTerspan'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_sweep(self, inst: Keysight33500B):
        # Test Selects the method for specifying sweep frequency range.

        # Call the method
        inst.set_display_unit_sweep(sweep=['DispWindUnitSweepCommandParameter1.STARtstop', 'DispWindUnitSweepCommandParameter1.CENTerspan'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_unit_voltage(self, inst: Keysight33500B):
        # Test Selects the method for specifying voltage ranges.

        # Call the method
        result = inst.get_display_unit_voltage(voltage=['DispWindUnitVoltageCommandParameter1.AMPLitudeoff', 'DispWindUnitVoltageCommandParameter1.HIGHlow'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_unit_voltage(self, inst: Keysight33500B):
        # Test Selects the method for specifying voltage ranges.

        # Call the method
        inst.set_display_unit_voltage(voltage=['DispWindUnitVoltageCommandParameter1.AMPLitudeoff', 'DispWindUnitVoltageCommandParameter1.HIGHlow'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_display_view(self, inst: Keysight33500B):
        # Test Selects the screen layout.

        # Call the method
        result = inst.get_display_view(view=['DispWindViewCommandParameter1.STANdard', 'DispWindViewCommandParameter1.TEXT', 'DispWindViewCommandParameter1.GRAPH', 'DispWindViewCommandParameter1.DUAL'])

        # Verify the response is not None
        assert result is not None

    def test_set_display_view(self, inst: Keysight33500B):
        # Test Selects the screen layout.

        # Call the method
        inst.set_display_view(view=['DispWindViewCommandParameter1.STANdard', 'DispWindViewCommandParameter1.TEXT', 'DispWindViewCommandParameter1.GRAPH', 'DispWindViewCommandParameter1.DUAL'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_format_border(self, inst: Keysight33500B):
        # Test Sets the byte order used in binary data point transfers in the block mode.

        # Call the method
        result = inst.get_format_border(border=['FormBorderCommandParameter1.NORMal', 'FormBorderCommandParameter1.SWAPped'])

        # Verify the response is not None
        assert result is not None

    def test_set_format_border(self, inst: Keysight33500B):
        # Test Sets the byte order used in binary data point transfers in the block mode.

        # Call the method
        inst.set_format_border(border=['FormBorderCommandParameter1.NORMal', 'FormBorderCommandParameter1.SWAPped'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_hcopy_sdump_data(self, inst: Keysight33500B):
        # Test Returns the front panel display image ("screen shot")

        # Call the method
        result = inst.get_hcopy_sdump_data()

        # Verify the response is not None
        assert result is not None

    def test_get_hcopy_sdump_data_format(self, inst: Keysight33500B):
        # Test Specifies the image format for images returned by HCOPy:SDUMp:DATA?.

        # Call the method
        result = inst.get_hcopy_sdump_data_format(format=['HcopSdumDataFormatCommandParameter1.BMP', 'HcopSdumDataFormatCommandParameter1.PNG'])

        # Verify the response is not None
        assert result is not None

    def test_set_hcopy_sdump_data_format(self, inst: Keysight33500B):
        # Test Specifies the image format for images returned by HCOPy:SDUMp:DATA?.

        # Call the method
        inst.set_hcopy_sdump_data_format(format=['HcopSdumDataFormatCommandParameter1.BMP', 'HcopSdumDataFormatCommandParameter1.PNG'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_initiate_continuous(self, inst: Keysight33500B):
        # Test Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        # Call the method
        result = inst.get_initiate_continuous(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_initiate_continuous(self, inst: Keysight33500B):
        # Test Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        # Call the method
        inst.set_initiate_continuous(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_initiate_continuous_all(self, inst: Keysight33500B):
        # Test Specifies whether the trigger system for both channels (ALL) always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        # Call the method
        inst.set_initiate_continuous_all(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_initiate_immediate(self, inst: Keysight33500B):
        # Test Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt.

        # Call the method
        inst.initiate_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_initiate_immediate_all(self, inst: Keysight33500B):
        # Test Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt

        # Call the method
        inst.initiate_immediate_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_identify_state(self, inst: Keysight33500B):
        # Test Turns the LXI Identify Indicator on the display on or off.

        # Call the method
        result = inst.get_lxi_identify_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_lxi_identify_state(self, inst: Keysight33500B):
        # Test Turns the LXI Identify Indicator on the display on or off.

        # Call the method
        inst.set_lxi_identify_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_mdns_enable(self, inst: Keysight33500B):
        # Test Disables or enables the Multicast Domain Name System (mDNS).

        # Call the method
        result = inst.get_lxi_mdns_enable(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_lxi_mdns_enable(self, inst: Keysight33500B):
        # Test Disables or enables the Multicast Domain Name System (mDNS).

        # Call the method
        inst.set_lxi_mdns_enable(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_mdns_hname_resolved(self, inst: Keysight33500B):
        # Test Returns the resolved (unique) mDNS hostname in the form <mDNS Hostname>-N. 

        # Call the method
        result = inst.get_lxi_mdns_hname_resolved()

        # Verify the response is not None
        assert result is not None

    def test_get_lxi_mdns_sname_desired(self, inst: Keysight33500B):
        # Test Sets the desired mDNS service name.

        # Call the method
        result = inst.get_lxi_mdns_sname_desired(name=1)

        # Verify the response is not None
        assert result is not None

    def test_set_lxi_mdns_sname_desired(self, inst: Keysight33500B):
        # Test Sets the desired mDNS service name.

        # Call the method
        inst.set_lxi_mdns_sname_desired(name=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_lxi_mdns_sname_resolved(self, inst: Keysight33500B):
        # Test Returns the resolved (unique) mDNS service name in the form <Desired mDNS Service Name>(N). 

        # Call the method
        result = inst.get_lxi_mdns_sname_resolved()

        # Verify the response is not None
        assert result is not None

    def test_lxi_reset(self, inst: Keysight33500B):
        # Test Resets LAN settings to a known operating state, beginning with DHCP. 

        # Call the method
        inst.lxi_reset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_lxi_restart(self, inst: Keysight33500B):
        # Test Restarts the LAN with the current settings as specified by the SYSTem:COMM:LAN commands. 

        # Call the method
        inst.lxi_restart()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_nstates(self, inst: Keysight33500B):
        # Test Returns the total number of memory locations available for state storage 

        # Call the method
        result = inst.get_memory_nstates()

        # Verify the response is not None
        assert result is not None

    def test_get_memory_state_catalog(self, inst: Keysight33500B):
        # Test Returns the names assigned to locations 0 through 4.

        # Call the method
        result = inst.get_memory_state_catalog()

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_delete(self, inst: Keysight33500B):
        # Test Deletes a state storage location.

        # Call the method
        inst.set_memory_state_delete(location=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_name(self, inst: Keysight33500B):
        # Test Names a storage location. 

        # Call the method
        result = inst.get_memory_state_name(sLocation=1, name=1)

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_name(self, inst: Keysight33500B):
        # Test Names a storage location. 

        # Call the method
        inst.set_memory_state_name(sLocation=1, name=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_recall_auto(self, inst: Keysight33500B):
        # Test Disables or enables automatic recall of instrument state in storage location "0" at power on.

        # Call the method
        result = inst.get_memory_state_recall_auto(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_memory_state_recall_auto(self, inst: Keysight33500B):
        # Test Disables or enables automatic recall of instrument state in storage location "0" at power on.

        # Call the method
        inst.set_memory_state_recall_auto(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_memory_state_valid(self, inst: Keysight33500B):
        # Test Indicates whether a valid state is currently stored in a storage location.

        # Call the method
        result = inst.get_memory_state_valid()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_catalog_all(self, inst: Keysight33500B):
        # Test Returns a list of all files in the current mass storage directory, including internal storage and the USB drive.

        # Call the method
        result = inst.get_mmemory_catalog_all()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_catalog_data_arbitrary(self, inst: Keysight33500B):
        # Test Returns a list of all the arbitrary sequence (.seq) files and folders, as well as arbitrary waveform (.arb/.barb) files in a folder.

        # Call the method
        result = inst.get_mmemory_catalog_data_arbitrary()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_catalog_state(self, inst: Keysight33500B):
        # Test Lists all state files (.sta file extension) in a folder. 

        # Call the method
        result = inst.get_mmemory_catalog_state()

        # Verify the response is not None
        assert result is not None

    def test_get_mmemory_cdirectory(self, inst: Keysight33500B):
        # Test MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        # Call the method
        result = inst.get_mmemory_cdirectory(folder=1)

        # Verify the response is not None
        assert result is not None

    def test_set_mmemory_cdirectory(self, inst: Keysight33500B):
        # Test MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        # Call the method
        inst.set_mmemory_cdirectory(folder=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_copy(self, inst: Keysight33500B):
        # Test Copies <file1> to <file2>. 

        # Call the method
        inst.set_mmemory_copy(file1=1, file2=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_copy_sequence(self, inst: Keysight33500B):
        # Test Copies a sequence from <source> to <destination>. 

        # Call the method
        inst.set_mmemory_copy_sequence(source=1, destination=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_delete(self, inst: Keysight33500B):
        # Test Deletes a file. 

        # Call the method
        inst.set_mmemory_delete(file=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_download_data(self, inst: Keysight33500B):
        # Test Downloads data from the host computer to a file in the instrument.

        # Call the method
        inst.set_mmemory_download_data(binary_block=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_mmemory_download_fname(self, inst: Keysight33500B):
        # Test Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        # Call the method
        result = inst.get_mmemory_download_fname(filename=1)

        # Verify the response is not None
        assert result is not None

    def test_set_mmemory_download_fname(self, inst: Keysight33500B):
        # Test Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        # Call the method
        inst.set_mmemory_download_fname(filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_all(self, inst: Keysight33500B):
        # Test Loads a complete instrument setup, using a named file on the mass storage.

        # Call the method
        inst.set_mmemory_load_all(filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_data(self, inst: Keysight33500B):
        # Test Loads the specified arb segment(.arb/.barb) or arb sequence (.seq) file in INTERNAL or USB memory into volatile memory for the specified channel.

        # Call the method
        inst.set_mmemory_load_data(data_num=1, filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_list(self, inst: Keysight33500B):
        # Test Loads a frequency list file (.lst).

        # Call the method
        inst.set_mmemory_load_list(list_num=1, filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_load_state(self, inst: Keysight33500B):
        # Test Stores the current instrument state to a state file. 

        # Call the method
        inst.set_mmemory_load_state(filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_mdirectory(self, inst: Keysight33500B):
        # Test MMEMory:MDIRectory makes a new directory (folder) on the mass storage medium.

        # Call the method
        inst.set_mmemory_mdirectory(folder=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_move(self, inst: Keysight33500B):
        # Test Moves and/or renames <file1> to <file2>. 

        # Call the method
        inst.set_mmemory_move(file1=1, file2=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_rdirectory(self, inst: Keysight33500B):
        # Test MMEMory:RDIRectory removes a directory (folder) on the mass storage medium.

        # Call the method
        inst.set_mmemory_rdirectory(folder=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_all(self, inst: Keysight33500B):
        # Test Loads or saves a complete instrument setup, using a named file on the mass storage.

        # Call the method
        inst.set_mmemory_store_all(filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_data(self, inst: Keysight33500B):
        # Test Stores the specified arb segment(.arb/.barb) or arb sequence (.seq) data in the channel specified volatile memory (default, channel 1) in INTERNAL or USB memory.

        # Call the method
        inst.set_mmemory_store_data(data_num=1, filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_list(self, inst: Keysight33500B):
        # Test Loads or stores a frequency list file (.lst).

        # Call the method
        inst.set_mmemory_store_list(list_num=1, filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_mmemory_store_state(self, inst: Keysight33500B):
        # Test Stores the current instrument state to a state file. 

        # Call the method
        inst.set_mmemory_store_state(filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_mmemory_upload(self, inst: Keysight33500B):
        # Test Uploads the contents of a file from the instrument to the host computer.

        # Call the method
        result = inst.get_mmemory_upload()

        # Verify the response is not None
        assert result is not None

    def test_get_output(self, inst: Keysight33500B):
        # Test Enables or disables the front-panel output connector.

        # Call the method
        result = inst.get_output(output_num=1, state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_output(self, inst: Keysight33500B):
        # Test Enables or disables the front-panel output connector.

        # Call the method
        inst.set_output(output_num=1, state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_load(self, inst: Keysight33500B):
        # Test Sets expected output termination.

        # Call the method
        result = inst.get_output_load(ohms=1)

        # Verify the response is not None
        assert result is not None

    def test_set_output_load(self, inst: Keysight33500B):
        # Test Sets expected output termination.

        # Call the method
        inst.set_output_load(ohms=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_mode(self, inst: Keysight33500B):
        # Test Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        # Call the method
        result = inst.get_output_mode(mode=['OutpModeCommandParameter1.NORMal', 'OutpModeCommandParameter1.GATed'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_mode(self, inst: Keysight33500B):
        # Test Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        # Call the method
        inst.set_output_mode(mode=['OutpModeCommandParameter1.NORMal', 'OutpModeCommandParameter1.GATed'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_polarity(self, inst: Keysight33500B):
        # Test Inverts waveform relative to the offset voltage.

        # Call the method
        result = inst.get_output_polarity(polarity=['OutpPolarityCommandParameter1.NORMal', 'OutpPolarityCommandParameter1.INVerted'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_polarity(self, inst: Keysight33500B):
        # Test Inverts waveform relative to the offset voltage.

        # Call the method
        inst.set_output_polarity(polarity=['OutpPolarityCommandParameter1.NORMal', 'OutpPolarityCommandParameter1.INVerted'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync(self, inst: Keysight33500B):
        # Test Disables or enables the front-panel Sync connector.  

        # Call the method
        result = inst.get_output_sync(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync(self, inst: Keysight33500B):
        # Test Disables or enables the front-panel Sync connector.  

        # Call the method
        inst.set_output_sync(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_mode(self, inst: Keysight33500B):
        # Test Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        # Call the method
        result = inst.get_output_sync_mode(mode=['OutpSyncModeCommandParameter1.NORMal', 'OutpSyncModeCommandParameter1.CARRier', 'OutpSyncModeCommandParameter1.MARKer'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_mode(self, inst: Keysight33500B):
        # Test Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        # Call the method
        inst.set_output_sync_mode(mode=['OutpSyncModeCommandParameter1.NORMal', 'OutpSyncModeCommandParameter1.CARRier', 'OutpSyncModeCommandParameter1.MARKer'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_polarity(self, inst: Keysight33500B):
        # Test Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        # Call the method
        result = inst.get_output_sync_polarity(polarity=['OutpSyncPolarityCommandParameter1.NORMal', 'OutpSyncPolarityCommandParameter1.INVerted'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_polarity(self, inst: Keysight33500B):
        # Test Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        # Call the method
        inst.set_output_sync_polarity(polarity=['OutpSyncPolarityCommandParameter1.NORMal', 'OutpSyncPolarityCommandParameter1.INVerted'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_sync_source(self, inst: Keysight33500B):
        # Test Sets the source for the Sync output connector.

        # Call the method
        result = inst.get_output_sync_source(channel=['OutpSyncSourceCommandParameter1.CH1', 'OutpSyncSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_sync_source(self, inst: Keysight33500B):
        # Test Sets the source for the Sync output connector.

        # Call the method
        inst.set_output_sync_source(channel=['OutpSyncSourceCommandParameter1.CH1', 'OutpSyncSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger(self, inst: Keysight33500B):
        # Test Disables or enables the "trigger out" signal for sweep and burst modes.

        # Call the method
        result = inst.get_output_trigger(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger(self, inst: Keysight33500B):
        # Test Disables or enables the "trigger out" signal for sweep and burst modes.

        # Call the method
        inst.set_output_trigger(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger_slope(self, inst: Keysight33500B):
        # Test Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        # Call the method
        result = inst.get_output_trigger_slope(edge=['OutpTrigSlopeCommandParameter1.POSitive', 'OutpTrigSlopeCommandParameter1.NEGative'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger_slope(self, inst: Keysight33500B):
        # Test Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        # Call the method
        inst.set_output_trigger_slope(edge=['OutpTrigSlopeCommandParameter1.POSitive', 'OutpTrigSlopeCommandParameter1.NEGative'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_output_trigger_source(self, inst: Keysight33500B):
        # Test Selects the source channel used by trigger output on a two-channel instrument. 

        # Call the method
        result = inst.get_output_trigger_source(channel=['OutpTrigSourceCommandParameter1.CH1', 'OutpTrigSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_output_trigger_source(self, inst: Keysight33500B):
        # Test Selects the source channel used by trigger output on a two-channel instrument. 

        # Call the method
        inst.set_output_trigger_source(channel=['OutpTrigSourceCommandParameter1.CH1', 'OutpTrigSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_gate_polarity(self, inst: Keysight33500B):
        # Test Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        # Call the method
        result = inst.get_source_burst_gate_polarity(polarity=['SourBursGatePolarityCommandParameter1.NORMal', 'SourBursGatePolarityCommandParameter1.INVerted'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_gate_polarity(self, inst: Keysight33500B):
        # Test Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        # Call the method
        inst.set_source_burst_gate_polarity(polarity=['SourBursGatePolarityCommandParameter1.NORMal', 'SourBursGatePolarityCommandParameter1.INVerted'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_internal_period(self, inst: Keysight33500B):
        # Test Sets the burst period for internally-triggered bursts.

        # Call the method
        result = inst.get_source_burst_internal_period(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_internal_period(self, inst: Keysight33500B):
        # Test Sets the burst period for internally-triggered bursts.

        # Call the method
        inst.set_source_burst_internal_period(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_mode(self, inst: Keysight33500B):
        # Test Selects the burst mode.

        # Call the method
        result = inst.get_source_burst_mode(mode=['SourBursModeCommandParameter1.TRIGgered', 'SourBursModeCommandParameter1.GATed'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_mode(self, inst: Keysight33500B):
        # Test Selects the burst mode.

        # Call the method
        inst.set_source_burst_mode(mode=['SourBursModeCommandParameter1.TRIGgered', 'SourBursModeCommandParameter1.GATed'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_ncycles(self, inst: Keysight33500B):
        # Test Sets the number of cycles to be output per burst (triggered burst mode only).

        # Call the method
        result = inst.get_source_burst_ncycles(num_cycles=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_ncycles(self, inst: Keysight33500B):
        # Test Sets the number of cycles to be output per burst (triggered burst mode only).

        # Call the method
        inst.set_source_burst_ncycles(num_cycles=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_phase(self, inst: Keysight33500B):
        # Test Sets the starting phase angle for the burst.

        # Call the method
        result = inst.get_source_burst_phase(angle=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_phase(self, inst: Keysight33500B):
        # Test Sets the starting phase angle for the burst.

        # Call the method
        inst.set_source_burst_phase(angle=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_burst_state(self, inst: Keysight33500B):
        # Test Enables or disables burst mode.

        # Call the method
        result = inst.get_source_burst_state(boolean=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_burst_state(self, inst: Keysight33500B):
        # Test Enables or disables burst mode.

        # Call the method
        inst.set_source_burst_state(boolean=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_depth(self, inst: Keysight33500B):
        # Test Sets internal modulation depth ("percent modulation") in percent.

        # Call the method
        result = inst.get_source_am_depth(depth_in_percent=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_depth(self, inst: Keysight33500B):
        # Test Sets internal modulation depth ("percent modulation") in percent.

        # Call the method
        inst.set_source_am_depth(depth_in_percent=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_dssc(self, inst: Keysight33500B):
        # Test Selects Amplitude Modulation mode 

        # Call the method
        result = inst.get_source_am_dssc(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_dssc(self, inst: Keysight33500B):
        # Test Selects Amplitude Modulation mode 

        # Call the method
        inst.set_source_am_dssc(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_internal_frequency(self, inst: Keysight33500B):
        # Test Sets frequency of modulating waveform.

        # Call the method
        result = inst.get_source_am_internal_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_internal_frequency(self, inst: Keysight33500B):
        # Test Sets frequency of modulating waveform.

        # Call the method
        inst.set_source_am_internal_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_internal_function(self, inst: Keysight33500B):
        # Test Selects shape of modulating waveform.

        # Call the method
        result = inst.get_source_am_internal_function(function=['SourAmIntFuncShapeCommandParameter1clone.SINusoid', 'SourAmIntFuncShapeCommandParameter1clone.SQUare', 'SourAmIntFuncShapeCommandParameter1clone.TRIangle', 'SourAmIntFuncShapeCommandParameter1clone.RAMP', 'SourAmIntFuncShapeCommandParameter1clone.NRAMp', 'SourAmIntFuncShapeCommandParameter1clone.NOISe', 'SourAmIntFuncShapeCommandParameter1clone.PRBS', 'SourAmIntFuncShapeCommandParameter1clone.ARB'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_internal_function(self, inst: Keysight33500B):
        # Test Selects shape of modulating waveform.

        # Call the method
        inst.set_source_am_internal_function(function=['SourAmIntFuncShapeCommandParameter1clone.SINusoid', 'SourAmIntFuncShapeCommandParameter1clone.SQUare', 'SourAmIntFuncShapeCommandParameter1clone.TRIangle', 'SourAmIntFuncShapeCommandParameter1clone.RAMP', 'SourAmIntFuncShapeCommandParameter1clone.NRAMp', 'SourAmIntFuncShapeCommandParameter1clone.NOISe', 'SourAmIntFuncShapeCommandParameter1clone.PRBS', 'SourAmIntFuncShapeCommandParameter1clone.ARB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        result = inst.get_source_am_source(source=['SourAmSourceCommandParameter1.INTernal', 'SourAmSourceCommandParameter1.EXTernal', 'SourAmSourceCommandParameter1.CH1', 'SourAmSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        inst.set_source_am_source(source=['SourAmSourceCommandParameter1.INTernal', 'SourAmSourceCommandParameter1.EXTernal', 'SourAmSourceCommandParameter1.CH1', 'SourAmSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_am_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        result = inst.get_source_am_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_am_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        inst.set_source_am_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_apply(self, inst: Keysight33500B):
        # Test Queries the output configuration.

        # Call the method
        result = inst.get_source_apply()

        # Verify the response is not None
        assert result is not None

    def test_set_source_apply_arbitrary(self, inst: Keysight33500B):
        # Test Outputs arbitrary waveform selected by FUNCtion: ARBitrary, using the specified sample rate, amplitude, and offset. 

        # Call the method
        inst.set_source_apply_arbitrary(sample_rate=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_dc(self, inst: Keysight33500B):
        # Test Outputs a DC voltage.

        # Call the method
        inst.set_source_apply_dc(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_noise(self, inst: Keysight33500B):
        # Test Outputs gaussian noise with the specified amplitude and DC offset.

        # Call the method
        inst.set_source_apply_noise(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_prbs(self, inst: Keysight33500B):
        # Test Outputs a pseudo-random binary sequence with the specified bit rate, amplitude and DC offset.

        # Call the method
        inst.set_source_apply_prbs(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_pulse(self, inst: Keysight33500B):
        # Test Outputs a pulse wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        inst.set_source_apply_pulse(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_ramp(self, inst: Keysight33500B):
        # Test Outputs a ramp wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        inst.set_source_apply_ramp(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_sinusoid(self, inst: Keysight33500B):
        # Test Outputs a sine wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        inst.set_source_apply_sinusoid(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_square(self, inst: Keysight33500B):
        # Test Outputs a square wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        inst.set_source_apply_square(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_apply_triangle(self, inst: Keysight33500B):
        # Test Outputs a triangle wave with the specified frequency, amplitude, and DC offset.

        # Call the method
        inst.set_source_apply_triangle(frequency=1, amplitude=1, offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_internal_rate(self, inst: Keysight33500B):
        # Test Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        # Call the method
        result = inst.get_source_bpsk_internal_rate(modulating_frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_internal_rate(self, inst: Keysight33500B):
        # Test Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        # Call the method
        inst.set_source_bpsk_internal_rate(modulating_frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_phase(self, inst: Keysight33500B):
        # Test Sets the Binary Phase Shift Keying phase shift in degrees.

        # Call the method
        result = inst.get_source_bpsk_phase(angle=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_phase(self, inst: Keysight33500B):
        # Test Sets the Binary Phase Shift Keying phase shift in degrees.

        # Call the method
        inst.set_source_bpsk_phase(angle=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        result = inst.get_source_bpsk_source(source=['SourAmSourceCommandParameter1clone.INTernal', 'SourAmSourceCommandParameter1clone.EXTernal'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        inst.set_source_bpsk_source(source=['SourAmSourceCommandParameter1clone.INTernal', 'SourAmSourceCommandParameter1clone.EXTernal'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_bpsk_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        result = inst.get_source_bpsk_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_bpsk_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        inst.set_source_bpsk_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_combine_feed(self, inst: Keysight33500B):
        # Test Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        # Call the method
        result = inst.get_source_combine_feed(source=['SourCombFeedCommandParameter1.CH1', 'SourCombFeedCommandParameter1.CH2', 'SourCombFeedCommandParameter1.NONE'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_combine_feed(self, inst: Keysight33500B):
        # Test Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        # Call the method
        inst.set_source_combine_feed(source=['SourCombFeedCommandParameter1.CH1', 'SourCombFeedCommandParameter1.CH2', 'SourCombFeedCommandParameter1.NONE'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_blockreal32(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockReal32 syntax

        # Call the method with BlockReal32 syntax
        inst.set_source_data_arbitrary(arb_name=1, binary_block=1, syntax=SourceDataArbitrarySyntax.BLOCKREAL32)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_blockreal32(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockReal32 syntax

        # Call the method with BlockReal32 syntax
        inst.set_source_data_arbitrary(arb_name=1, binary_block=1, syntax=SourceDataArbitrarySyntax.BLOCKREAL32)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary(arb_name=1, binary_block=1, syntax=SourceDataArbitrarySyntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary(arb_name=1, binary_block=1, syntax=SourceDataArbitrarySyntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_dac_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary_dac(arb_name=1, value=1, syntax=SourceDataArbitraryDacSyntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_dac_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary_dac(arb_name=1, value=1, syntax=SourceDataArbitraryDacSyntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_dac_blockint16(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockInt16 syntax

        # Call the method with BlockInt16 syntax
        inst.set_source_data_arbitrary_dac(arb_name=1, value=1, syntax=SourceDataArbitraryDacSyntax.BLOCKINT16)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary_dac_blockint16(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockInt16 syntax

        # Call the method with BlockInt16 syntax
        inst.set_source_data_arbitrary_dac(arb_name=1, value=1, syntax=SourceDataArbitraryDacSyntax.BLOCKINT16)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_blockreal32(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockReal32 syntax

        # Call the method with BlockReal32 syntax
        inst.set_source_data_arbitrary2(arb_name=1, binary_block=1, syntax=SourceDataArbitrary2Syntax.BLOCKREAL32)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_blockreal32(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockReal32 syntax

        # Call the method with BlockReal32 syntax
        inst.set_source_data_arbitrary2(arb_name=1, binary_block=1, syntax=SourceDataArbitrary2Syntax.BLOCKREAL32)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary2(arb_name=1, binary_block=1, syntax=SourceDataArbitrary2Syntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary2(arb_name=1, binary_block=1, syntax=SourceDataArbitrary2Syntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_dac_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary2_dac(arb_name=1, value=1, syntax=SourceDataArbitrary2DacSyntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_dac_ascii(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with Ascii syntax

        # Call the method with Ascii syntax
        inst.set_source_data_arbitrary2_dac(arb_name=1, value=1, syntax=SourceDataArbitrary2DacSyntax.ASCII)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_dac_blockint16(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockInt16 syntax

        # Call the method with BlockInt16 syntax
        inst.set_source_data_arbitrary2_dac(arb_name=1, value=1, syntax=SourceDataArbitrary2DacSyntax.BLOCKINT16)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_set_source_data_arbitrary2_dac_blockint16(self, inst: Keysight33500B):
        # Test Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data. with BlockInt16 syntax

        # Call the method with BlockInt16 syntax
        inst.set_source_data_arbitrary2_dac(arb_name=1, value=1, syntax=SourceDataArbitrary2DacSyntax.BLOCKINT16)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_arbitrary2_format(self, inst: Keysight33500B):
        # Test Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        # Call the method
        result = inst.get_source_data_arbitrary2_format(format=['SourceDataArb2FormatCommandParameter1.AABB', 'SourceDataArb2FormatCommandParameter1.ABAB'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_data_arbitrary2_format(self, inst: Keysight33500B):
        # Test Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        # Call the method
        inst.set_source_data_arbitrary2_format(format=['SourceDataArb2FormatCommandParameter1.AABB', 'SourceDataArb2FormatCommandParameter1.ABAB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_attribute_average(self, inst: Keysight33500B):
        # Test Returns the arithmetic mean of all data points for the specified arbitrary waveform INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = inst.get_source_data_attribute_average()

        # Verify the response is not None
        assert result is not None

    def test_get_source_data_attribute_cfactor(self, inst: Keysight33500B):
        # Test Returns the crest factor of all data points for the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = inst.get_source_data_attribute_cfactor()

        # Verify the response is not None
        assert result is not None

    def test_get_source_data_attribute_points(self, inst: Keysight33500B):
        # Test Returns the number of points in the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = inst.get_source_data_attribute_points()

        # Verify the response is not None
        assert result is not None

    def test_get_source_data_attribute_ptpeak(self, inst: Keysight33500B):
        # Test This query calculates the peak-to-peak value of all data points for the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        # Call the method
        result = inst.get_source_data_attribute_ptpeak()

        # Verify the response is not None
        assert result is not None

    def test_set_source_data_sequence(self, inst: Keysight33500B):
        # Test Defines a sequence of waveforms already loaded into waveform memory via MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        # Call the method
        inst.set_source_data_sequence(block_descriptor=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_volatile_catalog(self, inst: Keysight33500B):
        # Test Returns the contents of volatile waveform memory, including arbitrary waveforms and sequences.

        # Call the method
        result = inst.get_source_data_volatile_catalog()

        # Verify the response is not None
        assert result is not None

    def test_source_data_volatile_clear(self, inst: Keysight33500B):
        # Test Clears waveform memory for the specified channel and reloads the default waveform.

        # Call the method
        inst.source_data_volatile_clear()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_data_volatile_free(self, inst: Keysight33500B):
        # Test Returns number of points available (free) in volatile memory. 

        # Call the method
        result = inst.get_source_data_volatile_free()

        # Verify the response is not None
        assert result is not None

    def test_get_source_fm_deviation(self, inst: Keysight33500B):
        # Test Sets the peak frequency deviation in Hz. 

        # Call the method
        result = inst.get_source_fm_deviation(peak_deviation_in_Hz=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_deviation(self, inst: Keysight33500B):
        # Test Sets the peak frequency deviation in Hz. 

        # Call the method
        inst.set_source_fm_deviation(peak_deviation_in_Hz=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_internal_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency of the modulating waveform. 

        # Call the method
        result = inst.get_source_fm_internal_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_internal_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency of the modulating waveform. 

        # Call the method
        inst.set_source_fm_internal_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_internal_function(self, inst: Keysight33500B):
        # Test This command selects the shape of the modulating waveform.

        # Call the method
        result = inst.get_source_fm_internal_function(function=['SourAmIntFuncShapeCommandParameter1clone.SINusoid', 'SourAmIntFuncShapeCommandParameter1clone.SQUare', 'SourAmIntFuncShapeCommandParameter1clone.TRIangle', 'SourAmIntFuncShapeCommandParameter1clone.RAMP', 'SourAmIntFuncShapeCommandParameter1clone.NRAMp', 'SourAmIntFuncShapeCommandParameter1clone.NOISe', 'SourAmIntFuncShapeCommandParameter1clone.PRBS', 'SourAmIntFuncShapeCommandParameter1clone.ARB'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_internal_function(self, inst: Keysight33500B):
        # Test This command selects the shape of the modulating waveform.

        # Call the method
        inst.set_source_fm_internal_function(function=['SourAmIntFuncShapeCommandParameter1clone.SINusoid', 'SourAmIntFuncShapeCommandParameter1clone.SQUare', 'SourAmIntFuncShapeCommandParameter1clone.TRIangle', 'SourAmIntFuncShapeCommandParameter1clone.RAMP', 'SourAmIntFuncShapeCommandParameter1clone.NRAMp', 'SourAmIntFuncShapeCommandParameter1clone.NOISe', 'SourAmIntFuncShapeCommandParameter1clone.PRBS', 'SourAmIntFuncShapeCommandParameter1clone.ARB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        result = inst.get_source_fm_source(source=['SourFmSourceCommandParameter1.INTernal', 'SourFmSourceCommandParameter1.EXTernal', 'SourFmSourceCommandParameter1.CH1', 'SourFmSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        inst.set_source_fm_source(source=['SourFmSourceCommandParameter1.INTernal', 'SourFmSourceCommandParameter1.EXTernal', 'SourFmSourceCommandParameter1.CH1', 'SourFmSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fm_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        result = inst.get_source_fm_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_fm_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        inst.set_source_fm_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency(self, inst: Keysight33500B):
        # Test Sets the output frequency.

        # Call the method
        result = inst.get_source_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency(self, inst: Keysight33500B):
        # Test Sets the output frequency.

        # Call the method
        inst.set_source_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_center(self, inst: Keysight33500B):
        # Test Sets the center frequency.

        # Call the method
        result = inst.get_source_frequency_center(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_center(self, inst: Keysight33500B):
        # Test Sets the center frequency.

        # Call the method
        inst.set_source_frequency_center(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_mode(self, inst: Keysight33500B):
        # Test Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        # Call the method
        result = inst.get_source_frequency_couple_mode(mode=['SourFreqCoupModeCommandParameter1.OFFSet', 'SourFreqCoupModeCommandParameter1.RATio'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_mode(self, inst: Keysight33500B):
        # Test Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        # Call the method
        inst.set_source_frequency_couple_mode(mode=['SourFreqCoupModeCommandParameter1.OFFSet', 'SourFreqCoupModeCommandParameter1.RATio'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_offset(self, inst: Keysight33500B):
        # Test Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        # Call the method
        result = inst.get_source_frequency_couple_offset(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_offset(self, inst: Keysight33500B):
        # Test Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        # Call the method
        inst.set_source_frequency_couple_offset(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_ratio(self, inst: Keysight33500B):
        # Test Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        # Call the method
        result = inst.get_source_frequency_couple_ratio(ratio=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_ratio(self, inst: Keysight33500B):
        # Test Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        # Call the method
        inst.set_source_frequency_couple_ratio(ratio=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_couple_state(self, inst: Keysight33500B):
        # Test Enables/disables frequency coupling between channels in a two-channel instrument.

        # Call the method
        result = inst.get_source_frequency_couple_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_couple_state(self, inst: Keysight33500B):
        # Test Enables/disables frequency coupling between channels in a two-channel instrument.

        # Call the method
        inst.set_source_frequency_couple_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_mode(self, inst: Keysight33500B):
        # Test Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        # Call the method
        result = inst.get_source_frequency_mode(mode=['SourFreqModeCommandParameter1.FIXed', 'SourFreqModeCommandParameter1.SWEep', 'SourFreqModeCommandParameter1.CW', 'SourFreqModeCommandParameter1.LIST'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_mode(self, inst: Keysight33500B):
        # Test Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        # Call the method
        inst.set_source_frequency_mode(mode=['SourFreqModeCommandParameter1.FIXed', 'SourFreqModeCommandParameter1.SWEep', 'SourFreqModeCommandParameter1.CW', 'SourFreqModeCommandParameter1.LIST'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_span(self, inst: Keysight33500B):
        # Test Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        # Call the method
        result = inst.get_source_frequency_span(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_span(self, inst: Keysight33500B):
        # Test Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        # Call the method
        inst.set_source_frequency_span(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_start(self, inst: Keysight33500B):
        # Test Sets the start frequencies for a frequency sweep.

        # Call the method
        result = inst.get_source_frequency_start(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_start(self, inst: Keysight33500B):
        # Test Sets the start frequencies for a frequency sweep.

        # Call the method
        inst.set_source_frequency_start(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_frequency_stop(self, inst: Keysight33500B):
        # Test Sets the stop frequencies for a frequency sweep.

        # Call the method
        result = inst.get_source_frequency_stop(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_frequency_stop(self, inst: Keysight33500B):
        # Test Sets the stop frequencies for a frequency sweep.

        # Call the method
        inst.set_source_frequency_stop(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_frequency(self, inst: Keysight33500B):
        # Test Sets the FSK alternate (or "hop") frequency.

        # Call the method
        result = inst.get_source_fskey_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_frequency(self, inst: Keysight33500B):
        # Test Sets the FSK alternate (or "hop") frequency.

        # Call the method
        inst.set_source_fskey_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_internal_rate(self, inst: Keysight33500B):
        # Test Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        # Call the method
        result = inst.get_source_fskey_internal_rate(rate_in_Hz=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_internal_rate(self, inst: Keysight33500B):
        # Test Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        # Call the method
        inst.set_source_fskey_internal_rate(rate_in_Hz=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        result = inst.get_source_fskey_source(source=['SourAmSourceCommandParameter1clone.INTernal', 'SourAmSourceCommandParameter1clone.EXTernal'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        inst.set_source_fskey_source(source=['SourAmSourceCommandParameter1clone.INTernal', 'SourAmSourceCommandParameter1clone.EXTernal'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_fskey_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        result = inst.get_source_fskey_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_fskey_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        inst.set_source_fskey_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function(self, inst: Keysight33500B):
        # Test Selects output function.

        # Call the method
        result = inst.get_source_function(function=['SourFuncShapeCommandParameter1clone.SINusoid', 'SourFuncShapeCommandParameter1clone.SQUare', 'SourFuncShapeCommandParameter1clone.RAMP', 'SourFuncShapeCommandParameter1clone.PULSe', 'SourFuncShapeCommandParameter1clone.ARB', 'SourFuncShapeCommandParameter1clone.TRIangle', 'SourFuncShapeCommandParameter1clone.NOISe', 'SourFuncShapeCommandParameter1clone.PRBS', 'SourFuncShapeCommandParameter1clone.DC'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function(self, inst: Keysight33500B):
        # Test Selects output function.

        # Call the method
        inst.set_source_function(function=['SourFuncShapeCommandParameter1clone.SINusoid', 'SourFuncShapeCommandParameter1clone.SQUare', 'SourFuncShapeCommandParameter1clone.RAMP', 'SourFuncShapeCommandParameter1clone.PULSe', 'SourFuncShapeCommandParameter1clone.ARB', 'SourFuncShapeCommandParameter1clone.TRIangle', 'SourFuncShapeCommandParameter1clone.NOISe', 'SourFuncShapeCommandParameter1clone.PRBS', 'SourFuncShapeCommandParameter1clone.DC'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary(self, inst: Keysight33500B):
        # Test Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        # Call the method
        result = inst.get_source_function_arbitrary(filename=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary(self, inst: Keysight33500B):
        # Test Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        # Call the method
        inst.set_source_function_arbitrary(filename=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_advance(self, inst: Keysight33500B):
        # Test Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        # Call the method
        result = inst.get_source_function_arbitrary_advance(mode=['SourFuncShapArbAdvanceCommandParameter1.TRIGger', 'SourFuncShapArbAdvanceCommandParameter1.SRATe'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_advance(self, inst: Keysight33500B):
        # Test Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        # Call the method
        inst.set_source_function_arbitrary_advance(mode=['SourFuncShapArbAdvanceCommandParameter1.TRIGger', 'SourFuncShapArbAdvanceCommandParameter1.SRATe'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_gain(self, inst: Keysight33500B):
        # Test Sets the gain balance ratio for dual arbitrary waveforms.

        # Call the method
        result = inst.get_source_function_arbitrary_balance_gain(percent=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_gain(self, inst: Keysight33500B):
        # Test Sets the gain balance ratio for dual arbitrary waveforms.

        # Call the method
        inst.set_source_function_arbitrary_balance_gain(percent=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_offset1(self, inst: Keysight33500B):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        result = inst.get_source_function_arbitrary_balance_offset1(volts=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_offset1(self, inst: Keysight33500B):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        inst.set_source_function_arbitrary_balance_offset1(volts=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_offset2(self, inst: Keysight33500B):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        result = inst.get_source_function_arbitrary_balance_offset2(volts=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_offset2(self, inst: Keysight33500B):
        # Test Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        # Call the method
        inst.set_source_function_arbitrary_balance_offset2(volts=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_balance_state(self, inst: Keysight33500B):
        # Test Enables or disables channel balancing for dual arbitrary waveforms 

        # Call the method
        result = inst.get_source_function_arbitrary_balance_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_balance_state(self, inst: Keysight33500B):
        # Test Enables or disables channel balancing for dual arbitrary waveforms 

        # Call the method
        inst.set_source_function_arbitrary_balance_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_filter(self, inst: Keysight33500B):
        # Test Specifies the filter setting for an arbitrary waveform.

        # Call the method
        result = inst.get_source_function_arbitrary_filter(filter=['SourFuncShapArbFilterCommandParameter1.OFF', 'SourFuncShapArbFilterCommandParameter1.NORMal', 'SourFuncShapArbFilterCommandParameter1.STEP'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_filter(self, inst: Keysight33500B):
        # Test Specifies the filter setting for an arbitrary waveform.

        # Call the method
        inst.set_source_function_arbitrary_filter(filter=['SourFuncShapArbFilterCommandParameter1.OFF', 'SourFuncShapArbFilterCommandParameter1.NORMal', 'SourFuncShapArbFilterCommandParameter1.STEP'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency for the arbitrary waveform.



        # Call the method
        result = inst.get_source_function_arbitrary_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency for the arbitrary waveform.



        # Call the method
        inst.set_source_function_arbitrary_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_period(self, inst: Keysight33500B):
        # Test Sets the period for the arbitrary waveform.

        # Call the method
        result = inst.get_source_function_arbitrary_period(period=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_period(self, inst: Keysight33500B):
        # Test Sets the period for the arbitrary waveform.

        # Call the method
        inst.set_source_function_arbitrary_period(period=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_points(self, inst: Keysight33500B):
        # Test Returns the number of points in the currently selected arbitrary waveform.

        # Call the method
        result = inst.get_source_function_arbitrary_points()

        # Verify the response is not None
        assert result is not None

    def test_get_source_function_arbitrary_ptpeak(self, inst: Keysight33500B):
        # Test Sets peak to peak voltage.

        # Call the method
        result = inst.get_source_function_arbitrary_ptpeak(voltage=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_ptpeak(self, inst: Keysight33500B):
        # Test Sets peak to peak voltage.

        # Call the method
        inst.set_source_function_arbitrary_ptpeak(voltage=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_skew_state(self, inst: Keysight33500B):
        # Test Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        # Call the method
        result = inst.get_source_function_arbitrary_skew_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_skew_state(self, inst: Keysight33500B):
        # Test Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        # Call the method
        inst.set_source_function_arbitrary_skew_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_skew_time(self, inst: Keysight33500B):
        # Test Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        # Call the method
        result = inst.get_source_function_arbitrary_skew_time(time=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_skew_time(self, inst: Keysight33500B):
        # Test Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        # Call the method
        inst.set_source_function_arbitrary_skew_time(time=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_arbitrary_srate(self, inst: Keysight33500B):
        # Test Sets the sample rate for the arbitrary waveform.

        # Call the method
        result = inst.get_source_function_arbitrary_srate(sample_rate=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_arbitrary_srate(self, inst: Keysight33500B):
        # Test Sets the sample rate for the arbitrary waveform.

        # Call the method
        inst.set_source_function_arbitrary_srate(sample_rate=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_function_arbitrary_synchronize(self, inst: Keysight33500B):
        # Test Causes two independent arbitrary waveforms to synchronize to first point of each waveform (two-channel instruments only).

        # Call the method
        inst.source_function_arbitrary_synchronize()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_noise_bandwidth(self, inst: Keysight33500B):
        # Test Sets bandwidth of noise function.

        # Call the method
        result = inst.get_source_function_noise_bandwidth(bandwidth=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_noise_bandwidth(self, inst: Keysight33500B):
        # Test Sets bandwidth of noise function.

        # Call the method
        inst.set_source_function_noise_bandwidth(bandwidth=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_prbs_brate(self, inst: Keysight33500B):
        # Test Sets the pseudo-random binary sequence (PRBS) bit rate.

        # Call the method
        result = inst.get_source_function_prbs_brate(bit_rate=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_prbs_brate(self, inst: Keysight33500B):
        # Test Sets the pseudo-random binary sequence (PRBS) bit rate.

        # Call the method
        inst.set_source_function_prbs_brate(bit_rate=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_prbs_data(self, inst: Keysight33500B):
        # Test Sets the pseudo-random binary sequence (PRBS) type. 

        # Call the method
        result = inst.get_source_function_prbs_data(sequence_type=['SourFuncShapPrbsDataCommandParameter1.PN7', 'SourFuncShapPrbsDataCommandParameter1.PN9', 'SourFuncShapPrbsDataCommandParameter1.PN11', 'SourFuncShapPrbsDataCommandParameter1.PN15', 'SourFuncShapPrbsDataCommandParameter1.PN20', 'SourFuncShapPrbsDataCommandParameter1.PN23'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_prbs_data(self, inst: Keysight33500B):
        # Test Sets the pseudo-random binary sequence (PRBS) type. 

        # Call the method
        inst.set_source_function_prbs_data(sequence_type=['SourFuncShapPrbsDataCommandParameter1.PN7', 'SourFuncShapPrbsDataCommandParameter1.PN9', 'SourFuncShapPrbsDataCommandParameter1.PN11', 'SourFuncShapPrbsDataCommandParameter1.PN15', 'SourFuncShapPrbsDataCommandParameter1.PN20', 'SourFuncShapPrbsDataCommandParameter1.PN23'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_prbs_transition_both(self, inst: Keysight33500B):
        # Test Sets PRBS transition edge time on both edges of a PRBS transition.

        # Call the method
        result = inst.get_source_function_prbs_transition_both(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_prbs_transition_both(self, inst: Keysight33500B):
        # Test Sets PRBS transition edge time on both edges of a PRBS transition.

        # Call the method
        inst.set_source_function_prbs_transition_both(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_dcycle(self, inst: Keysight33500B):
        # Test Sets pulse duty cycle.

        # Call the method
        result = inst.get_source_function_pulse_dcycle(percent=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_dcycle(self, inst: Keysight33500B):
        # Test Sets pulse duty cycle.

        # Call the method
        inst.set_source_function_pulse_dcycle(percent=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_hold(self, inst: Keysight33500B):
        # Test Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        # Call the method
        result = inst.get_source_function_pulse_hold(pulse=['SourFuncShapPulsHoldCommandParameter1.WIDTh', 'SourFuncShapPulsHoldCommandParameter1.DCYCle'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_hold(self, inst: Keysight33500B):
        # Test Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        # Call the method
        inst.set_source_function_pulse_hold(pulse=['SourFuncShapPulsHoldCommandParameter1.WIDTh', 'SourFuncShapPulsHoldCommandParameter1.DCYCle'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_period(self, inst: Keysight33500B):
        # Test Sets the period for pulse waveforms.

        # Call the method
        result = inst.get_source_function_pulse_period(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_period(self, inst: Keysight33500B):
        # Test Sets the period for pulse waveforms.

        # Call the method
        inst.set_source_function_pulse_period(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_transition_both(self, inst: Keysight33500B):
        # Test Sets the pulse edge time on both edges of a pulse.

        # Call the method
        result = inst.get_source_function_pulse_transition_both(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_transition_both(self, inst: Keysight33500B):
        # Test Sets the pulse edge time on both edges of a pulse.

        # Call the method
        inst.set_source_function_pulse_transition_both(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_transition_leading(self, inst: Keysight33500B):
        # Test Sets the pulse edge time on the leading edges of a pulse.



        # Call the method
        result = inst.get_source_function_pulse_transition_leading(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_transition_leading(self, inst: Keysight33500B):
        # Test Sets the pulse edge time on the leading edges of a pulse.



        # Call the method
        inst.set_source_function_pulse_transition_leading(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_transition_trailing(self, inst: Keysight33500B):
        # Test Sets the pulse edge time on the trailing edges of a pulse.



        # Call the method
        result = inst.get_source_function_pulse_transition_trailing(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_transition_trailing(self, inst: Keysight33500B):
        # Test Sets the pulse edge time on the trailing edges of a pulse.



        # Call the method
        inst.set_source_function_pulse_transition_trailing(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_pulse_width(self, inst: Keysight33500B):
        # Test Sets pulse width.

        # Call the method
        result = inst.get_source_function_pulse_width(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_pulse_width(self, inst: Keysight33500B):
        # Test Sets pulse width.

        # Call the method
        inst.set_source_function_pulse_width(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_ramp_symmetry(self, inst: Keysight33500B):
        # Test Sets the symmetry percentage for ramp waves.

        # Call the method
        result = inst.get_source_function_ramp_symmetry(percent=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_ramp_symmetry(self, inst: Keysight33500B):
        # Test Sets the symmetry percentage for ramp waves.

        # Call the method
        inst.set_source_function_ramp_symmetry(percent=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_square_dcycle(self, inst: Keysight33500B):
        # Test Sets duty cycle percentage for square wave.

        # Call the method
        result = inst.get_source_function_square_dcycle(percent=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_square_dcycle(self, inst: Keysight33500B):
        # Test Sets duty cycle percentage for square wave.

        # Call the method
        inst.set_source_function_square_dcycle(percent=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_function_square_period(self, inst: Keysight33500B):
        # Test Sets period for square wave.

        # Call the method
        result = inst.get_source_function_square_period(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_function_square_period(self, inst: Keysight33500B):
        # Test Sets period for square wave.

        # Call the method
        inst.set_source_function_square_period(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_list_dwell(self, inst: Keysight33500B):
        # Test Sets dwell time, the amount of time each frequency in a frequency list is generated.

        # Call the method
        result = inst.get_source_list_dwell(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_list_dwell(self, inst: Keysight33500B):
        # Test Sets dwell time, the amount of time each frequency in a frequency list is generated.

        # Call the method
        inst.set_source_list_dwell(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_list_frequency(self, inst: Keysight33500B):
        # Test Specifies frequency values in a frequency list.

        # Call the method
        result = inst.get_source_list_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_list_frequency(self, inst: Keysight33500B):
        # Test Specifies frequency values in a frequency list.

        # Call the method
        inst.set_source_list_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_list_frequency_points(self, inst: Keysight33500B):
        # Test Returns number of frequencies in current frequency list.

        # Call the method
        result = inst.get_source_list_frequency_points()

        # Verify the response is not None
        assert result is not None

    def test_get_source_marker_cycle(self, inst: Keysight33500B):
        # Test Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        # Call the method
        result = inst.get_source_marker_cycle(cycle_num=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_cycle(self, inst: Keysight33500B):
        # Test Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        # Call the method
        inst.set_source_marker_cycle(cycle_num=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_marker_frequency(self, inst: Keysight33500B):
        # Test Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        # Call the method
        result = inst.get_source_marker_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_frequency(self, inst: Keysight33500B):
        # Test Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        # Call the method
        inst.set_source_marker_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_marker_point(self, inst: Keysight33500B):
        # Test Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        # Call the method
        result = inst.get_source_marker_point(sample_number=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_marker_point(self, inst: Keysight33500B):
        # Test Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        # Call the method
        inst.set_source_marker_point(sample_number=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_modulation_phase(self, inst: Keysight33500B):
        # Test Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        # Call the method
        result = inst.get_source_modulation_phase(angle=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_modulation_phase(self, inst: Keysight33500B):
        # Test Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        # Call the method
        inst.set_source_modulation_phase(angle=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_phase_reference(self, inst: Keysight33500B):
        # Test Simultaneously removes the offset set by PHASe and adjusts the primary phase generator by an amount equivalent to the PHASe setting.

        # Call the method
        inst.source_phase_reference()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_source_phase_synchronize(self, inst: Keysight33500B):
        # Test Simultaneously resets all phase generators in the instrument, including the modulation phase generators, to establish a common, internal phase zero reference point.

        # Call the method
        inst.source_phase_synchronize()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_phase_unlock_error_state(self, inst: Keysight33500B):
        # Test Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        # Call the method
        result = inst.get_source_phase_unlock_error_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_phase_unlock_error_state(self, inst: Keysight33500B):
        # Test Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        # Call the method
        inst.set_source_phase_unlock_error_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_deviation(self, inst: Keysight33500B):
        # Test Sets the phase deviation in degrees. 

        # Call the method
        result = inst.get_source_pm_deviation(deviation_in_degrees=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_deviation(self, inst: Keysight33500B):
        # Test Sets the phase deviation in degrees. 

        # Call the method
        inst.set_source_pm_deviation(deviation_in_degrees=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_internal_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency of the modulating waveform.

        # Call the method
        result = inst.get_source_pm_internal_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_internal_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency of the modulating waveform.

        # Call the method
        inst.set_source_pm_internal_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_internal_function(self, inst: Keysight33500B):
        # Test Selects shape of modulating waveform.

        # Call the method
        result = inst.get_source_pm_internal_function(function=['SourAmIntFuncShapeCommandParameter1clone.SINusoid', 'SourAmIntFuncShapeCommandParameter1clone.SQUare', 'SourAmIntFuncShapeCommandParameter1clone.TRIangle', 'SourAmIntFuncShapeCommandParameter1clone.RAMP', 'SourAmIntFuncShapeCommandParameter1clone.NRAMp', 'SourAmIntFuncShapeCommandParameter1clone.NOISe', 'SourAmIntFuncShapeCommandParameter1clone.PRBS', 'SourAmIntFuncShapeCommandParameter1clone.ARB'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_internal_function(self, inst: Keysight33500B):
        # Test Selects shape of modulating waveform.

        # Call the method
        inst.set_source_pm_internal_function(function=['SourAmIntFuncShapeCommandParameter1clone.SINusoid', 'SourAmIntFuncShapeCommandParameter1clone.SQUare', 'SourAmIntFuncShapeCommandParameter1clone.TRIangle', 'SourAmIntFuncShapeCommandParameter1clone.RAMP', 'SourAmIntFuncShapeCommandParameter1clone.NRAMp', 'SourAmIntFuncShapeCommandParameter1clone.NOISe', 'SourAmIntFuncShapeCommandParameter1clone.PRBS', 'SourAmIntFuncShapeCommandParameter1clone.ARB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        result = inst.get_source_pm_source(source=['SourPmSourceCommandParameter1.INTernal', 'SourPmSourceCommandParameter1.EXTernal', 'SourPmSourceCommandParameter1.CH1', 'SourPmSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        inst.set_source_pm_source(source=['SourPmSourceCommandParameter1.INTernal', 'SourPmSourceCommandParameter1.EXTernal', 'SourPmSourceCommandParameter1.CH1', 'SourPmSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pm_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        result = inst.get_source_pm_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_pm_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        inst.set_source_pm_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_deviation(self, inst: Keysight33500B):
        # Test Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        # Call the method
        result = inst.get_source_pwm_deviation(deviation=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_deviation(self, inst: Keysight33500B):
        # Test Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        # Call the method
        inst.set_source_pwm_deviation(deviation=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_deviation_dcycle(self, inst: Keysight33500B):
        # Test Sets duty cycle deviation in percent of period.

        # Call the method
        result = inst.get_source_pwm_deviation_dcycle(deviation_in_pct=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_deviation_dcycle(self, inst: Keysight33500B):
        # Test Sets duty cycle deviation in percent of period.

        # Call the method
        inst.set_source_pwm_deviation_dcycle(deviation_in_pct=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_internal_frequency(self, inst: Keysight33500B):
        # Test Selects frequency at which output pulse width shifts through its pulse width deviation.

        # Call the method
        result = inst.get_source_pwm_internal_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_internal_frequency(self, inst: Keysight33500B):
        # Test Selects frequency at which output pulse width shifts through its pulse width deviation.

        # Call the method
        inst.set_source_pwm_internal_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_internal_function(self, inst: Keysight33500B):
        # Test Selects shape of the internal modulating waveform.

        # Call the method
        result = inst.get_source_pwm_internal_function(function=['SourSumIntFunctionCommandParameter1clone.SINusoid', 'SourSumIntFunctionCommandParameter1clone.SQUare', 'SourSumIntFunctionCommandParameter1clone.TRIangle', 'SourSumIntFunctionCommandParameter1clone.RAMP', 'SourSumIntFunctionCommandParameter1clone.NRAMp', 'SourSumIntFunctionCommandParameter1clone.NOISe', 'SourSumIntFunctionCommandParameter1clone.PRBS', 'SourSumIntFunctionCommandParameter1clone.ARB'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_internal_function(self, inst: Keysight33500B):
        # Test Selects shape of the internal modulating waveform.

        # Call the method
        inst.set_source_pwm_internal_function(function=['SourSumIntFunctionCommandParameter1clone.SINusoid', 'SourSumIntFunctionCommandParameter1clone.SQUare', 'SourSumIntFunctionCommandParameter1clone.TRIangle', 'SourSumIntFunctionCommandParameter1clone.RAMP', 'SourSumIntFunctionCommandParameter1clone.NRAMp', 'SourSumIntFunctionCommandParameter1clone.NOISe', 'SourSumIntFunctionCommandParameter1clone.PRBS', 'SourSumIntFunctionCommandParameter1clone.ARB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        result = inst.get_source_pwm_source(source=['SourPwmSourceCommandParameter1.INTernal', 'SourPwmSourceCommandParameter1.EXTernal', 'SourPwmSourceCommandParameter1.CH1', 'SourPwmSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_source(self, inst: Keysight33500B):
        # Test Select the source of the modulating signal.

        # Call the method
        inst.set_source_pwm_source(source=['SourPwmSourceCommandParameter1.INTernal', 'SourPwmSourceCommandParameter1.EXTernal', 'SourPwmSourceCommandParameter1.CH1', 'SourPwmSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_pwm_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        result = inst.get_source_pwm_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_pwm_state(self, inst: Keysight33500B):
        # Test Enables or disables modulation.

        # Call the method
        inst.set_source_pwm_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_mode(self, inst: Keysight33500B):
        # Test Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        # Call the method
        result = inst.get_source_rate_couple_mode(mode=['SourRateCoupModeCommandParameter1.OFFSet', 'SourRateCoupModeCommandParameter1.RATio'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_mode(self, inst: Keysight33500B):
        # Test Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        # Call the method
        inst.set_source_rate_couple_mode(mode=['SourRateCoupModeCommandParameter1.OFFSet', 'SourRateCoupModeCommandParameter1.RATio'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_offset(self, inst: Keysight33500B):
        # Test Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        # Call the method
        result = inst.get_source_rate_couple_offset(sample_rate=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_offset(self, inst: Keysight33500B):
        # Test Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        # Call the method
        inst.set_source_rate_couple_offset(sample_rate=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_ratio(self, inst: Keysight33500B):
        # Test Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        # Call the method
        result = inst.get_source_rate_couple_ratio(ratio=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_ratio(self, inst: Keysight33500B):
        # Test Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        # Call the method
        inst.set_source_rate_couple_ratio(ratio=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_rate_couple_state(self, inst: Keysight33500B):
        # Test Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        # Call the method
        result = inst.get_source_rate_couple_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_rate_couple_state(self, inst: Keysight33500B):
        # Test Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        # Call the method
        inst.set_source_rate_couple_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_roscillator_source(self, inst: Keysight33500B):
        # Test Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        # Call the method
        result = inst.get_source_roscillator_source(source=['SourRoscSourceCommandParameter1.INTernal', 'SourRoscSourceCommandParameter1.EXTernal'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_roscillator_source(self, inst: Keysight33500B):
        # Test Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        # Call the method
        inst.set_source_roscillator_source(source=['SourRoscSourceCommandParameter1.INTernal', 'SourRoscSourceCommandParameter1.EXTernal'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_roscillator_source_auto(self, inst: Keysight33500B):
        # Test Disables or enables automatic selection of the reference oscillator.

        # Call the method
        result = inst.get_source_roscillator_source_auto(state=['SourRoscSourAutoCommandParameter1.OFF', 'SourRoscSourAutoCommandParameter1.ON'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_roscillator_source_auto(self, inst: Keysight33500B):
        # Test Disables or enables automatic selection of the reference oscillator.

        # Call the method
        inst.set_source_roscillator_source_auto(state=['SourRoscSourAutoCommandParameter1.OFF', 'SourRoscSourAutoCommandParameter1.ON'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_roscillator_source_current(self, inst: Keysight33500B):
        # Test Indicates which reference oscillator signal is currently in use when ROSC:SOURce:AUTO is ON.

        # Call the method
        result = inst.get_source_roscillator_source_current()

        # Verify the response is not None
        assert result is not None

    def test_get_source_sum_amplitude(self, inst: Keysight33500B):
        # Test Sets internal modulation depth (or "percent modulation") in percent.

        # Call the method
        result = inst.get_source_sum_amplitude(amplitude=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_amplitude(self, inst: Keysight33500B):
        # Test Sets internal modulation depth (or "percent modulation") in percent.

        # Call the method
        inst.set_source_sum_amplitude(amplitude=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_internal_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        # Call the method
        result = inst.get_source_sum_internal_frequency(frequency=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_internal_frequency(self, inst: Keysight33500B):
        # Test Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        # Call the method
        inst.set_source_sum_internal_frequency(frequency=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_internal_function(self, inst: Keysight33500B):
        # Test Selects the summing waveform (the waveform added to the primary waveform).

        # Call the method
        result = inst.get_source_sum_internal_function(function=['SourSumIntFunctionCommandParameter1clone.SINusoid', 'SourSumIntFunctionCommandParameter1clone.SQUare', 'SourSumIntFunctionCommandParameter1clone.TRIangle', 'SourSumIntFunctionCommandParameter1clone.RAMP', 'SourSumIntFunctionCommandParameter1clone.NRAMp', 'SourSumIntFunctionCommandParameter1clone.NOISe', 'SourSumIntFunctionCommandParameter1clone.PRBS', 'SourSumIntFunctionCommandParameter1clone.ARB'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_internal_function(self, inst: Keysight33500B):
        # Test Selects the summing waveform (the waveform added to the primary waveform).

        # Call the method
        inst.set_source_sum_internal_function(function=['SourSumIntFunctionCommandParameter1clone.SINusoid', 'SourSumIntFunctionCommandParameter1clone.SQUare', 'SourSumIntFunctionCommandParameter1clone.TRIangle', 'SourSumIntFunctionCommandParameter1clone.RAMP', 'SourSumIntFunctionCommandParameter1clone.NRAMp', 'SourSumIntFunctionCommandParameter1clone.NOISe', 'SourSumIntFunctionCommandParameter1clone.PRBS', 'SourSumIntFunctionCommandParameter1clone.ARB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_source(self, inst: Keysight33500B):
        # Test Selects source of summing signal.

        # Call the method
        result = inst.get_source_sum_source(source=['SourAmSourceCommandParameter1.INTernal', 'SourAmSourceCommandParameter1.EXTernal', 'SourAmSourceCommandParameter1.CH1', 'SourAmSourceCommandParameter1.CH2'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_source(self, inst: Keysight33500B):
        # Test Selects source of summing signal.

        # Call the method
        inst.set_source_sum_source(source=['SourAmSourceCommandParameter1.INTernal', 'SourAmSourceCommandParameter1.EXTernal', 'SourAmSourceCommandParameter1.CH1', 'SourAmSourceCommandParameter1.CH2'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sum_state(self, inst: Keysight33500B):
        # Test Disables or enables SUM function.

        # Call the method
        result = inst.get_source_sum_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_sum_state(self, inst: Keysight33500B):
        # Test Disables or enables SUM function.

        # Call the method
        inst.set_source_sum_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_htime(self, inst: Keysight33500B):
        # Test Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        # Call the method
        result = inst.get_source_sweep_htime(hold_time=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_htime(self, inst: Keysight33500B):
        # Test Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        # Call the method
        inst.set_source_sweep_htime(hold_time=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_rtime(self, inst: Keysight33500B):
        # Test Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        # Call the method
        result = inst.get_source_sweep_rtime(return_time=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_rtime(self, inst: Keysight33500B):
        # Test Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        # Call the method
        inst.set_source_sweep_rtime(return_time=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_spacing(self, inst: Keysight33500B):
        # Test Selects linear or logarithmic spacing for sweep.

        # Call the method
        result = inst.get_source_sweep_spacing(spacing=['SourSweSpacingCommandParameter1.LINear', 'SourSweSpacingCommandParameter1.LOGarithmic'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_spacing(self, inst: Keysight33500B):
        # Test Selects linear or logarithmic spacing for sweep.

        # Call the method
        inst.set_source_sweep_spacing(spacing=['SourSweSpacingCommandParameter1.LINear', 'SourSweSpacingCommandParameter1.LOGarithmic'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_state(self, inst: Keysight33500B):
        # Test Enables or disables the sweep.

        # Call the method
        result = inst.get_source_sweep_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_state(self, inst: Keysight33500B):
        # Test Enables or disables the sweep.

        # Call the method
        inst.set_source_sweep_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_sweep_time(self, inst: Keysight33500B):
        # Test Sets time (seconds) to sweep from start frequency to stop frequency.

        # Call the method
        result = inst.get_source_sweep_time(seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_sweep_time(self, inst: Keysight33500B):
        # Test Sets time (seconds) to sweep from start frequency to stop frequency.

        # Call the method
        inst.set_source_sweep_time(seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_track(self, inst: Keysight33500B):
        # Test Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        # Call the method
        result = inst.get_source_track(track=['SourTrackCommandParameter1.OFF', 'SourTrackCommandParameter1.ON', 'SourTrackCommandParameter1.INVerted'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_track(self, inst: Keysight33500B):
        # Test Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        # Call the method
        inst.set_source_track(track=['SourTrackCommandParameter1.OFF', 'SourTrackCommandParameter1.ON', 'SourTrackCommandParameter1.INVerted'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage(self, inst: Keysight33500B):
        # Test Sets output amplitude.

        # Call the method
        result = inst.get_source_voltage(amplitude=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage(self, inst: Keysight33500B):
        # Test Sets output amplitude.

        # Call the method
        inst.set_source_voltage(amplitude=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_limit_high(self, inst: Keysight33500B):
        # Test Sets the high limits for output voltage.



        # Call the method
        result = inst.get_source_voltage_limit_high(voltage=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_limit_high(self, inst: Keysight33500B):
        # Test Sets the high limits for output voltage.



        # Call the method
        inst.set_source_voltage_limit_high(voltage=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_limit_low(self, inst: Keysight33500B):
        # Test Sets the low limits for output voltage.



        # Call the method
        result = inst.get_source_voltage_limit_low(voltage=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_limit_low(self, inst: Keysight33500B):
        # Test Sets the low limits for output voltage.



        # Call the method
        inst.set_source_voltage_limit_low(voltage=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_limit_state(self, inst: Keysight33500B):
        # Test Enables or disables output amplitude voltage limits.

        # Call the method
        result = inst.get_source_voltage_limit_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_limit_state(self, inst: Keysight33500B):
        # Test Enables or disables output amplitude voltage limits.

        # Call the method
        inst.set_source_voltage_limit_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_range_auto(self, inst: Keysight33500B):
        # Test Disables or enables voltage autoranging for all functions.

        # Call the method
        result = inst.get_source_voltage_range_auto(state=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_range_auto(self, inst: Keysight33500B):
        # Test Disables or enables voltage autoranging for all functions.

        # Call the method
        inst.set_source_voltage_range_auto(state=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_unit(self, inst: Keysight33500B):
        # Test Selects the units for output amplitude.

        # Call the method
        result = inst.get_source_voltage_unit(unit=['SourVoltLevUnitCommandParameter1.VPP', 'SourVoltLevUnitCommandParameter1.VRMS', 'SourVoltLevUnitCommandParameter1.DBM'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_unit(self, inst: Keysight33500B):
        # Test Selects the units for output amplitude.

        # Call the method
        inst.set_source_voltage_unit(unit=['SourVoltLevUnitCommandParameter1.VPP', 'SourVoltLevUnitCommandParameter1.VRMS', 'SourVoltLevUnitCommandParameter1.DBM'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_couple_state(self, inst: Keysight33500B):
        # Test Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        # Call the method
        result = inst.get_source_voltage_couple_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_couple_state(self, inst: Keysight33500B):
        # Test Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        # Call the method
        inst.set_source_voltage_couple_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_high(self, inst: Keysight33500B):
        # Test Set the waveform's high voltage levels.

        # Call the method
        result = inst.get_source_voltage_high(voltage=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_high(self, inst: Keysight33500B):
        # Test Set the waveform's high voltage levels.

        # Call the method
        inst.set_source_voltage_high(voltage=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_low(self, inst: Keysight33500B):
        # Test Set the waveform's low voltage levels.

        # Call the method
        result = inst.get_source_voltage_low(voltage=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_low(self, inst: Keysight33500B):
        # Test Set the waveform's low voltage levels.

        # Call the method
        inst.set_source_voltage_low(voltage=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_source_voltage_offset(self, inst: Keysight33500B):
        # Test Sets DC offset voltage.

        # Call the method
        result = inst.get_source_voltage_offset(offset=1)

        # Verify the response is not None
        assert result is not None

    def test_set_source_voltage_offset(self, inst: Keysight33500B):
        # Test Sets DC offset voltage.

        # Call the method
        inst.set_source_voltage_offset(offset=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_operation_condition(self, inst: Keysight33500B):
        # Test Queries the condition register for the Standard Operation Register group. 

        # Call the method
        result = inst.get_status_operation_condition()

        # Verify the response is not None
        assert result is not None

    def test_get_status_operation_enable(self, inst: Keysight33500B):
        # Test Enables bits in the enable register for the Standard Operation Register group.

        # Call the method
        result = inst.get_status_operation_enable(enable_value=1)

        # Verify the response is not None
        assert result is not None

    def test_set_status_operation_enable(self, inst: Keysight33500B):
        # Test Enables bits in the enable register for the Standard Operation Register group.

        # Call the method
        inst.set_status_operation_enable(enable_value=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_operation_event(self, inst: Keysight33500B):
        # Test Queries the event register for the Standard Operation Register group.

        # Call the method
        result = inst.get_status_operation_event()

        # Verify the response is not None
        assert result is not None

    def test_status_preset(self, inst: Keysight33500B):
        # Test Clears Questionable Data enable register and Standard Operation enable register.

        # Call the method
        inst.status_preset()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_questionable_condition(self, inst: Keysight33500B):
        # Test Queries the condition register for the Questionable Data Register group.

        # Call the method
        result = inst.get_status_questionable_condition()

        # Verify the response is not None
        assert result is not None

    def test_get_status_questionable_enable(self, inst: Keysight33500B):
        # Test Enables bits in the enable register for the Questionable Data Register group. 

        # Call the method
        result = inst.get_status_questionable_enable(enable_value=1)

        # Verify the response is not None
        assert result is not None

    def test_set_status_questionable_enable(self, inst: Keysight33500B):
        # Test Enables bits in the enable register for the Questionable Data Register group. 

        # Call the method
        inst.set_status_questionable_enable(enable_value=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_status_questionable_event(self, inst: Keysight33500B):
        # Test Queries the event register for the Questionable Data Register group. 

        # Call the method
        result = inst.get_status_questionable_event()

        # Verify the response is not None
        assert result is not None

    def test_system_beeper_immediate(self, inst: Keysight33500B):
        # Test Issues a single beep.

        # Call the method
        inst.system_beeper_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_beeper_state(self, inst: Keysight33500B):
        # Test Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        # Call the method
        result = inst.get_system_beeper_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_system_beeper_state(self, inst: Keysight33500B):
        # Test Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        # Call the method
        inst.set_system_beeper_state(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_enable(self, inst: Keysight33500B):
        # Test Disables or enables the GPIB, USB, or LAN remote interface.

        # Call the method
        result = inst.get_system_communicate_enable(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'], interface=['SystCommEnableCommandParameter2clone.GPIB', 'SystCommEnableCommandParameter2clone.USB', 'SystCommEnableCommandParameter2clone.LAN', 'SystCommEnableCommandParameter2clone.SOCKets', 'SystCommEnableCommandParameter2clone.TELNet', 'SystCommEnableCommandParameter2clone.VXI11', 'SystCommEnableCommandParameter2clone.WEB'])

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_enable(self, inst: Keysight33500B):
        # Test Disables or enables the GPIB, USB, or LAN remote interface.

        # Call the method
        inst.set_system_communicate_enable(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'], interface=['SystCommEnableCommandParameter2clone.GPIB', 'SystCommEnableCommandParameter2clone.USB', 'SystCommEnableCommandParameter2clone.LAN', 'SystCommEnableCommandParameter2clone.SOCKets', 'SystCommEnableCommandParameter2clone.TELNet', 'SystCommEnableCommandParameter2clone.VXI11', 'SystCommEnableCommandParameter2clone.WEB'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_gpib_address(self, inst: Keysight33500B):
        # Test Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        # Call the method
        result = inst.get_system_communicate_gpib_address(address=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_gpib_address(self, inst: Keysight33500B):
        # Test Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        # Call the method
        inst.set_system_communicate_gpib_address(address=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_control(self, inst: Keysight33500B):
        # Test Reads the initial Control connection port number for Sockets communications.

        # Call the method
        result = inst.get_system_communicate_lan_control()

        # Verify the response is not None
        assert result is not None

    def test_get_system_communicate_lan_dhcp(self, inst: Keysight33500B):
        # Test Disables or enables instrument's use of DHCP.

        # Call the method
        result = inst.get_system_communicate_lan_dhcp(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_dhcp(self, inst: Keysight33500B):
        # Test Disables or enables instrument's use of DHCP.

        # Call the method
        inst.set_system_communicate_lan_dhcp(state=['Enum33500bBoolean.ON', 'Enum33500bBoolean.OFF'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_dns(self, inst: Keysight33500B):
        # Test Assigns static IP addresses of Domain Name System (DNS) servers.

        # Call the method
        result = inst.get_system_communicate_lan_dns(dns_num=1, address=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_dns(self, inst: Keysight33500B):
        # Test Assigns static IP addresses of Domain Name System (DNS) servers.

        # Call the method
        inst.set_system_communicate_lan_dns(dns_num=1, address=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_domain(self, inst: Keysight33500B):
        # Test Returns the domain name of the LAN to which the instrument is connected.

        # Call the method
        result = inst.get_system_communicate_lan_domain()

        # Verify the response is not None
        assert result is not None

    def test_get_system_communicate_lan_gateway(self, inst: Keysight33500B):
        # Test Assigns a default gateway for the instrument.

        # Call the method
        result = inst.get_system_communicate_lan_gateway(address=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_gateway(self, inst: Keysight33500B):
        # Test Assigns a default gateway for the instrument.

        # Call the method
        inst.set_system_communicate_lan_gateway(address=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_hostname(self, inst: Keysight33500B):
        # Test Assigns a hostname to the instrument.

        # Call the method
        result = inst.get_system_communicate_lan_hostname(name=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_hostname(self, inst: Keysight33500B):
        # Test Assigns a hostname to the instrument.

        # Call the method
        inst.set_system_communicate_lan_hostname(name=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_ipaddress(self, inst: Keysight33500B):
        # Test Assigns a static Internet Protocol (IP) address for the instrument. 

        # Call the method
        result = inst.get_system_communicate_lan_ipaddress(address=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_ipaddress(self, inst: Keysight33500B):
        # Test Assigns a static Internet Protocol (IP) address for the instrument. 

        # Call the method
        inst.set_system_communicate_lan_ipaddress(address=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_mac(self, inst: Keysight33500B):
        # Test Reads the instrument's Media Access Control (MAC) address.

        # Call the method
        result = inst.get_system_communicate_lan_mac()

        # Verify the response is not None
        assert result is not None

    def test_get_system_communicate_lan_smask(self, inst: Keysight33500B):
        # Test Assigns a subnet mask for the instrument. 

        # Call the method
        result = inst.get_system_communicate_lan_smask(mask=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_smask(self, inst: Keysight33500B):
        # Test Assigns a subnet mask for the instrument. 

        # Call the method
        inst.set_system_communicate_lan_smask(mask=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_telnet_prompt(self, inst: Keysight33500B):
        # Test Sets the command prompt seen when communicating with the instrument via Telnet.

        # Call the method
        result = inst.get_system_communicate_lan_telnet_prompt(string=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_telnet_prompt(self, inst: Keysight33500B):
        # Test Sets the command prompt seen when communicating with the instrument via Telnet.

        # Call the method
        inst.set_system_communicate_lan_telnet_prompt(string=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_telnet_wmessage(self, inst: Keysight33500B):
        # Test Sets welcome message seen when communicating with instrument via Telnet.

        # Call the method
        result = inst.get_system_communicate_lan_telnet_wmessage(string=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_telnet_wmessage(self, inst: Keysight33500B):
        # Test Sets welcome message seen when communicating with instrument via Telnet.

        # Call the method
        inst.set_system_communicate_lan_telnet_wmessage(string=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_system_communicate_lan_update(self, inst: Keysight33500B):
        # Test Stores any changes made to the LAN settings into non-volatile memory and restarts the LAN driver with the updated settings.

        # Call the method
        inst.system_communicate_lan_update()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_communicate_lan_wins(self, inst: Keysight33500B):
        # Test Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        # Call the method
        result = inst.get_system_communicate_lan_wins(wins_num=1, address=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_communicate_lan_wins(self, inst: Keysight33500B):
        # Test Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        # Call the method
        inst.set_system_communicate_lan_wins(wins_num=1, address=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_date(self, inst: Keysight33500B):
        # Test Sets system clock date.

        # Call the method
        result = inst.get_system_date(year=1, month=1, day=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_date(self, inst: Keysight33500B):
        # Test Sets system clock date.

        # Call the method
        inst.set_system_date(year=1, month=1, day=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_error(self, inst: Keysight33500B):
        # Test Reads and clears one error from error queue.

        # Call the method
        result = inst.get_system_error()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_catalog(self, inst: Keysight33500B):
        # Test Returns a comma separated list of installed, licensed options.

        # Call the method
        result = inst.get_system_license_catalog()

        # Verify the response is not None
        assert result is not None

    def test_set_system_license_delete(self, inst: Keysight33500B):
        # Test Deletes a license.

        # Call the method
        inst.set_system_license_delete(option_name=['SystCommEnableCommandParameter2clone2.SEC', 'SystCommEnableCommandParameter2clone2.IQP', 'SystCommEnableCommandParameter2clone2.MEM', 'SystCommEnableCommandParameter2clone2.BW30'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_system_license_delete_all(self, inst: Keysight33500B):
        # Test Deletes all licenses.

        # Call the method
        inst.system_license_delete_all()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_license_description(self, inst: Keysight33500B):
        # Test Returns a description of specified option, regardless of whether it is currently licensed.

        # Call the method
        result = inst.get_system_license_description()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_error(self, inst: Keysight33500B):
        # Test Returns a string of all the errors produced by SYSTem:LICense:INSTall.

        # Call the method
        result = inst.get_system_license_error()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_error_count(self, inst: Keysight33500B):
        # Test Returns the number of license errors generated by SYSTem:LICense:INSTall.

        # Call the method
        result = inst.get_system_license_error_count()

        # Verify the response is not None
        assert result is not None

    def test_get_system_license_install(self, inst: Keysight33500B):
        # Test This command installs all licenses from a specified file or from all license files in the specified folder. 

        # Call the method
        result = inst.get_system_license_install(fileFolder=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_license_install(self, inst: Keysight33500B):
        # Test This command installs all licenses from a specified file or from all license files in the specified folder. 

        # Call the method
        inst.set_system_license_install(fileFolder=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_lock_name(self, inst: Keysight33500B):
        # Test Returns the current I/O interface (the I/O interface in use by the querying computer).

        # Call the method
        result = inst.get_system_lock_name()

        # Verify the response is not None
        assert result is not None

    def test_get_system_lock_owner(self, inst: Keysight33500B):
        # Test Returns the I/O interface that currently has a lock.

        # Call the method
        result = inst.get_system_lock_owner()

        # Verify the response is not None
        assert result is not None

    def test_system_lock_release(self, inst: Keysight33500B):
        # Test Decrements the lock count by 1 and may release the I/O interface from which the command is executed.

        # Call the method
        inst.system_lock_release()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_lock_request(self, inst: Keysight33500B):
        # Test Requests a lock of the current I/O interface.

        # Call the method
        result = inst.get_system_lock_request()

        # Verify the response is not None
        assert result is not None

    def test_system_security_immediate(self, inst: Keysight33500B):
        # Test Sanitizes all user-accessible instrument memory.

        # Call the method
        inst.system_security_immediate()

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_time(self, inst: Keysight33500B):
        # Test Sets system clock time.

        # Call the method
        result = inst.get_system_time(hour=1, minute=1, seconds=1)

        # Verify the response is not None
        assert result is not None

    def test_set_system_time(self, inst: Keysight33500B):
        # Test Sets system clock time.

        # Call the method
        inst.set_system_time(hour=1, minute=1, seconds=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_system_version(self, inst: Keysight33500B):
        # Test Returns version of the SCPI (Standard Commands for Programmable Instruments) that the instrument complies with. 

        # Call the method
        result = inst.get_system_version()

        # Verify the response is not None
        assert result is not None

    def test_trigger(self, inst: Keysight33500B):
        # Test Forces immediate trigger to initiate sequence, sweep, list, or burst.

        # Call the method
        inst.trigger(trigger_num=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_count(self, inst: Keysight33500B):
        # Test Sets trigger count.

        # Call the method
        result = inst.get_trigger_count(number=1)

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_count(self, inst: Keysight33500B):
        # Test Sets trigger count.

        # Call the method
        inst.set_trigger_count(number=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_delay(self, inst: Keysight33500B):
        # Test Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        # Call the method
        result = inst.get_trigger_delay(delay=1)

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_delay(self, inst: Keysight33500B):
        # Test Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        # Call the method
        inst.set_trigger_delay(delay=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_timer(self, inst: Keysight33500B):
        # Test Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        # Call the method
        result = inst.get_trigger_timer(timer=1)

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_timer(self, inst: Keysight33500B):
        # Test Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        # Call the method
        inst.set_trigger_timer(timer=1)

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_slope(self, inst: Keysight33500B):
        # Test Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        # Call the method
        result = inst.get_trigger_slope(edge=['TrigSeqSlopeCommandParameter1.POSitive', 'TrigSeqSlopeCommandParameter1.NEGative'])

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_slope(self, inst: Keysight33500B):
        # Test Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        # Call the method
        inst.set_trigger_slope(edge=['TrigSeqSlopeCommandParameter1.POSitive', 'TrigSeqSlopeCommandParameter1.NEGative'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_trigger_source(self, inst: Keysight33500B):
        # Test Selects the trigger source for sequence, list, burst or sweep. 

        # Call the method
        result = inst.get_trigger_source(source=['TrigSeqSourceCommandParameter1.IMMediate', 'TrigSeqSourceCommandParameter1.EXTernal', 'TrigSeqSourceCommandParameter1.BUS', 'TrigSeqSourceCommandParameter1.TIMer'])

        # Verify the response is not None
        assert result is not None

    def test_set_trigger_source(self, inst: Keysight33500B):
        # Test Selects the trigger source for sequence, list, burst or sweep. 

        # Call the method
        inst.set_trigger_source(source=['TrigSeqSourceCommandParameter1.IMMediate', 'TrigSeqSourceCommandParameter1.EXTernal', 'TrigSeqSourceCommandParameter1.BUS', 'TrigSeqSourceCommandParameter1.TIMer'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters

    def test_get_unit_angle(self, inst: Keysight33500B):
        # Test Specifies the angle units that displayed on the screen and used for specifying angles.

        # Call the method
        result = inst.get_unit_angle(unit=['UnitAngleCommandParameter1clone.DEGree', 'UnitAngleCommandParameter1clone.RADian', 'UnitAngleCommandParameter1clone.SECond', 'UnitAngleCommandParameter1clone.DEFAult'])

        # Verify the response is not None
        assert result is not None

    def test_set_unit_angle(self, inst: Keysight33500B):
        # Test Specifies the angle units that displayed on the screen and used for specifying angles.

        # Call the method
        inst.set_unit_angle(unit=['UnitAngleCommandParameter1clone.DEGree', 'UnitAngleCommandParameter1clone.RADian', 'UnitAngleCommandParameter1clone.SECond', 'UnitAngleCommandParameter1clone.DEFAult'])

        # Verify the command was executed without errors
        # Note: We can't verify the exact command sent as it depends on the parameters
