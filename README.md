

```bash
git clone --recursive <website-repository-url>

$ pew install 3.6.1 --type CPython
$ pew new --python=$(pew locate_python 3.6.1)  -a . -r requirements.txt monarc-website

$ git clone https://github.com/getpelican/pelican-themes
$ git clone https://github.com/getpelican/pelican-plugins

$ pelican -s pelicanconf.py
``
