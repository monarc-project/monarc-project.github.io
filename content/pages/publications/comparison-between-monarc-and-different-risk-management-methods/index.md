Title: Comparison between MONARC and different Risk Management Methods
Hidden: true


[TOC]

## 1. MONARC

### 1.1 Description

MONARC (in French: “_Méthode Optimisée d’aNAlyse des Risques CASES_”) simplifies risk management by offering a risk management solution as well as information security governance, based on industry standards. It allows analysis from existing and customisable models to be made in a short amount of time, while remaining compliant with the ISO/IEC 27005:2011 international standard.

MONARC is based on a library of risk models offering objects made of risk scenarios by assets or groups of assets. This approach simplify the management of the most common risks and increase objectivity as well as efficiency. As MONARC is completely repeatable, these results can be intensified and adjusted to the maturity of each organisation by increasing the depth of risk scenarios.

The MONARC risk analysis method is composed of four phases:

<div align="center">
  <img src="/assets/images/comparison-of-rm/monarc_1.png" width="60%">
</div>


** Context Establishment **

The first step is to take stock of the context, challenges and priorities of the company or organization that wishes to analyse its risks. This particularly serves to identify key activities and critical processes of the business in order to guide the risk analysis towards the most important elements. To do this, a kick-off meeting is organized with the members of the management and key persons. The goal is to know what makes the company «live» and what could destroy it, to identify the key processes, the internal and external threats as well as organisational, technical and human vulnerabilities.

** Context Modelling **

This phase includes the modelling of objects and trees. The assets were identified in the previous phase. They must now be detailed and formalised in a diagram that displays their interdependencies.

Impacts are defined at the level of the primary assets (processes or information), following the information gathered in the context establishment phase. The secondary assets inherit the impact of the primary asset to which they are attached (object tree).
The impact level of the secondary assets can be modified manually.

** Evaluation and treatment of risks **

The assessment consists of quantifying the threats, vulnerabilities and impacts in order to calculate the risks.

To do this, it is necessary to have reliable information about the exact likelihood of the threats, the ease of exploitation of vulnerabilities and potential impacts; hence the need to rely on metrics that have been validated by experts.

When the risk assessment identifies a risk that is higher than the acceptable level (risk acceptance grid), risk treatment measures should be implemented in order to reduce the risk down to an acceptable level.

** Implementation and monitoring **

When the first treatment of risks has been carried out, an ongoing management phase with security monitoring and recurring control of security measures must be entered, in order to improve it in a sustainable way.

This fourth phase also allows to continuously optimising the security by increasing the detail of objects used and by expanding the scope of the risk analysis.

### 1.2 MONARC Vs ISO 27005:2011

The four phases of MONARC fully respect the ISO/IEC 27005:2011 international standard, which contains the guidelines for risk management as related to information security. A comparison with MONARC is displayed below:

<div align="center">
  <img src="/assets/images/comparison-of-rm/monarc_2.png" width="60%">
</div>

### 1.3	MONARC Tool

The tool associated with MONARC allows access to the knowledge bases, as well as modifying and sharing them. MONARC provides export and import features, so that users can easily exchange risk models.

The tool also allows a very great modelling feature with "Drag & Drop" function. The proposed hierarchical structure is very simple to use. This is a great advantage as it simplifies the implementation of the changes in the model at each iteration.

## 2. ISO 31000

### 2.1	Description

ISO 31000: 2009 (“_Risk management – Principles and guidelines_”) is intended to harmonize risk management processes with existing and future standards. It provides guidelines on how to organize and manage effectively all kinds of risks in all kinds of organizations.

ISO 31000:2009 introduce a new definition of risk, abandons the technical vision ("_risk is the combination of event probability and its consequence_") to link risks with the objectives of the organization: "_Risk is the effect of uncertainty on objectives_". This definition is more in line with the management point of view.

** Structure of the standard **

The standard is structured in three parts:

1. The principles answer the question of why risk management is done. The process of integrating these principles takes place at two levels: the decision-making level and the operational level.

2. The organizational framework explains how to integrate risk management into the strategy of the organization (strategic management) via the iterative process of the Deming wheel (Plan-Do-Check-Act).

3. The management process specifies how to integrate risk management at the operational level


<div align="center">
  <img src="/assets/images/comparison-of-rm/iso_31000.png" width="70%">
</div>

** What is not ISO 31000? **

