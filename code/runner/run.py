# -*- coding: utf-8 -*-

"""Documentation file main.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from tqdm import tqdm
from utils.helm import Helm
from tools.date import Date
from settings.log import Log
from utils.process import Process
from typing import NoReturn, Text
from settings.arguments import Arguments
from settings.exception import ExceptionDefault
from settings.configuration import Configuration

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# =============================================================================
# GLOBAL DEFINITION
# =============================================================================

config, args = Configuration(), Arguments(description="Helm Cleanup").args

namespace = args["namespace"] if args["namespace"] else (config.get_env("NAMESPACE") if config.get_env("NAMESPACE") else None)
all_namespaces = args["allnamespaces"] if args["allnamespaces"] else (config.get_env("ALL_NAMESPACES") if config.get_env("ALL_NAMESPACES") else None)
kubeconfig_path = ["kubeconfig_path"] if args["kubeconfig_path"] else (config.get_env("KUBECONFIG") if config.get_env("KUBECONFIG") else None)
helm_release_filter_days = int(["helm_release_filter_days"] if args["helm_release_filter_days"] else (config.get_env("HELM_RELEASE_FILTER_DAYS") if config.get_env("HELM_RELEASE_FILTER_DAYS") else None))

log_path = args["logpath"] if args["logpath"] else (config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else None)
log_file = args["logfile"] if args["logfile"] else (config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else None)

log = Log(log_path, log_file, config.get_env("LOG_LEVEL"), config.get_env("LOGGER")).logger

date, process, helm, exception = Date(log), Process(log), Helm(log), ExceptionDefault()

# =============================================================================
# FUNCTIONS
# =============================================================================

def run_execution(command: Text) -> NoReturn:
    
    today = date.date_today()

    try:
        output, errors = process.run_command(command)

        if errors:
            exception.raise_exception(Exception(f"We find errors when we run the command {command} - {errors}"))

        all_helm_releases = helm.get_all_helm_releases(output)

        helm.show_helm_releases(all_helm_releases, "Release")

        filtro = [[elemento[0], elemento[1]]  for elemento in all_helm_releases 
                            if date.days_between(elemento[2], str(today)) > helm_release_filter_days]

        if len(filtro) == 0:
            exception.raise_exception(Exception(f"We don't have any release to delete - Rule of {helm_release_filter_days} days not exceeded"))

        helm.show_helm_releases(filtro, "Release Filter")

        releases, namespaces = [release[0] for release in filtro], [namespace[1] for namespace in filtro]

        log.info("Applying helm delete")

        helm.delete_all_helm_releases(tqdm(releases), namespaces, process)   

    except Exception as error:
        log.error(f"Error general exception in run cleanup - {error}")

# =============================================================================

def run_cleanup() -> NoReturn:

    cprint(figlet_format("Cleanup", font="starwars"), "red", "on_yellow", attrs=["dark"])

    if all_namespaces and namespace is None:
        command = "helm list -d --filter '[a-z0-9\-]+feature[a-z0-9\-]+' --all-namespaces | awk '{print $1, $2, $4}'"
        run_execution(command)

    elif namespace and all_namespaces is None:
        command = f"helm list -d --filter '[a-z0-9\-]+feature[a-z0-9\-]+' -n {namespace}" + " | awk '{print $1, $2, $4}'"
        run_execution(command)

    else:
        log.warning("Nothing to do")
