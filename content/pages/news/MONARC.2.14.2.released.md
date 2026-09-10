Title: MONARC 2.14.2 released
Date: 2026-09-10
Category: monarc
Tags: monarc, new-release
Summary: Release 2.14.2 of MONARC

Version 2.14.2 delivers fixes for issues introduced or identified in v2.14.1, improving asset imports and search results, operational risk recommendations, risk-management views, risk-treatment calendars, and MFA one-time-code autofill.

### New

- [Highlighting asset search results](https://github.com/monarc-project/MonarcAppFO/issues/623)

### Fixes

- [Import rename assets to "<asset_name> - Imp. #1" when multiple asset have the same name](https://github.com/monarc-project/MonarcAppFO/issues/620)
- [Operational risk recommendations display issue](https://github.com/monarc-project/MonarcAppFO/issues/628)
- [Problems with "Synthesis of assets" and "Risks management organisation"](https://github.com/monarc-project/MonarcAppFO/issues/622)
- [Buggy calendar in risk treatment](https://github.com/monarc-project/MonarcAppFO/issues/624)
- [MFA OTP input field incorrectly uses autocomplete="new-password" instead of autocomplete="one-time-code"](https://github.com/monarc-project/MonarcAppFO/issues/610)


## Documentation

The updated [User guide HTML](/documentation/user-guide/) and [PDF](/assets/files/guides/user-guide.pdf) include the new functionality. The ISO 27005:2022 additions are also available as a separate [HTML guide](/documentation/iso27005_2022_adaptations/) and [PDF guide](/assets/files/guides/iso27005_2022_adaptations.pdf).

## Updating

Follow the standard [MONARC update guide](https://monarc.lu/documentation/technical-guide/#monarc-update).

> **Important:** If your MONARC installation includes a BackOffice, update the BackOffice to **v2.14.1** (if the BackOffice version is lower) together with the FrontOffice. The FrontOffice application will not work with an outdated BackOffice.

### Ansible deployment

Update the Ansible repository if this was not done during the v2.14.1 update.

For MONARC installations deployed with [ansible-ubuntu](https://github.com/monarc-project/ansible-ubuntu), a BackOffice with multiple FrontOffice clients, - it's required to update the Ansible repository before deploying this release. It contains the new FrontOffice-client configuration changes. Updating the repository only requires pulling the latest `master` branch:

```bash
git pull origin master
```

More details are available on the [GitHub Release v2.14.2](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.14.2){:target="_blank"}.


## Local installation (Docker + application)

Monarc FrontOffice can also be installed locally using Docker and a small utility to execute docker commands, configure and update the Monarc FO tool.

To install the application:

- Install Docker on your system.
- Download the appropriate application package for your operating system from [here](https://vm.monarc.lu/apps/){:target="_blank"}.
- Follow the setup instructions included with the package.

For detailed installation steps and additional information, refer to the official documentation [here](https://monarc.lu/documentation/technical-guide/#end-user-app).


## MONARC BackOffice application

There is now new release, so v2.14.1 needs to be used / installed. The details can be found [here](https://github.com/monarc-project/MonarcAppBO/releases/tag/v2.14.1){:target="_blank"}.
