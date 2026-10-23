Title: PHP runtime security notice for MONARC deployments
Date: 2026-10-23
Category: security
Tags: security, php, advisory
Slug: php-runtime-security-notice
Summary: Update affected PHP web runtimes for CVE-2026-109618 and CVE-2026-109619.

The reported vulnerabilities affect the PHP runtime, not the MONARC application
code itself. However, MONARC installations using an affected PHP version to
serve web requests may be exposed.

Please apply your operating system or vendor security update for
**CVE-2026-109618** and **CVE-2026-109619**, then restart the affected web
server or PHP workers.

For Ubuntu, see the
[Ubuntu Security Notice USN-8948-1](https://ubuntu.com/security/notices/USN-8948-1).
In particular, Ubuntu 22.04 installations using PHP 8.1 should update to
Ubuntu package version `8.1.2-1ubuntu2.28` or later.

Please verify the PHP runtime used by the web server, not only the CLI version.
This applies to Apache mod_php, PHP-FPM, CGI, and other PHP web SAPIs.

For other operating systems, follow the relevant vendor security advisory and
ensure it explicitly addresses both CVEs.

More information is available in
[CIRCL TR-102](https://www.circl.lu/pub/tr-102/).
