MONARC website
==============

# Installation

```bash
$ git clone --recursive https://github.com/monarc-project/website.git
$ cd website/
$ pipenv install
```

# Deployment

## Generate and publish

```bash
$ pipenv shell
$ make html
$ ghp-import output
$ git push git@github.com:monarc-project/monarc-project.github.io.git gh-pages:master -f
```

## Development server

If you want to test with the development server, type in the virtualenv:

```bash
$ make devserver
```
