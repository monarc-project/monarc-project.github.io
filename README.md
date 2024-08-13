MONARC website
==============

# Installation

```bash
$ git clone https://github.com/monarc-project/monarc-project.github.io
$ cd monarc-project.github.io/
$ poetry install
```

# Deployment

## Check and publish

You can directly push your changes, but it is preferable to first check locally:

```bash
$  # you can also use pipenv shell
# generation of the static website:
$ make html
# or test with the development server:
$ make devserver
```

In case if `make devserver` command fails, it can be replaced with:
```
# only once:
$ pip install invoke
$ invoke build

# to start dev server:
$ invoke serve
```


Once everything looks fine, publish the changes:


```bash
$ git commit -S -am "<your comment>"
$ git push origin source
```

The website will be automatically generated thanks to GitHub Actions and the
result deployed on the MONARC GitHub Organization Pages
(available [here](https://www.monarc.lu)).
