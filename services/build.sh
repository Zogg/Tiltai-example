#!/bin/bash

cd nanomsg
./build.sh

cd ../feeder
./build.sh

cd ../encryptor
./build.sh

cd ../emailsink
./build.sh
