# IDE settings

- [Visual Code](#visual-code)

## Visual Code

### Formatter

We are using black as formatter, so you need to install it on your VSCode.

```
ext install ms-python.black-formatter
```

Then you need to add the following settings to your VSCode settings.json:

```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackPath": ".venv/bin/black",
    "[python]": {
      "editor.defaultFormatter": "ms-python.black-formatter",
      "editor.formatOnSave": true
    },
}
```

### launch.json

```
TODO: Add configuration for debugging
```