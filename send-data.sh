#!/bin/bash

git add -A; git commit -m "Add this weeks challenges"; git push

read -r line < ../mynumber.txt

echo "Repo Successfully Updated" | .././twilio-sms.sh -c /.twiliorc/config $line
