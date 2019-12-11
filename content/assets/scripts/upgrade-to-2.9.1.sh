#! /usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Everything must be executed with the normal user.
if [[ $EUID -eq 0 ]]; then
    echo  -e "${RED}This script must not be executed with root privileges.${NC}" 2>&1
    exit 1
fi

# Checks the version of PHP
vercomp () {
    if [[ $1 == $2 ]]
    then
        return 0
    fi
    local IFS=.
    local i ver1=($1) ver2=($2)
    # fill empty fields in ver1 with zeros
    for ((i=${#ver1[@]}; i<${#ver2[@]}; i++))
    do
        ver1[i]=0
    done
    for ((i=0; i<${#ver1[@]}; i++))
    do
        if [[ -z ${ver2[i]} ]]
        then
            # fill empty fields in ver2 with zeros
            ver2[i]=0
        fi
        if ((10#${ver1[i]} > 10#${ver2[i]}))
        then
            return 1
        fi
        if ((10#${ver1[i]} < 10#${ver2[i]}))
        then
            return 2
        fi
    done
    return 0
}

PHP_VERSION=`php -v | grep ^PHP | cut -d ' ' -f2 | cut -d '-' -f1`


if [[ $(vercomp $PHP_VERSION 7.2.0 ; echo $?) -eq 2  ]]; then
    echo -e "${RED}You are using an old version of PHP: $PHP_VERSION${NC}"
    echo "The migration should works but we advise you to update."
    echo "https://www.php.net/supported-versions.php"
    sleep 3
fi

if ! [ -x "$(command -v composer)" ]; then
  echo -e "${RED}Composer is not installed.${NC} Please install it:" >&2
  echo '    $ sudo apt-get install composer'
  exit 1
fi

# Update the root repository of MONARC
echo  -e "${GREEN}Updating root of the project…${NC}"
git pull origin master
if [[ $? -ne 0 ]]; then
    echo -e "${RED}Error when updating root of the project.${NC}"
    exit 1
fi

# Clean old directories
echo  -e "${GREEN}Removing old vendor, module and cache directories…${NC}"
rm -Rf vendor/
rm -Rf module/

# Create new required directories
echo  -e "${GREEN}Creating new module and cache directories…${NC}"
mkdir -p module/Monarc

# Update PHP dependencies of MONARC
echo  -e "${GREEN}Installing new PHP backend…${NC}"
composer clear-cache
composer install -o

# Create new symlinks
echo  -e "${GREEN}Creating new symlinks…${NC}"
cd module/Monarc
ln -s ./../../vendor/monarc/core Core
if [[ -d ./../../vendor/monarc/frontoffice ]]; then
    ln -s ./../../vendor/monarc/frontoffice FrontOffice
else
    ln -s ./../../vendor/monarc/backoffice BackOffice
fi
cd ../..

# Update all the project
echo  -e "${GREEN}Updating the whole project…${NC}"
./scripts/update-all.sh -c


echo  -e "${GREEN}Upgrade finished.${NC}"
echo "Checks the permission of the folder data/"


exit 0
