#!/usr/bin/env python

import sys, os, re, subprocess, paramiko

#search = sys.argv[1]
#hosts = sys.argv[2]

command = "coach /server list"

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('shell.iad3a.mlsrvr.com',username='scot8965')

stdin, stdout, stderr = ssh.exec_command(command)

print stdout.read()
