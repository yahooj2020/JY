#!/bin/bash

for url in `cat l.txt`
do
    wget "$url"
done