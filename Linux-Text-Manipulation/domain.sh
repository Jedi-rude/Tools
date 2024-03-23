#!/bin/bash
for hostname in $(cat $1); do
	host $hostname | grep "has address"
done
