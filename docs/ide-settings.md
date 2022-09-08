# IDE settings

- [Visual Code](#visual-code)

## Visual Code

Most of the settings can be added to the `.vscode/settings.json` file, so the options are only applied to this project.

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

### Linter

We are using pylint as linter, so you need to install it on your VSCode.

```
ext install ms-python.pylint
```

Then you need to add the following settings to your VSCode settings.json:

```json
{
    "python.linting.pylintPath": ".venv/bin/pylint",
    "python.linting.pylintEnabled": true,
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