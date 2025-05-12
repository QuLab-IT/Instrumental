Arun Microelectronics NGC Pressure Gauge Controllers
=============================

.. module:: instrumental.drivers.vacuum.ngc

The NGC series of pressure gauge controllers support multiple gauge types including ion gauges and pirani gauges. This driver provides an interface to control and read from various NGC models (NGC2, NGC2D, NGC2-D, and NGC3) with their specific features.

The `NGC2 <https://arunmicro.com/documentation/Manual_NGC2.pdf>`_, `NGC2D <https://arunmicro.com/documentation/Manual_NGC2D.pdf>`_, `NGC2-D <https://manualzz.com/doc/7009440/aml-ngc2-d-dual-pressure-gauge-controller-user-manual>`_ and `NGC3 <https://arunmicro.com/documentation/Manual_NGC3.pdf>`_ user manuals were used as guide for the implementation.

Supported Models
---------------

The driver supports the following NGC models:

- **NGC2**: Basic pressure gauge controller
- **NGC2D**: Dual ion gauge controller with bakeout capability
- **NGC2-D**: Dual ion gauge controller
- **NGC3**: Dual ion gauge controller with bakeout capability

Feature Support
-------------

+----------------+-----------+-----------+-----------+-----------+
| Feature        | NGC2      | NGC2D     | NGC2-D    | NGC3      |
+================+===========+===========+===========+===========+
| Dual Ion Gauge | No        | Yes       | Yes       | Yes       |
+----------------+-----------+-----------+-----------+-----------+
| Bakeout        | No        | Yes       | No        | Yes       |
+----------------+-----------+-----------+-----------+-----------+

Installation
------------

The NGC driver is included in the Instrumental package. To use it, ensure you have the following:

- Python 3.6 or higher
- Instrumental package installed
- PySerial package installed
- Proper serial port permissions (on Linux/Unix systems)

Interface Protocol
-----------------

The controllers communicate via RS232 serial interface with the following settings:

- Baud rate: 9600
- Data bits: 8
- Stop bits: 1
- Parity: None
- Handshaking: None

Commands are sent in the format:
- First byte: * (ASCII 47)
- Second byte: Command character
- Third byte: Ignored byte (for compatibility)
- Optional parameter: Additional command parameters

The instrument responds with a state byte and an error byte, followed by a CR-LF. If a status report was requested, the state and error bytes are followed by the report and CR-LF.

Configuration
------------

The NGC controllers can be configured with the following settings:

Serial Port Settings
~~~~~~~~~~~~~~~~~~

- Baud rate: 9600
- Data bits: 8
- Stop bits: 1
- Parity: None
- Handshaking: None

Default Settings
~~~~~~~~~~~~~~~

- Pressure unit: Torr
- Emission current: 0.5mA
- Default gauge: Ion Gauge 1

Usage
-----

Basic usage example::

    from instrumental.drivers.vacuum.ngc import NGC2D  # or NGC2, NGC2_D, NGC3

    # Create NGC instance
    ngc = NGC2D(port='COM1')  # Replace with your actual port

    try:
        # Set remote control
        ngc.control()
        
        # Select ion gauge 1 (only available on dual ion gauge models)
        if ngc.has_feature(OptionalFeature.DUAL_ION_GAUGE):
            ngc.select_ion_gauge('1')
        
        # Turn on the gauge with 0.5mA emission current
        ngc.gauge_on('0')
        
        # Read status
        status = ngc.get_status()
        print(status)
        
    finally:
        # Always close the connection
        ngc.close()

Advanced Usage
~~~~~~~~~~~~~

Monitoring Pressure::

    # Continuously monitor pressure
    while True:
        status = ngc.get_status()
        for gauge in status.gauges:
            if gauge.pressure is not None:
                print(f"Gauge {gauge.number}: {gauge.pressure} Torr")
        time.sleep(1)

Error Handling::

    try:
        ngc.gauge_on()
    except RuntimeError as e:
        print(f"Failed to turn on gauge: {e}")

Bakeout Example (NGC2D and NGC3 only)::

    if ngc.has_feature(OptionalFeature.BAKEOUT):
        ngc.bakeout()

API Reference
------------

.. autoclass:: NGC
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: NGC2
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: NGC2D
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: NGC2_D
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: NGC3
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: GaugeType
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: PressureUnit
   :members:
   :undoc-members:
   :show-inheritance:

Command Reference
---------------

The following commands are supported:

