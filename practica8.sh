#!/bin/bash

p_IP=$(curl ipconfig.me)
nmap scanme.nmap.org
nmap --script Discovery $p_IP

