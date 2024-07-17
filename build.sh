#!/bin/bash

entrypoint='hello'
exe='hello.pyz'
reqs='requirements.txt'
pipenv lock
pipenv requirements > ${reqs}
shiv -c ${entrypoint} -o ${exe} -r ${reqs}  .
