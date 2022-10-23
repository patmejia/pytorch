# Install & Setup

```bash
poetry --version
poetry shell
poetry install
```

## Run the code

For instance, to run the code in the `src` folder, you can use the following command:

```bash
poetry run python src/networkx_example.py # run the script
poetry run python src/main.py
```

## Adding or Remove dependency

```bash
poetry add matplotlib
poetry add pytest --dev
poetry add <your package>

poetry remove matplotlib
poetry remove pytest --dev
poetry remove <your package>
```

## Update

Update the dependencies as according to the pyproject.toml file.

```
poetry update
```

# Poetry Options

```bash
Poetry (version 1.2.1)

Usage:
  command [options] [arguments]

Options:
  -h, --help            Display help for the given command. When no command is given display help for the list command.
  -q, --quiet           Do not output any message.
  -V, --version         Display this application version.
      --ansi            Force ANSI output.
      --no-ansi         Disable ANSI output.
  -n, --no-interaction  Do not ask any interactive question.
      --no-plugins      Disables plugins.
      --no-cache        Disables Poetry source caches.
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.

Available commands:
  about              Shows information about Poetry.
  add                Adds a new dependency to pyproject.toml.
  build              Builds a package, as a tarball and a wheel by default.
  check              Checks the validity of the pyproject.toml file.
  config             Manages configuration settings.
  export             Exports the lock file to alternative formats.
  help               Displays help for a command.
  init               Creates a basic pyproject.toml file in the current directory.
  install            Installs the project dependencies.
  list               Lists commands.
  lock               Locks the project dependencies.
  new                Creates a new Python project at <path>.
  publish            Publishes a package to a remote repository.
  remove             Removes a package from the project dependencies.
  run                Runs a command in the appropriate environment.
  search             Searches for packages on remote repositories.
  shell              Spawns a shell within the virtual environment.
  show               Shows information about packages.
  update             Update the dependencies as according to the pyproject.toml file.
  version            Shows the version of the project or bumps it when a valid bump rule is provided.

 cache
  cache clear        Clears Poetry's cache.
  cache list         List Poetry's caches.

 debug
  debug info         Shows debug information.
  debug resolve      Debugs dependency resolution.

 env
  env info           Displays information about the current environment.
  env list           Lists all virtualenvs associated with the current project.
  env remove         Remove virtual environments associated with the project.
  env use            Activates or creates a new virtualenv for the current project.

 self
  self add           Add additional packages to Poetry's runtime environment.
  self install       Install locked packages (incl. addons) required by this Poetry installation.
  self lock          Lock the Poetry installation's system requirements.
  self remove        Remove additional packages from Poetry's runtime environment.
  self show          Show packages from Poetry's runtime environment.
  self show plugins  Shows information about the currently installed plugins.
  self update        Updates Poetry to the latest version.

 source
  source add         Add source configuration for project.
  source remove      Remove source configured for the project.
  source show        Show information about sources configured for the project.
```
