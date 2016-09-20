#!/bin/bash

set -e 

rsync -e ssh -avz --include="**/" --include="**/p*q*/**" --exclude="**" tsunami:/home/wfarr/guywhiten/real_data/ ./