+----------------+--------+----------------+--------------------------------+------------------+
| Command        | Char.  | Parameter      | Description                    | Response Format  |
+================+========+================+================================+==================+
| <poll>         | P      | None          | Poll instrument                | State, Error    |
+----------------+--------+----------------+--------------------------------+------------------+
| <control>      | C      | None          | Switch to remote control       | None            |
+----------------+--------+----------------+--------------------------------+------------------+
| <release>      | R      | None          | Return to local control        | None            |
+----------------+--------+----------------+--------------------------------+------------------+
| <reset_error>  | E      | None          | Reset all error flags          | State, Error    |
+----------------+--------+----------------+--------------------------------+------------------+
| <status>       | S      | None          | Request status report          | Full status     |
+----------------+--------+----------------+--------------------------------+------------------+
| <gauge_on>     | i      | E             | Switch on ion gauge emission   | State, Error    |
|                |        |               | (E='0' 0.5mA, E='1' 5mA)      |                 |
+----------------+--------+----------------+--------------------------------+------------------+
| <select_IG>    | j      | G             | Select ion gauge               | State, Error    |
|                |        |               | (G='1' IG1, G='2' IG2)        |                 |
+----------------+--------+----------------+--------------------------------+------------------+
| <gauge_off>    | o      | None          | Switch off ion gauge           | State, Error    |
+----------------+--------+----------------+--------------------------------+------------------+
| <override>     | O      | R             | Permanently energize relay     | State, Error    |
|                |        |               | (R='A' to 'D')                |                 |
+----------------+--------+----------------+--------------------------------+------------------+
| <inhibit>      | I      | R             | Permanently de-energize relay  | State, Error    |
|                |        |               | (R='A' to 'D')                |                 |
+----------------+--------+----------------+--------------------------------+------------------+
| <bakeout>      | B      | None          | Start bakeout cycle           | State, Error    |
+----------------+--------+----------------+--------------------------------+------------------+

Status Report Format
------------------

The status report provides detailed information about the controller's state:

1. State byte
   - Bits 3-0: Instrument type
   - Bit 4: Mode (local/remote)
   - Bit 6: Selected gauge
   - Bit 7: IG connected status

2. Error byte
   - Bit 0: Gauge error
   - Bit 1: Over temperature trip
   - Bit 3: Temperature warning

3. Relay status byte (0100XXXX)
   - XXXX indicates state of relays A-D
   - 1 = energized, 0 = de-energized

4. Unused byte ('0')

5. Gauge records for each gauge:
   - Header byte ('G')
   - Gauge type (I/P/M for Ion/Pirani/Manometer)
   - Gauge number (1-5)
   - Gauge status (bit field)
   - Gauge error (bit field)
   - Pressure value (comma-delimited string in scientific notation)

Gauge Types
----------

The controllers support the following gauge types:

1. Ion Gauge 1
2. Pirani 1
3. Pirani 2
4. Capacitance manometer
5. Ion Gauge 2 (on dual ion gauge models)

Pressure Units
-------------

The controllers support the following pressure units:

- Torr
- Pascal
- mBar

Error Handling
------------

The driver includes comprehensive error handling for all commands and responses. Errors are raised as exceptions with descriptive messages. Common error conditions include:

- Invalid responses from the device
- Attempting to control the device while in local mode
- Invalid parameter values
- Communication timeouts
- Attempting to use features not supported by the model

Troubleshooting
--------------

Common Issues
~~~~~~~~~~~~

- **No Response from Device**
  - Check serial port connection
  - Verify baud rate and other settings
  - Ensure device is powered on

- **Permission Denied**
  - On Linux/Unix: Add user to dialout group
  - On Windows: Check device manager for correct COM port

- **Invalid Responses**
  - Check cable connections
  - Verify device is in correct mode (local/remote)
  - Ensure no other program is using the port

- **Feature Not Supported**
  - Verify your device model supports the feature
  - Check has_feature() before using advanced features

Safety Information
----------------

Important safety considerations when using NGC controllers:

- Always ensure proper ventilation when using ion gauges
- Do not operate ion gauges at pressures above 1e-3 Torr
- Allow proper warm-up time for ion gauges
- Follow manufacturer's guidelines for bakeout procedures
- Use appropriate safety measures when handling high voltage components

Version History
--------------

- 1.0.0 (2024-03-20)
  - Initial release
  - Support for all NGC models
  - Feature detection and validation
  - Comprehensive error handling

References
----------

- `NGC Series User Manual <https://www.lesker.com>`_
- `PySerial Documentation <https://pyserial.readthedocs.io>`_
- `Instrumental Documentation <https://instrumental-lib.readthedocs.io>`_

See Also
--------

- :doc:`vacuum`
- :doc:`instruments` 