A certificate standard that provides detailed instructions: ISO 31000 only provides the general principles of risk management and highlights the framework and processes that should be implemented. Only 24 pages to describe the norm.

### 2.2	ISO 31000 vs. MONARC

ISO 31000 describes how to approach risk management strategically and understandable; and does not offer any specific advice about information security risk assessment nor risk treatment. From a technical point of view, ISO 31000 lists various risk management processes without a complete description.

MONARC gives guidelines for information security risk assessment and treatment, it gives the “know-how” to identify assets, threats and vulnerabilities, to assess impact, consequences and probability in order to calculate risk.

MONARC is compliant with ISO 31000.

<div align="center">
  <img src="/assets/images/comparison-of-rm/iso_31000_1.png" width="40%">
</div>


## 3. ISO 27005:2011

### 3.1	Description

ISO/IEC 27005:2011 (“_Information technology — Security techniques — Information security risk management (second edition)_”).

ISO 27005 provides an iterative framework compliant with ISO 27001 and set of processes for effective risk management. Half of the standard are appendices that provide examples and very useful information to help the user implement the method.

ISO 27005 is only dedicated to risk management in information security domain. It proposes either qualitative or quantitative risk management and does not advise any methods or tools.

ISO 27005 refers to the ISO 31000 risk management process, but provides much more detail and implementation guidance.

As shown in the figure below, there are some differences, especially "decision points", which are added to possibly refine the risk assessment and the risk treatment stages.
There is also an additional risk acceptance process. It ensures that residual risks are explicitly accepted by the management of the organization. This is particularly important in a situation where the implementation of controls is omitted or postponed.

<div align="center">
  <img src="/assets/images/comparison-of-rm/iso_27005_1.png" width="50%">
</div>

### 3.2	ISO 27005 vs. MONARC
MONARC is fully compliant with ISO 27005.

ISO 27005 is dedicated to information risks. MONARC can also manage operational risks for which, the risk treatment is done directly on reputation, operation, legal, financial criterias. The impact to the person can also be considered (in particular for the GDPR).

ISO 27005 gives the choice to use a qualitative or quantitative method, MONARC is a purely qualitative method.

The free software provided with MONARC allows to extend the risk management up to the monitoring of the implementation of the security measures.

<div align="center">
  <img src="/assets/images/comparison-of-rm/iso_27005_2.png" width="40%">
</div>

## 4. MAGERIT

### 4.1	Description
MAGERIT (in Spanish: “_Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información_”) is a method for risk analysis and management for information systems, developed by the Spanish ministry of public administrations.

This method provides a management framework and a structured approach to risk management in accordance with ISO 27005.

The method provides valuable knowledge databases based on assets, threats and security measures, as well as different techniques to conduct qualitative or quantitative risk analyzes.

The analysis approach is structured into three main parts: planning, risk analysis and risk management.

The distinctive characteristic of the method lies in the modelling of assets which takes into account the dependencies between assets. Dependency values are used to calculate asset degradation values. The impact criteria used for this inheritance link are confidentiality, integrity, availability, authenticity and accountability.
When calculating the potential impact, 3 values are considered:

* the accumulated impact (depending on the dependencies)
* the deflected impact (intrinsic value)
* the aggregated impact (aggregation of impact values)

These three types of impacts make it possible to calculate the three associated risks (minimum, median, max ...)

The analysis approach is as follows:

** Identification of assets **

* Information and services are upper assets.
* Other assets are lower assets (types of assets are given by the method and structured into layers).

**	Dependency building **

Assets are organized into a hierarchical tree structure. An upper asset depends on all lower assets.

**	Asset valuation **

Lower assets in the dependencies diagram are said accumulating the value of the assets supported by them. The value may be its own or may be accumulated.

**	Identification and valuation of threats **

Magerit gives a list of typical threats according to a relationship between the types of asset.

** Determination of impact **

Its own plus the accumulated value of the assets that depend on it.

**	Determination of the risk **

Being aware of the threat’s impact to the assets, the risk can be derived directly simply by taking into account the frequency of occurrence.

**	Safeguards **

Reducing the frequency of threats and/or impact limitations. Calculation of the residual risk.

<div align="center">
  <img src="/assets/images/comparison-of-rm/magerit_1.png" width="50%">
</div>

### 4.2	Magerit vs. MONARC

Magerit gives the choice to use a qualitative or quantitative method, MONARC is only a qualitative method.

