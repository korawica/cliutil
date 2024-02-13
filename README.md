# Utility Package: *CLI Shelf*

[![test](https://github.com/korawica/clishelf/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/korawica/clishelf/actions/workflows/tests.yml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/clishelf?logo=pypi)](https://pypi.org/project/clishelf/)
[![size](https://img.shields.io/github/languages/code-size/korawica/clishelf)](https://github.com/korawica/clishelf)

**Table of Contents**:

* [Installation](#installation)
* [Pre-Commit Hook](#pre-commit-hook)
* [Features](#features)
  * [Extended Git](#extended-git)
  * [Versioning](#versioning)
  * [Emoji](#emoji)
* [Configuration](#configuration)

This is the **CLI Utility** Python package for help me to make versioning and
logging on my any Python package repositories, because I do not want to hard
code or set up the development flow every time that I create the new Python
package project :tired_face:.

## Installation

```shell
pip install clishelf
```

In the future, I will add more the CLI tools that able to dynamic with
many style of config such as I want to make changelog file with style B by my
custom message code.

## Pre-Commit Hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

```yaml
-   repo: https://github.com/korawica/clishelf
    rev: v0.x.x
    hooks:
    -   id: shelf-commit-msg
```

## Features

This Utility Package provide some CLI tools for handler development process.

```text
Usage: shelf.exe [OPTIONS] COMMAND [ARGS]...

  The Main Shelf commands.

Options:
  --help  Show this message and exit.

Commands:
  conf   Return config for clishelf commands
  cove   Run the coverage command.
  dep    List of Dependencies that was set in pyproject.toml file.
  echo   Echo Hello World
  emoji  The Emoji commands
  git    The Extended Git commands
  vs     The Versioning commands.
```

### Extended Git

```text
Usage: shelf.exe git [OPTIONS] COMMAND [ARGS]...

  The Extended Git commands

Options:
  --help  Show this message and exit.

Commands:
  bn           Show the Current Branch name.
  bn-clear     Clear Local Branches that sync from the Remote repository.
  cm           Show the latest Commit message
  cm-prev      Commit changes to the Previous Commit with same message.
  cm-revert    Revert the latest Commit on the Local repository.
  df           Show changed files from previous commit to HEAD
  init         Initialize GIT config on local
  log          Show the Commit Logs from the latest Tag to HEAD.
  mg           Merge change from another branch with strategy, `theirs`...
  pf           Show Profile object that contain Name and Email of Author
  tg           Show the Latest Tag if it exists, otherwise it will show...
  tg-clear     Clear Local Tags that sync from the Remote repository.
```

### Versioning

```text
Usage: shelf.exe vs [OPTIONS] COMMAND [ARGS]...

  The Versioning commands.

Options:
  --help  Show this message and exit.

Commands:
  bump       Bump Version with specific action.
  changelog  Make Changelogs file
  conf       Return the config data for bumping version.
  current    Return Current Version that read from ``__about__`` by default.
  tag        Create the Git tag by version from the ``__about__`` file.
```

### Emoji

```text
Usage: shelf.exe emoji [OPTIONS] COMMAND [ARGS]...

  The Emoji commands

Options:
  --help  Show this message and exit.

Commands:
  fetch  Refresh emoji metadata file on assets folder.
  ls     List all emojis from metadata file.
```

## Configuration

The configuration able to be `.clishelf.yaml` or mapping value in `pyproject.toml`.

`.clishelf.yaml`:

```yaml
git:
  commit_prefix:
    - ["comment", "Documents", ":bulb:"]  # 💡
    - ["typos", "Documents", ":pencil2:"]  # ✏️
  commit_prefix_group:
    - ["Features", ":tada:"]  # 🎉
```

`pyproject.toml`:

```toml
[tool.shelf.version]
version = "./clishelf/__about__.py"
changelog = "CHANGELOG.md"
mode = "normal"
```

> **Note**:\
> The bump version mode able to be `normal` or `datetime` only.

## License

This project was licensed under the terms of the [MIT license](LICENSE).
