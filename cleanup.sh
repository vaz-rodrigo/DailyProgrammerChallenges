#!/bin/bash

ls | grep -v "\[[a-zA-Z]*\]" | xargs -d"\n" rm -rf
