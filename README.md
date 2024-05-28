<img src="https://github.com/rcortini/pybruno/blob/main/pybruno.png" alt="pybruno" width="200"/>

# PyBruno

![Tests](https://github.com/rcortini/pybruno/actions/workflows/main.yml/badge.svg)

**pybruno** is a Python library containing utilities to parse BRU files, a special markup language defined in [Bruno](https://usebruno.com) - a lightweight, open-source alternative to Postman/Insomnia. It leverages a hybrid Python/JavaScript approach to handle the parsing logic effectively.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

`pybruno` provides utilities to parse BRU files, which are used to define blocks in a specific markdown-like language (see the [bruno-lang](https://github.com/usebruno/bruno/tree/main/packages/bruno-lang) package with the language definition). The library handles the conversion of BRU file content into JSON format, leveraging the Node.js source code for robust and efficient parsing.

## Features

- Parse BRU files into JSON format.
- Handle both dictionary and text blocks.
- Replace variables within the BRU content.
- Easy integration with Python projects.
- Hybrid approach utilizing Node.js for parsing.

## Installation

### Prerequisites

- Python 3.8+
- Node.js 14+

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/rcortini/pybruno.git
    cd pybruno
    ```

2. Install the Python package:

    ```sh
    pip install -e .
    ```

## Usage

### Example

Here's a simple example to get you started with `pybruno`:

```python
# Test usage
bru_file_path = 'tests/test.bru'
bru_env_path = '/tests/test_env.bru'

# first, print without env
parsed_data = parse_bru_file(bru_file_path)
print(parsed_data)

print("WITH ENVIRONMENT:")
env = parse_env_file(bru_env_path)
print(env)
parsed_data = parse_bru_file(bru_file_path, env)
print(parsed_data)
```

## Testing
To run tests, use the following commands:

Ensure you have all dependencies installed:

```sh
pip install -r requirements.txt
```

Then, execute the tests
```sh
pytest
```

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

Please make sure to update tests as appropriate.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- `bruno` package creators
- `ohm-js` for the parsing library.
- `lodash` for utility functions.
