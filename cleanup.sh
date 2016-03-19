#!/bin/bash

# Author: Freddie Vargus (github.com/FreddieV4)
# Purpose: Removes any files/dirs not containing [Easy/Intermediate/Hard]

ls | grep -v "\[[a-zA-Z]*\]" | xargs -d"\n" rm -rf
