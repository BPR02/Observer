# Contributing
Contributions are welcome! Make sure to first open an issue discussing the problem or the new feature before creating a pull request. This project uses [poetry](https://python-poetry.org/).

## Installation
Python and poetry are used for the dependency and build management.

### Install Poetry
[Poetry](https://python-poetry.org/) can be installed with `pip` on most systems, but the direct installer on windows systems may work better.

#### Linux/MacOS
```bash
$ pip install poetry
```

#### Windows
```bash
$ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
or 
```bash
$ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Install Dependencies
Once poetry is installed, the dependencies can be installed with the following command
```bash
$ poetry install --with dev
```

### Open Shell
The virtualenv can be accessed using the following command to avoid prepending `poetry run` to every command
```bash
$ poetry shell
```


## Code Style
The code follows the [black](https://github.com/psf/black) code style. Import statements are sorted with [isort](https://pycqa.github.io/isort/). The project must type-check with [pyright](https://github.com/microsoft/pyright). It is recommend to run the type-checker via the VSCode Python extension (discussed below).

**Reformat**
```bash
# omit `poetry run` if u have the virtualenv activated
$ poetry run isort beet_observer
$ poetry run black beet_observer
```

**Check Formatting**
```bash
# omit `poetry run` if u have the virtualenv activated
$ poetry run black --check beet_observer
$ poetry run isort --check-only beet_observer
```

**Type check**
```bash
# omit `poetry run` if u have the virtualenv activated
$ poetry run pyright
```

You can run `poetry self add 'poethepoet[poetry_plugin]'` to get access to an easier set of commands:
```bash
# omit `poetry` if u have the virtualenv activated
$ poetry poe format
$ poetry poe check
$ poetry poe typing
```

## IDE
It is recommend to use [VSCode](https://code.visualstudio.com/). The following recommendations are made for python contributions.

### Python
It is recommend to use the official [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension. This extension comes with type-checking support alongside automatic formatting and import sorting.

## Commits
When committing code, follow the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) style for writing commit messages:

```md
<type>: <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

### Examples
- feat: added support for multiple overlay definitions
- docs: add usage information
- fix: folder generates in incorrect location
- feat!: added support for multiple overlay definitions

> Note 

Here are the types used (adapted from [here](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)):


### Types
> **type** [*version*]: description

- **feat** [*minor*]: A new feature
- **fix** [*patch*]: A bug fix
- **perf** [*patch*]: A code change that improves performance
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation


### Extras
- The start of `<body>` or `<footer>` can be `BREAKING CHANGE:` to indicate a **major** version bump
- Keep each line under 100 characters


## Versioning
This project follows the [semantic versioning](https://semver.org/) format for versioning:
- `major` reserved for breaking changes (needs maintainer approval)
- `minor` for new features and larger tweaks (usually changing user experience like adding an option to the config)
- `patch` for bug fixes and smaller tweaks (usually doesn't affect user experience)

> The commit type indicates whether a bump should be `patch` or `minor`. The version will be updated automatically based on the commit.
