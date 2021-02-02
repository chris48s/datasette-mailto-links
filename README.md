# datasette-mailto-links

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
