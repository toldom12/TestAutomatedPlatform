# Automated Embedded Test Devices Platform

A Python platform for automating tests of embedded devices. It provides reusable tooling and test suites for communicating with hardware through interfaces such as serial COM ports.

The platform supports multiple device kinds. An **encoder controller** is the first supported device kind; additional embedded devices can be added with their own tooling and test suites.

## Encoder test cases

- **Startup parameters** - verifies the encoder COM port, baud rate, and stepper-motor steps per rotation against the expected configuration.
- **No-rotation measurement** - reads the encoder position twice while the motor is stationary and verifies that both position percentages are equal.

Encoder settings are configured in `setup/config.ini`. Run the test suite with:

```powershell
pytest automated_tests/encoder
```
