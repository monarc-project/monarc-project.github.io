MONARC website
==============

Installation
------------

```bash
$ git clone --recursive https://github.com/monarc-project/website.git
$ cd website/

$ sudo -H pip install pew
$ pew install 3.6.1 --type CPython
$ pew new --python=$(pew locate_python 3.6.1)  -a . -r requirements.txt monarc-website

$ make html
```

Deployment
----------
