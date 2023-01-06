# Fun-With-Pandas
dataframes and things


## About

Coming Soon

## Setup

### Poetry on Windows

[Poetry Docs](https://python-poetry.org/docs/)

After install use this powershell command to add **poetry** to your *$PATH*:
```sh
[Environment]::SetEnvironmentVariable("Path", $env:Path + "C:\Users\replace_with_user\AppData\Roaming\pypoetry\venv\Scripts\", "Machine")
```

I had to restart vscode for an unknown reason.

## Dev Environment

From Powershell, navigate to project directory:

```sh
poetry shell
poetry install
code .
```

In **vscode** check the blue bar at the bottom of the window to confirm environment is set correctly.

## Vscode setup

- Linter: Install extension **flake8**
- Formatter: Keyboard Combo! **Shift + Ctrl + P** and type *Format Document*, press Enter, select **Use black**.

Settings:

- **Ctrl + ,** find "Format on Save" and check it
- Open **.vscode/settings.json** and add:
```json
{
    ...
    "python.linting.flake8Args": [
        "--max-line-length=88"
    ],
}
```