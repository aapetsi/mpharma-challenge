
# ICDC API

## Prerequisites

- [Python](https://www.python.org/): This project has been created using `python 3.9.6`.
- [Pip3](https://pypi.org/project/pip/): This project makes use of `pip` to install Python packages.
- [Git](https://git-scm.com): Our source code repositories are hosted on [GitHub](https://github.com) for version control and collaboration.
  If you don't have a [GitHub](https://github.com) account already you can create one [here](https://github.com/join).
  Follow instructions [here](https://git-scm.com/downloads) to install the latest version of Git for your system.

## Dependencies

- [Postgres](https://www.postgresql.org/): Postgres is the target database dialect.

## Libraries

- [Flask](https://flask.palletsprojects.com/en/2.3.x/): The API service is build using python's flask framework.
- [Pandas](https://pandas.pydata.org/): We are using pandas to process csv file uploads.
- [psycopg2](https://pypi.org/project/psycopg2/): We using pscopg2 as our database adapter.

## Getting started

If you have [Docker](https://www.docker.com/) installed on your system, see [Docker](#docker) section below for quick start.



## Contributing

To enforce best coding practices and integrity, we use Rubocop for static code analysis and RSpec for testing functionality.
They both are configured as `test` and `spec` tasks with `rake`.

1. Fork a new branch off `master` using `git checkout -b <feature-branch-name> master`.
2. Do your changes and run `rake test` and `rake spec` to ensure code quality.
3. Commit your changes using `git commit -am 'Some message outlining your changes'`.
4. Push feature branch to Github using `git push origin <feature-branch-name>`.
5. Send a Pull Request on Github.

## Docker

You can also get started with development quickly using [Docker](https://www.docker.com/).
First you need to authenticate with Github's container registry ([see link here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry)) and follow below steps:

1. Clone this repository locally using `git clone https://github.com/swipe/swipe.git`.
2. Run `docker-compose up` to start the application.
3. Run database migrations using `docker-compose exec -T app rails db:migrate`.
4. To lint code and run test cases, run `docker-compose exec -T app rake test` and `docker-compose exec -T app rake spec` respectively.

## Guidelines

Use the following guides for getting things done, programming well, and programming in style.

- [Protocol](http://github.com/thoughtbot/guides/blob/master/protocol)
- [Best Practices](http://github.com/thoughtbot/guides/blob/master/best-practices)
- [Coding Style - Python](https://github.com/thoughtbot/guides/tree/main/python)

## Deployment
