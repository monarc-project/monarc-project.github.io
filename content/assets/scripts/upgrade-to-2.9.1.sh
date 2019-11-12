#! /usr/bin/env bash


# Everything must be executed with the normal user.
if [[ $EUID -eq 0 ]]; then
    echo "This script must not be executed with root privileges." 2>&1
    exit 1
fi

# Clean old directories
rm -Rf vendor/
rm -Rf module/
rm -Rf data/cache

# Create new required directories
mkdir -p module/Monarc
mkdir -p data/cache
mkdir -p data/DoctrineORMModule
mkdir -p data/LazyServices/Proxy

# Updated code MONARC PHP libraries and dependencies
composer install -o

# Create new symlinks
cd module/Monarc
ln -s ./../../vendor/monarc/core Core
if [[ -d ./../../vendor/monarc/frontoffice ]]; then
    ln -s ./../../vendor/monarc/frontoffice FrontOffice
else
    ln -s ./../../vendor/monarc/backoffice BackOffice
fi


# Update all the project
./scripts/update-all.sh -c

exit 0