Magerit uses 5 dimensions for impact criteria: confidentiality, integrity, availability, authenticity and traceability. MONARC only uses 3 dimensions, but provides the direct consequences on the ROLFP criteria, (Reputation, Operation, Legal, Financial, to the Person)

ISO 27005 is dedicated to information risks. MONARC can also manage operational risks.

The hierarchical model of the assets for the two methods is very similar:

*	With Magerit the inherited values of the three types of impacts are set up in the links of dependence.
*	With MONARC, dependency inheritance is always 100% by default, but it is possible to redefine the impact at each level of the hierarchy.

There is another big difference between Magerit and MONARC in order to calculate the risk:

*	Version v1.0 of Magerit introduced the notion of vulnerability. In v3.0, this notion is replaced by the degradation (amount of damage to the [asset value]) that is a threat parameter.
*	MONARC uses the concept of asset vulnerability that is related to the security measures in place and threats.

Depending on the situation, it is easier to check the security measure in place than evaluated the damage to an asset.

The two methods have a tool associated. The tool for MONARC is free.

 
## 5. OCTAVE
### 5.1	Description

OCTAVE® (“_Operationally Critical Threat, Asset, and Vulnerability Evaluation_”) is a risk-assessment method.

There are 3 versions of the OCTAVE method that address organizations of different sizes. The latest up-to-date version based on the first two is called OCTAVE Allegro.

The method consists in a series of workshops conducted and facilitated by an interdisciplinary analysis team drawn from business units throughout the organization.

Structure of the method: There are four distinct areas of activity that are carried out through eight steps in workshop-style.

For each step, the method proposes predefined questionnaires and worksheets in order to collect information in a structured way.

<div align="center">
  <img src="/assets/images/comparison-of-rm/octave_1.png" width="60%">
</div>

** Establish risk measurement criteria **

* Definition of a qualitative set of measures (risk measurement criteria).
* Prioritization of the impact areas from most important to least important.

** Develop an information asset profile **

* Identification of a collection of information assets.
* Evaluation of impact, if information is disclosed, modified, destroyed …
* Collection of the necessary information in order to begin the structured risk assessment process (scope, owner, impact criteria, security requirements).

** Identify information asset containers **

* Identification of asset containers (supporting asset: hardware, software, people …) either inside or outside of the organization.

** Identify areas of concern **

* Identification of areas of concern each of the containers that have been listed.
* Documentation of each area of concern that has been identified.
* Creation of threat scenarios.

** Identify threat scenarios **

* Identification of additional threat scenarios:

  - A tree structure is used to visually represent a range of threat scenarios.
  - Threat scenarios questionnaires are reviewed.

** Identify risks **

* Determine how threat scenarios that have been recorded on each information asset risk worksheet could affect your organization.

** Analyse risks **

* According to risk measurement criteria: Evaluation of the consequences relative to each of the impact areas.
* Calculation of a score for each risk.

** Select Mitigation Approach **

* Mitigation of the risk (accept, mitigate or defer).
* Categorization of risks (risk matrix).
* Assignation of a mitigation approach to each of your risks.

### 5.2	OCTAVE vs. MONARC

OCTAVE does not require the use of any tool for a first iteration of risk analysis. MONARC method is closely attached to the tool.

The identification of threats and threat scenarios is highly dependent on the skills of those involved in OCTAVE. MONARC has knowledge databases that provide default relationships between assets and threats.
 
## 6. EBIOS
### 6.1	Description

EBIOS (in French: “_Expression des Besoins et Identification des Objectifs de Sécurité_”) is a method of risks management and risks assessment of the French government.

The EBIOS method complies with the requirements of the main information security standards: ISO 31000 and ISO 27005, allows implementing ISO 27001, and exploiting controls of ISO 27002.

The method is rigorous and exhaustive as the tool that guides the user step by step, without the possibility of bypassing any step.

Risk models are based on the relationship between primary and asset assets. The tool provides comprehensive basic knowledge on media assets, threats, vulnerabilities...

The method follows the below steps:

<div align="center">
  <img src="/assets/images/comparison-of-rm/ebios_1.png" width="50%">
</div>

** Context study **

*	Definition of the context and risk management framework, metrics and scope of study.
*	Identifying essential assets and mapping the supporting assets on which they are based.

** Study of feared events **

*	Identification of security requirements in terms of availability, integrity, confidentiality.
*	Identification of impacts: Reputation, operation, legal, financial ...

