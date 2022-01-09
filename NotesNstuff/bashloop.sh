#!/usr/bin/bash.exe

n=0
command=$1
while ! $command && [[ $n -le 5 ]]; do
	sleep 1
	((n=n+1))
	echo "Retry #$n"
done;