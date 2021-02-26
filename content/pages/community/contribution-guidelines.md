Title: Contribution guidelines
Date: 2017-07-03
Hidden: false

The GitHub issue tracker is for bug reports and feature requests.
Please do not use it to ask questions about how to use MONARC.

You can contribute to MONARC by:

* Reporting [bugs](https://github.com/monarc-project/MonarcAppFO/issues/new?labels=bug)
* Suggesting enhancements or [new features](https://github.com/monarc-project/MonarcAppFO/issues/new?labels=feature+request)
* Improving the [documentation](https://github.com/monarc-project/MonarcAppFO/issues/new?labels=documentation)

If you want to contribute to the code you can use our
[Vagrant development environment](https://github.com/monarc-project/MonarcAppFO/tree/master/vagrant).
This is more convenient.

## Bug reports

Please be aware of the following things when filing bug reports:

1. Avoid raising duplicate issues. Use the GitHub issue search feature
   to check whether your bug report has been mentioned in the past.
2. When filing bug reports about exceptions or tracebacks, please include the
   *complete* traceback (logs of Apache, etc.).
3. Make sure you provide a suitable amount of information. This
   means you should provide: **how to reproduce the issue**,
   **what you expected to happen**, **what actually happens**,
   **what version of MONARC you are using** and  **how you installed it**.

Did you write a patch that fixes a bug?

* Open a new GitHub pull request with the patch.
* Ensure the pull request description clearly describes the problem and the
  solution. Include the relevant issue number if applicable.

If the bug concerns a
[security issue](/community/vulnerability-disclosure).

## New feature requests

Ideas of new features should always be discussed in an new issue on GitHub.

Do you intend to add a new feature or change an existing one?

* Suggest your change in an issue with the tag [feature request](https://github.com/monarc-project/MonarcAppFO/issues/new?labels=feature+request).
* Open a pull request if you have collected positive feedback and can implement it yourself.


## Contribution to the translations

If you are willing to improve the translations of MONARC or if MONARC is not
yet available in your language, you can help us via our
[internationalization platform](https://translate.monarc.lu/projects/monarc/).


## Contribution to the documentation

Contributions to the documentation are also always welcome.

Please uses
[Markdown](https://daringfireball.net/projects/markdown/).
[MarkdownMode](https://www.emacswiki.org/emacs/MarkdownMode) is of great help
for that. If you are using the ATOM editor, you should also find some Markdown
extensions.

Do not version binary files (*.docx* document, etc.). for the
documentation or anything else. It easier to follow the changes of plain text
files.

[Pandoc](http://pandoc.org/) is a wonderful tool to convert files from one
markup format into another.
