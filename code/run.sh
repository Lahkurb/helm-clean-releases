#/usr/bin/env sh

##################################################
#### Script to run cleanup and set kubeconfig ####
##################################################

set -eo pipefail

echo -n "${KUBECONFIG_CLUSTER}" | base64 -d > "${KUBECONFIG}"

python ./main.py -all
