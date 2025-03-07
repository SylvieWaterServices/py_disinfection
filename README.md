# Python Drinking Water Disinfection


<!-- .. image:: https://img.shields.io/pypi/v/py_disinfection.svg
        :target: https://pypi.python.org/pypi/py_disinfection

.. image:: https://img.shields.io/travis/toddrbryan/py_disinfection.svg
        :target: https://travis-ci.com/toddrbryan/py_disinfection

.. image:: https://readthedocs.org/projects/py-disinfection/badge/?version=latest
        :target: https://py-disinfection.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status -->




# Disinfection Parameter Calculator

## Overview

This library and CLI tool provide calculations for **disinfection values**, including CT, log inactivation, and log inactivation ratios. These values are used in drinking water treatment to assess the effectiveness of various disinfectants (e.g., free chlorine, chlorine dioxide, chloramines) against microbial targets such as **Giardia** and **viruses**.

This library implements most of the methods described in the [**US EPA Disinfection Profiling and Benchmarking Technical Guidance Manual**](https://www.epa.gov/sites/default/files/2015-09/documents/disinfection_profiling_and_benchmarking_guidance_manual.pdf). 
Its internal tables for CT values are also taken from this document.  A PDF copy is included in this repository to guard against removal of the EPA link, or dissolution of the EPA.


## Features

- **Python Library** for programmatic access to CT calculations.
- **Command-Line Interface (CLI)** for quick calculations from the terminal.
- **Supports Multiple Estimation Methods:** for free chlorine disinfection:
  - **Conservative**: Uses worst-case values.
  - **Interpolation**: Performs multi-step interpolation.
  - **Regression**: Uses EPA regression equations.
- **Temperature Handling** in Celsius or Fahrenheit.
- **Multiple Disinfectant Agents** supported, including free chlorine, chloramines, and chlorine dioxide.
- **Giardia and Virus Targets** for CT calculations.
- **JSON Output Support** for easy integration with other systems.

---

## Installation

To install the package, run:

```sh
pip install py-disinfection
```

To install from source:

```sh
git clone <repo_url>
cd py-disinfection
make
```

---

## Usage

### **🔹 Library Usage (Python API)**

You can use the library to calculate required CT values programmatically:

```python
from py_disinfection.core import DisinfectionSegment, DisinfectionSegmentOptions, DisinfectionTarget, DisinfectantAgent, CTReqEstimator

options = DisinfectionSegmentOptions(
    volume_gallons=1000,
    temperature_celsius=10,
    ph=7.0,
    concentration_mg_per_liter=0.5,
    baffling_factor=0.3,
    peak_hourly_flow_gallons_per_minute=20,
    agent=DisinfectantAgent.FREE_CHLORINE,
    ctreq_estimator=CTReqEstimator.INTERPOLATION
)

segment = DisinfectionSegment(options)
results = segment.analyze(DisinfectionTarget.GIARDIA)

print(results)  # {'Required CT': 126.5, 'Actual CT': 134, 'Meets Requirement': True}
```

### **🔹 CLI Usage**

You can also run calculations using the command-line tool:

#### **Basic Usage**

```sh
disinfect -v 1000 -t 10 -u C -p 7.0 -c 0.5 -m interpolation -T giardia -a free_chlorine -b 0.3 -f 20
```

#### **Output in JSON Format**

```sh
disinfect -v 1000 -t 10 -u C -p 7.0 -c 0.5 -m interpolation -T giardia -a free_chlorine -b 0.3 -f 20 --json
```

Output:

```json
{
    "Required CT": 126.5,
    "Actual CT": 134,
    "Meets Requirement": true
}
```

---

## Features Coming Soon
- Support for inactivation credits from filtration and other treatment steps
- Ozone disinfection support
- Ability to create multiple treatment segments, and calculate the sum parameters of all segments in a treatment chain
- Expanded test suite

## Development & Contribution

To contribute:

1. Fork the repository.
2. Clone your fork.
3. Install dependencies: `pip install -r requirements_dev.txt` and `pip install -r requirements.txt`
4. Run tests: `make test`

---

## License

This project is licensed under the **BSD License**. See `LICENSE` for details.

---

## Author

Developed by [Sylvie Water Services](www.sylviewater.com). Contributions and suggestions welcome! Reach us at hello@sylviewater.com.