** Threat scenario study **

*	Identification and assessment of risk scenarios.
*	Study of threats and sources of threats and exploitable vulnerabilities.

** Risk study **

*	Matching risks and feared events to threat scenarios.
*	Risk assessment.
*	Identification of the security objective’s to be met in order to address the risks.

** Study of security measures **

*	Treatment of risks.
*	Validation of risk treatment and residual risks.
*	Planning for implementing security measures.

The tool offers many deliverable solutions, according to the objectives of the users.

### 6.2	EBIOS vs. MONARC

The two methods are rather opposite, one proposes a structured and exhaustive approach (sometimes long and complicated), the other proposes a faster approach, based on small iterations that allow rapid evolutions. Software takeover time is not comparable at all.

Both tools offer an assisted approach and provide comprehensive knowledge databases. MONARC provides its own knowledge bases, but also those of EBIOS 2004 where the threats and vulnerabilities are distinct.

In EBIOS, risk assessment is based on the likelihood of threat scenarios. In MONARC, risk assessment is rather based on vulnerabilities of assets, which are easier to evaluate (measures in place or a repository of good practices).

In EBIOS, it is necessary to define security requirements, which is very difficult in low-maturity organizations. MONARC defines a security baseline to be reached with its default risk model.

## 7. IT-Grundschutz

### 7.1	Description

IT-Grundschutz is part of a series of standards, relating to information security and published by the German Federal Office for Information Security (BSI).

IT-Grundschutz is more a method of risk management than risk assessment. For a standard context, it is not necessary to carry out a risk analysis, as this has already been done.

<div align="center">
  <img src="/assets/images/comparison-of-rm/it-Grundschutz_1.png" width="50%">
</div>

The methodology consists of several standards that describe the management framework, the implementation of the ISMS, the risk management and risk assessment method, but above all a catalog of more than 4000 pages containing knowledge bases on assets, threats, vulnerabilities and especially thousands of good practices concerning configurations of all types (Hardware, software…).

<div align="center">
  <img src="/assets/images/comparison-of-rm/it-Grundschutz_2.png" width="60%">
</div>

The objective of the risk assessment is to provide a qualitative method in order to identifying, analysing and evaluating security incidents that may adversely affect the business. The standards describe a risk assessment at two levels: one is designed to achieve a "standard" level of security, and a second "complementary risk analysis" can be undertaken by organizations that want an approach that is appropriate to their needs.

<div align="center">
  <img src="/assets/images/comparison-of-rm/it-Grundschutz_3.png" width="60%">
</div>

For companies implementing a "standard" Information Security Management System based on IT-Grundschutz, the risk assessment is done by using the IT-Grundschutz guide books. These contain repositories of common threat scenarios and standard security countermeasures applicable to most IT environments and grouped by modules corresponding to various business environments and information system components.

In order to achieve a higher level of information security, a "supplementary risk analysis based on IT-Grundschutz" can also be performed by taking the following steps:

** Prepare an overview of threats **

A list of relevant threats is created for each asset that need to be analysed by using the IT-Grundschutz catalog.

** Determine additional threats **

Any threats specific to the application scenario are identified via a brainstorming session.

** Assess the threats **

The threat summary is systematically analysed to determine if the implemented and/or planned security measures provide adequate protection for each target object and threat. Thus, all relevant security mechanisms are checked for completeness, strength and reliability.

** Select safeguards for handling risks **

Decisions are made at the managerial level on the way risks not adequately mitigated are to be handled. Options include: reducing risk via safeguards, avoiding risk, transferring risk and accepting risk.

** Consolidate results **

The new security policy and mechanisms as a whole is verified, checked for consistency, user friendliness and adequacy to the target environment.

### 7.2	IT-Grundschutz vs. MONARC

One of the big differences of the IT-Grundschutz method compared to other methods is the bottom-up approach. Indeed, security is based on a predefined risk analysis of each element that makes up an information system, not a business asset-based approach.
The tool (GS-tool) allows to optimize the use of the method by selecting the pages of the catalog to be implemented in order to obtain an adequate level of protection.
One of the major problems of the IT-Grundschutz is that there are latencies in the English translation of the catalogs. Better to be German-speaking, to have up-to-date knowledge databases.

## 8. References

** ISO 31000:2009 **

