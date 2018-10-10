#!/bin/bash

set -Ceuo pipefail

rpm -q rpm-build   >/dev/null || sudo yum install -qy rpm-build
rpm -q rpmdevtools >/dev/null || sudo yum install -qy rpmdevtools
rpm -q yum-utils   >/dev/null || sudo yum install -qy yum-utils

if [[ ! -f $HOME/.rpmmacros ]]; then
  cp -fp .rpmmacros $HOME/.rpmmacros
fi

spectool -g -R SPECS/unit.spec
sudo yum-builddep SPEC/unit.spec
