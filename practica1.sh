#!/bin/bash 

echo "user's ip: "
curl --GET "https://www.passwordrandom.com/query?command=ip"

echo "user's passwd: "
curl --GET "https://www.passwordrandom.com/query?command=password"
