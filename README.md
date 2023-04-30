# ICD API

## Prerequisites

- [Python](https://www.python.org/): This project has been created using `python 3.9.6`.
- [Pip3](https://pypi.org/project/pip/): This project makes use of `pip` to install Python packages.
- [Git](https://git-scm.com): Our source code repositories are hosted on [GitHub](https://github.com) for version control and collaboration.
  If you don't have a [GitHub](https://github.com) account already you can create one [here](https://github.com/join).
  Follow instructions [here](https://git-scm.com/downloads) to install the latest version of Git for your system.

## Dependencies

- [Postgres](https://www.postgresql.org/): Postgres is the target database dialect.
- [Mailhog](https://github.com/mailhog/MailHog): Spins up a local mail server.

## Libraries

- [Flask](https://flask.palletsprojects.com/en/2.3.x/): The API service is build using python's flask framework.
- [Pandas](https://pandas.pydata.org/): We are using pandas to process csv file uploads.
- [psycopg2](https://pypi.org/project/psycopg2/): We are using psycopg2 as our database adapter.
- [pytest](https://docs.pytest.org/en/7.3.x/): We are making use of pytest to test the API endpoints

## Getting started

Once you have the libraries and dependencies above installed, do the following:

1. Create a .env file based on the `.env.example` file and update it with the correct credentials
2. Initialize the database with the following: `python3 init_db.py`
3. Run: `python3 -m flask --app ./app.py run --debug` to start the development server in debug mode
4. To run the test suites, run the following: `python3 -m pytest`

**Additional information:**

1. Make sure your postgres server is up and running
2. Make sure `mailhog` is up and running
3. Depending on your local installation of `python`, you can run the commands with just `python <command>`

## Contributing

To enforce best coding practices and integrity, we use Rubocop for static code analysis and RSpec for testing functionality.
They both are configured as `test` and `spec` tasks with `rake`.

1. Fork a new branch off `master` using `git checkout -b <feature-branch-name> master`.
2. Do your changes and run `rake test` and `rake spec` to ensure code quality.
3. Commit your changes using `git commit -am 'Some message outlining your changes'`.
4. Push feature branch to Github using `git push origin <feature-branch-name>`.
5. Send a Pull Request on Github.

## Guidelines

Use the following guides for getting things done, programming well, and programming in style.

- [Protocol](http://github.com/thoughtbot/guides/blob/master/protocol)
- [Best Practices](http://github.com/thoughtbot/guides/blob/master/best-practices)
- [Coding Style - Python](https://github.com/thoughtbot/guides/tree/main/python)

## API Documentation

- [Click here to view example queries and responses for the API](https://documenter.getpostman.com/view/3763588/2s93eSZbAu)
