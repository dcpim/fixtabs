#!/bin/bash
# Deploy fixtabs on the local system

set -e

if [ "$EUID" -ne 0 ]
	then echo "Please run as root"
	exit
fi

cp ./fixtabs.man /usr/share/man/man1/fixtabs.1
gzip -f /usr/share/man/man1/fixtabs.1
cp ./fixtabs.py /usr/bin/fixtabs
chmod a+x /usr/bin/fixtabs
