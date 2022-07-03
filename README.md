# datasette-mailto-links

[![Run tests](https://github.com/chris48s/datasette-mailto-links/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/chris48s/datasette-mailto-links/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/chris48s/datasette-mailto-links/branch/main/graph/badge.svg?token=JEUG9Y0ZT3)](https://codecov.io/gh/chris48s/datasette-mailto-links)
[![PyPI Version](https://img.shields.io/pypi/v/datasette-mailto-links.svg)](https://pypi.org/project/datasette-mailto-links/)
![License](https://img.shields.io/pypi/l/datasette-mailto-links.svg)
![Python Compatibility](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fdatasette-mailto-links%2Fjson)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Datasette plugin to render email addresses as `mailto:` links

## Installation

```
pip install datasette-mailto-links
```

## Configuration

By default, when installed datasette-mailto-links will search for values in any column that look like an email address and replace them with a `mailto:` link. To restrict this behaviour to only certain columns, the plugin behaviour can be configured in `metadata.json`. e.g:

```json
{
  "databases": {
    "my_db": {
      "tables": {
        "email": {
          "plugins": {
            "datasette-mailto-links": {
              "columns": ["sender", "recipient"]
            }
          }
        }
      }
    }
  }
}
```

The plugin can be disabled entirely for certain tables using `"columns": []`

For more detail on Datasette plugin configuration see https://docs.datasette.io/en/latest/plugins.html#plugin-configuration
