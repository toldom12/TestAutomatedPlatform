# Automated Tests Encoder Controller

Python automated tests for an encoder connected through a serial COM port.

## Encoder test cases

- **Startup parameters** - verifies the encoder COM port, baud rate, and stepper-motor steps per rotation against the expected configuration.
- **No-rotation measurement** - reads the encoder position twice while the motor is stationary and verifies that both position percentages are equal.

Encoder settings are configured in `setup/config.ini`. Run the test suite with:

```powershell
pytest automated_tests/encoder
```
