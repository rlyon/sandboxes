#!/bin/sh
source $1/functions.sh

FILE="zabbix-2.2.6.tar.gz"
SRC="http://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Stable/2.2.6/zabbix-2.2.6.tar.gz/download"
download_unless_present $FILE $SRC
