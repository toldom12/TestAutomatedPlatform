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

## Arduino Nano tests

The platform also contains tooling and automated tests for an Arduino Nano. The
Nano is programmed through `arduino-cli` and communicates with the Python test
suite over a serial COM port. The configured port, baud rate, CLI executable,
and sketch directories are stored in `setup/config.ini`.

The Arduino test sketch supports simple command/response checks such as:

- `STATUS` -> `OK`
- `TEMP` -> a temperature value
- `SELFTEST` -> a self-test result

Run the Arduino tests locally from the repository root with:

```powershell
pytest automated_tests/arduino
```

The test fixture can erase the previous application, flash the test sketch, and
then verify the response received from the Nano. The board must be connected to
the configured COM port, and the serial port must not be used by another
application.

## J-Link support

J-Link support is provided as a separate tool under `tools/jlink`. It currently
contains the connection/integration point for a configured J-Link executable
and probe serial number. J-Link-based flashing and device tests are intended to
follow the same pattern as the Arduino tooling, with device-specific commands
and verification implemented in their own test modules.

## CI/CD direction

This repository is an example platform for automated embedded-device testing
with CI/CD. The GitHub Actions workflow in `.github/workflows/run_selftest.yaml`
demonstrates how an Arduino Nano self-test can be triggered with workflow
inputs, flashed, and verified by pytest.

Hardware tests require a self-hosted Windows runner with the target device
physically connected (for example, an Arduino Nano on `COM4`). GitHub-hosted
runners cannot access hardware connected to a developer's workstation.

The CI/CD integration is an ongoing foundation for future work. Planned areas
include additional Arduino and J-Link test cases, richer self-test responses,
automatic device discovery, standardized test reports, and support for more
embedded boards and programmers.
