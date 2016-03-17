#!/bin/bash

# Author: Freddie Vargus (github.com/FreddieV4)
# Purpose: Used to move challenge directories into parent directories

find -maxdepth 1 -type d -iname "*[Easy*" -exec mv {} "Easy Challenges"/ \;

find -maxdepth 1 -type d -iname "*[Intermediate*" -exec mv {} "Intermediate Challenges"/ \;

find -maxdepth 1 -type d -iname "*[Difficult*" -exec mv {} "Hard Challenges"/ \;

find -maxdepth 1 -type d -iname "*[Hard*" -exec mv {} "Hard Challenges"/ \;
