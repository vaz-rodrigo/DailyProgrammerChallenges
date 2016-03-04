#!/bin/bash

eval $(ssh-agent)
ssh-add /root/.ssh/id_rsa
git add -A; git commit -m "Add this weeks challenges"; git push
