Title: MONARC 2.14.1 released
Date: 2026-08-18
Category: monarc
Tags: monarc, new-release
Summary: Release 2.14.1 of MONARC

Version 2.14.1 introduces ISO 27005:2022 asset-based alignment, PDF report generation, blank analyses, and CyFun referentials.

### New

- [Asset-based ISO 27005:2022 alignment](https://github.com/monarc-project/MonarcAppFO/issues/576): risk sources, reassessment triggers and schedules, risk-review governance, residual-risk approval, risk history, and role-based risks management. See the [ISO 27005:2022 adaptations HTML guide](/documentation/iso27005_2022_adaptations/) or [PDF guide](/assets/files/guides/iso27005_2022_adaptations.pdf).
- [PDF report generation](https://github.com/monarc-project/MonarcAppFO/issues/615): select PDF when generating a deliverable. See the [User guide](/documentation/user-guide/#generate-a-pdf-report).
- [Blank Analysis](https://github.com/monarc-project/MonarcAppFO/issues/324): create an empty analysis without Knowledge Base or Assets Library data. See the [User guide](/documentation/user-guide/#creating-a-risk-analysis).
- [CyFun referential integration](https://github.com/monarc-project/MonarcAppFO/issues/616): use the CyFun Basic, Important, and Essential 2025 referentials with ISO 27002 mappings. See the [User guide](/documentation/user-guide/#cyfun-referentials).

## Documentation

The updated [User guide HTML](/documentation/user-guide/) and [PDF](/assets/files/guides/user-guide.pdf) include the new functionality. The ISO 27005:2022 additions are also available as a separate [HTML guide](/documentation/iso27005_2022_adaptations/) and [PDF guide](/assets/files/guides/iso27005_2022_adaptations.pdf).

## Updating

Follow the standard [MONARC update guide](https://monarc.lu/documentation/technical-guide/#monarc-update).

More details are available on the [GitHub Release v2.14.1](https://github.com/monarc-project/MonarcAppFO/releases/tag/v2.14.1){:target="_blank"}.


## Local Installation (Docker + Application).

Monarc FrontOffice can also be installed locally using Docker and a small utililty to execute docker commands, configure and update the Monarc FO tool.

To install the application:

- Install Docker on your system.

- Download the appropriate application package for your operating system from [here](https://vm.monarc.lu/apps/){:target="_blank"}.

- Follow the setup instructions included with the package.

For detailed installation steps and additional information, refer to the official documentation [here](https://monarc.lu/documentation/technical-guide/#end-user-app).


## Monarc BackOffice application.

The is also a new BackOffice release available. The details can be found [here](https://github.com/monarc-project/MonarcAppBO/releases/tag/v2.13.5){:target="_blank"}.
