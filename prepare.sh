#!/bin/bash

set -Ceuo pipefail

rpm -q rpm-build   || sudo yum install -y rpm-build
rpm -q rpmdevtools || sudo yum install -y rpmdevtools
rpm -q yum-utils   || sudo yum install -y yum-utils

if [[ ! -f $HOME/.rpmmacros ]]; then
  ln -sfn .rpmmacros $HOME/.rpmmacros
fi

spectool -g -R SPEC/unit.spec
sudo yum-builddep SPEC/unit.spec
