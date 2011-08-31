#!/bin/bash

mailbody="/tmp/emailmsg.`date +%Y-%b-%d.%s`"
mailbodytail="/tmp/emailmsgtail.`date +%Y-%b-%d.%s`"

# Define email address to send report to
mailto=shai@me.com
mailcc=shai@me.com

echo "=== The End! ===" > $mailbodytail

function emailme {
  echo "This is me, running ..." >> $mailbody
  echo >> $mailbody
  cat $mailbodytail >> $mailbody
  mutt -e 'set realname="do not reply" from=noreply@domain.com' -s "`hostname` - State of $1" $mailto -c $mailcc < $mailbody
  rm $mailbody $mailbodytail
}

emailme "this code"
