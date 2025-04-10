NGC2D Pressure Gauge Controller
=============================

.. module:: instrumental.drivers.vacuum.ngc2d

The NGC2D is a dual pressure gauge controller that supports multiple gauge types including ion gauges and pirani gauges. This driver provides an interface to control and read from the NGC2D pressure gauge controller.

Interface Protocol
-----------------

The controller communicates via RS232 serial interface with the following settings:

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

Usage
-----

Basic usage example::

    from instrumental.drivers.vacuum.ngc2d import NGC2D

    # Create NGC2D instance
    ngc = NGC2D(port='COM1')  # Replace with your actual port

    try:
        # Set remote control
        ngc.control()
        
        # Select ion gauge 1
        ngc.select_ion_gauge('1')
        
        # Turn on the gauge with 0.5mA emission current
        ngc.gauge_on('0')
        
        # Read status
        status = ngc.get_status()
        print(status)
        
    finally:
        # Always close the connection
        ngc.close()

API Reference
------------

.. autoclass:: NGC2D
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

+----------------+--------+----------------+--------------------------------+
| Command        | Char.  | Parameter      | Description                    |
+================+========+================+================================+
| <poll>         | P      | None          | Poll instrument                |
+----------------+--------+----------------+--------------------------------+
| <control>      | C      | None          | Switch to remote control       |
+----------------+--------+----------------+--------------------------------+
| <release>      | R      | None          | Return to local control        |
+----------------+--------+----------------+--------------------------------+
| <reset_error>  | E      | None          | Reset all error flags          |
+----------------+--------+----------------+--------------------------------+
| <status>       | S      | None          | Request status report          |
+----------------+--------+----------------+--------------------------------+
| <gauge_on>     | i      | E             | Switch on ion gauge emission   |
|                |        |               | (E='0' 0.5mA, E='1' 5mA)      |
+----------------+--------+----------------+--------------------------------+
| <select_IG>    | j      | G             | Select ion gauge               |
|                |        |               | (G='1' IG1, G='2' IG2)        |
+----------------+--------+----------------+--------------------------------+
| <gauge_off>    | o      | None          | Switch off ion gauge           |
+----------------+--------+----------------+--------------------------------+
| <override>     | O      | R             | Permanently energize relay     |
|                |        |               | (R='A' to 'D')                |
+----------------+--------+----------------+--------------------------------+
| <inhibit>      | I      | R             | Permanently de-energize relay  |
|                |        |               | (R='A' to 'D')                |
+----------------+--------+----------------+--------------------------------+

Status Report Format
------------------

The status report provides information about all gauges in the NGC2D:

1. State byte
2. Error byte
3. Relay status byte (0100XXXX, where XXXX indicates state of relays A-D)
4. Unused byte ('0')
5. Gauge records for each gauge:
   - Header byte ('G')
   - Gauge type
   - Gauge number
   - Gauge status
   - Gauge error
   - Pressure value (comma-delimited string in scientific notation)

Gauge Types
----------

The controller supports the following gauge types:

1. Ion Gauge 1
2. Pirani 1
3. Pirani 2
4. Capacitance manometer
5. Ion Gauge 2

Pressure Units
-------------

The controller supports the following pressure units:

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

See Also
--------

- :doc:`vacuum`
- :doc:`instruments` 