MONARC website
==============

Installation
------------

```bash
$ git clone --recursive https://github.com/monarc-project/website.git
$ cd website/

$ sudo apt-get install python-pip
$ sudo -H pip install pew
$ pew install 3.6.1 --type CPython
$ pew new --python=$(pew locate_python 3.6.1)  -a . -r requirements.txt monarc-website

$ make html
```

If you want to test with the development server:

```bash
$ make devserver
```

And go to the address: http://localhost:8000


Deployment
----------

```bash
$ ghp-import output
$ git push git@github.com:monarc-project/monarc-project.github.io.git gh-pages:master
```
