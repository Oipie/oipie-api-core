# Oipie API

Oipie API repository implements the API that will be consumed by the mobile apps.

## 💻 I'm a dev, how do I get started?

Prerequisites:

- [Python](https://www.python.org/downloads/): 3.10
- [Poetry](https://python-poetry.org/docs/#installation): 1.2.0
- [Docker](https://docs.docker.com/get-docker/)

Now:

```bash
git clone git@github.com:Oipie/oipie-api-core.git
cd oipie-api-core
poetry install
docker-compose up [-d] --build postgres # starts DDBB
flask db init # creates database if not exists
flask db upgrade # runs all database migrations
flask --app "src/app.py" run # starts the server in development mode
```

You are now good ready to go!! 👯

### Dependency management

We are using virtual environments to manage our dependencies separated from other Python projects. Dependencies are managed using poetry.

```bash
poetry add [--group dev] <package==version> # adds a new dependency
```

If no version is specified, the latest version will be installed with caret, but the caret should be removed. If that is the case, just regenerate lockfile.

```bash
poetry lock # regenerates lockfile
```

## Dependency Injection

Dependency injection have been implemented using `dependency-injection` python library. Following the documentation and the [tutorial](https://python-dependency-injector.ets-labs.org/examples/fastapi-sqlalchemy.html).

To use dependecy injection have to take into account that providers have to be defined on the `Container.py` defined into `src/confg/`. Actual configuration of the dependency injection resolver is only set up to resolve dependencies inside the `src/api/`.

### Docker

We use Docker as a utility tool, mainly for running a Postgres, which is the Database that we have deployed with RDS. In the `docker-compose.yml` you have two services:

- `postgres`: A postgres database that we use for starting the API in development mode and running the integration tests locally.
- `web`: Our API running in production mode with [Gunicorn](https://gunicorn.org/).

For starting the full application you can run the following command

```bash
docker-compose up [-d] --build
```

#### Why do we have more than just a simple Dockerfile?

Since we are using Heroku containers (SENKIU Heroku) as our deploying platform, we need to have two different Dockerfiles regarding Heroku container images:
- `Dockerfile.web` --> Starts gunicorn at specified port by Heroku
- `Dockerfile.release` --> Executes pre-deploy scripts. In this case we just launch migrations

As soon as we stop using Heroku these files will be removed **PERMANENTLY** from the project

#### :warning: Important warning

If you're using a M1 chipset based computer, you may encounter some problems when interacting to `web` container. The main reason is because some `pip` dependencies regarding `SQLAlchemy`. This can be solved by exporting `DOCKER_DEFAULT_PLATFORM` variable to `linux/amd64`:
`export DOCKER_DEFAULT_PLATFORM=linux/amd64` or adding it to your `.bashrc`/`.zshrc` or the tool you are using. Another alternative is to simply use Rosetta. Please be adviced that any of these workarounds may make your Docker performance a little bit lower.

### Heroku

We use [Heroku](https://www.heroku.com/) to publish this API so it can be consumed. Heroku settings are set in repositorie's CI/CD workflows, so you do not need anything to worry about to this matter.

For now we just have a main environment that you can access [through this URL](https://oipie.herokuapp.com/)

### Project management

- [Oipie board](https://trello.com/b/727W8t27/development)
- [Github repo](https://github.com/Oipie/oipie-api-core)
- [Figma](https://www.figma.com/file/baltSi1jqPjxE3lJRdl3gh/Oipiegma)
- [IDE settings](/docs/ide-settings.md)

## 🛠 Which technologies are you using?

- Python
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## 🗂 How is the repository organized?

In order to be aligned with the Oipie DevOps Team, this repository is organized with the following folder structure:

1. src - contains all source code of the application.
    * api: code all controllers and DTO
    * config: configuration files
    * core: all modules on the application.
    * tests: E2E tests and fixtures
3. .github - Github actions integration for CI/CD

## 🏘 How is the code organized?

The architecture follows the principles from Hexagonal Architecture.

All the main code of the application lives under `src`

## ✅ Tests

- We are using [Pytest](https://docs.pytest.org/en/7.1.x/)
- Unitary Tests are paired with the element that tests. For example `test_recipe.py` is next to `recipe.py`.
- Acceptance tests lives under the `tests` directory.

### CI/CD

Continous integration execute pylint and all tests on each push to any branch.
<<<<<<< HEAD
=======

Continous deployment is executed only on master brach after all previous actions have succed.
>>>>>>> 821f0cad68385585254999a06e6ed07a24d86eb2

## 📲 Contact

The project was mainly developed by [Jaume Moreno](morenocantoj@gmail.com) and [Diego Machín](diego@acidtango.com)
for [Acid Tango](https://acidtango.com/)
