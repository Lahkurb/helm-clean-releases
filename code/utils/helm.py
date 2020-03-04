# -*- coding: utf-8 -*-

"""Documentation file helm.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import NoReturn, Text, List, Callable

# =============================================================================
# CLASS - HELM
# =============================================================================

class Helm(object):

    def __init__(self, logger: Callable) -> NoReturn:
        self._logger = logger

    def show_helm_releases(self, releases: List, comment: Text) -> NoReturn:
        try:
            for index, release in enumerate(releases):
                self.logger.info(f"{comment} {index} - {release}")
        except Exception as error:
            self.logger.error(f"Error general exception in show the Helm Releases - {error}")

    def get_all_helm_releases(self, output: Text) -> List:
        try:
            return [elemento.split(" ") for elemento in [elemento.strip() 
                                            for elemento in output.splitlines()][1::]]
        except Exception as error:
            self.logger.error(f"Error general exception in get all Helm Releases. - {error}")

    def delete_helm_release(self, release: Text, namespace: Text, process: Callable) -> Text:
        try:
            command = f"helm del {release} -n {namespace}"
            self.logger.debug(f"Deleting helm release - {release} in namespace - {namespace} - {command}")
            output, errors = process.run_command(command)
            if errors:
                raise Exception(f"We find errors when we run the command {command} - {errors}")
            return output
        except Exception as error:
            self.logger.error(f"Error general exception in delete the helm release {release} in namespace {namespace}")

    def delete_all_helm_releases(self, releases: Text, namespaces: Text, process: Callable) -> NoReturn:
        try:
            for value, release in enumerate(releases):
                output = self.delete_helm_release(release, namespaces[value], process)
                if output:
                    self.logger.info(f"Output Delete - {output}")
        except Exception as error:
            self.logger.error(f"Error general exception in delete all helm releases - {error}")

    @property
    def logger(self) -> Text:
        return self._logger