* [Risk Management – Principles and Guidelines](https://www.iso.org/standard/43170.html)

** ISO 27005:2011 **

* [Information technology — Security techniques — Information security risk management](https://www.iso.org/standard/56742.html)

** MAGARIT **

* [Methodology for Information Systems Risk Analysis and Management Book](https://administracionelectronica.gob.es/pae_Home/dam/jcr:80b16a91-75b1-432d-ab23-844a12aab5fc/MAGERIT_v_3_book_1_method_PDF_NIPO_630-14-162-0.pdf)
* [Methodology for Information Systems Risk Analysis and Management Book I – The Method](https://administracionelectronica.gob.es/pae_Home/dam/jcr:80b16a91-75b1-432d-ab23-844a12aab5fc/MAGERIT_v_3_book_1_method_PDF_NIPO_630-14-162-0.pdf)
* [Methodology for Information Systems Risk Analysis and Management II - Catalogue of Elements](https://administracionelectronica.gob.es/pae_Home/dam/jcr:9c699ff6-63c4-43cf-8315-baffbf51197f/BIBLIOTECA_PUBLICACIONES_MAGERIT_VOL_II_INGLES.pdf)
* [Methodology for Information Systems Risk Analysis and Management III – Techniques](https://administracionelectronica.gob.es/pae_Home/dam/jcr:eea9fd1f-ced2-40e6-870d-a1ba483dece7/BIBLIOTECA_PUBLICACIONES_MAGERIT_VOL_III_INGLES.pdf)

** OCTAVE **

* [Introducing OCTAVE Allegro: Improving the Information Security Risk Assessment Process](https://resources.sei.cmu.edu/asset_files/TechnicalReport/2007_005_001_14885.pdf)
* [Method Implementation Guide Version 2.0 Volume 2: Preliminary Activities](http://www.dtic.mil/get-tr-doc/pdf?AD=ADA634139)
* [Implementation Guide, Version 1.0 Volume 1](ftp://ftp.sei.cmu.edu/pub/documents/04.reports/pdf/04hb003-01-introduction-to-octave-s.pdf)
* [Implementation Guide, Version 1.0 Volume 2](ftp://ftp.sei.cmu.edu/pub/documents/04.reports/pdf/04hb003-02-preparation-guidance.pdf)
* [Implementation Guide, Version 1.0 Volume 3](ftp://ftp.sei.cmu.edu/pub/documents/04.reports/pdf/04hb003-03-method-guidelines.pdf)
* [Implementation Guide, Version 1.0  Volume 4](ftp://ftp.sei.cmu.edu/pub/documents/04.reports/pdf/04hb003-04-organizational-worksheets.pdf)
* [Implementation Guide, Version 1.0 Volume 9](ftp://ftp.sei.cmu.edu/pub/documents/04.reports/pdf/04hb003-09-strategy-and-plan-worksheets.pdf)

** EBIOS 2010 **

* [La méthodologie](https://www.ssi.gouv.fr/uploads/2011/10/EBIOS-1-GuideMethodologique-2010-01-25.pdf)
* [Les bases de connaissances](https://www.ssi.gouv.fr/uploads/2011/10/EBIOS-2-BasesDeConnaissances-2010-01-25.pdf)

** IT-Grundschutz **

* [Information Security Management Systems (ISMS)](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/BSIStandards/standard_100-2_e_pdf.pdf?__blob=publicationFile)
* [IT-Grundschutz Methodology](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/BSIStandards/standard_100-1_e_pdf.pdf?__blob=publicationFile&v=1)
* [Risk analysis based on IT-Grundschutz](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/BSIStandards/standard_100-3_e_pdf.pdf?__blob=publicationFile)
* [IT-Grundschutz-Catalogues](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/download/threats_catalogue.pdf?__blob=publicationFile&v=2)


** ENISA **

* [Inventory of risk assessment and risk management methods](https://www.enisa.europa.eu/publications/information-packages-for-small-and-medium-sized-enterprises-smes/at_download/fullReport)
* [Reference source for threats, vulnerabilities, impacts and controls in IT risk assessment and risk management](https://www.enisa.europa.eu/publications/archive/reference-source-for-threats-vulnerabilities-impacts-and-controls-in-it-risk-assessment-and-risk-management/at_download/fullReport)
* [ENISA Website](https://www.enisa.europa.eu/topics/threat-risk-management/risk-management/current-risk/risk-management-inventory/rm-ra-methods)
