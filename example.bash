#!/usr/bin/env bash
alias sunset='for i in {0..10}; do python /home/born/fhem-helpers/sunset-step.py --state-file sunset.state --fhem-server localhost --hue-devices HUEDevice1,HUEDevice2 --debug; sleep 30s; done'
alias party='while : ; do python /home/born/fhem-helpers/party.py --fhem-server localhost --hue-devices HUEDevice1,HUEDevice2 --debug; sleep 1s; done'
alias off='python /home/born/fhem-helpers/off.py --fhem-server localhost --hue-devices HUEDevice1,HUEDevice2 --debug'
