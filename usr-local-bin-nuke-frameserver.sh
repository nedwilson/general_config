#!/bin/bash

NUKE_DIR=/usr/local/Nuke11.0v3
pushd $NUKE_DIR

./python ./pythonextensions/site-packages/foundry/frameserver/nuke/runframeserver.py --useInteractiveLicense --numworkers=6 --nukeworkerthreads=4 --nukeworkermemory=6144 --workerconnecturl=tcp://hibiki:5560 --nukepath=./Nuke11.0
