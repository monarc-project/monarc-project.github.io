MONARC website
==============

# Installation

```bash
$ git clone --recursive https://github.com/monarc-project/monarc-project.github.io
$ cd monarc-project.github.io/
$ poetry install # you can also use pipenv install
```

# Deployment

## Check and publish

You can directly push your changes but it is preferable to first check locally:

```bash
$ poetry shell # you can also use pipenv shell
# generation of the static website:
$ make html
# or test with the development server:
$ make devserver
```

Once everything looks fine, publish the changes:


```bash
$ git commit -S -am "<your comment>"
$ git push origin source
```

The website will be automatically generated thanks to GitHub Actions and the
result deployed on the GitHub Organization Pages
(available [here](https://www.monarc.lu)).
