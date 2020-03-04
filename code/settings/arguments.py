# -*- coding: utf-8 -*-

"""Documentation file arguments.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import argparse
from typing import NoReturn, Text

# =============================================================================
# CLASS - ARGUMENTS
# =============================================================================

class Arguments(object):

    def __init__(self, *args, **kwargs) -> NoReturn:
        self._parser = self._create_parser_object(*args, **kwargs)
        self._build()

    @staticmethod
    def _create_parser_object(*args, **kwargs) -> argparse.ArgumentParser:
        try:
            return argparse.ArgumentParser(*args, **kwargs)
        except argparse.ArgumentError as error:
            print(f"\nError when we create a parser object - {error}")
        except Exception as error:
            print(f"\nError general exception in create a parser object - {error}")

    def _adding_arguments(self) -> NoReturn:
        try:
            self._parser.add_argument("-n", "--namespace",
                                    type=str,
                                    metavar="<namespace>",
                                    default=None,
                                    help="Kubernetes get specific namespace")
            self._parser.add_argument("-all", "--allnamespaces",
                                    action="store_true",
                                    default=False,
                                    help="Kubernetes get all namespaces")
            self._parser.add_argument("-kcp", "--kubeconfig_path",
                                    type=str,
                                    metavar="<kubeconfig>",
                                    default=None,
                                    help="Just the Kubeconfig path")
            self._parser.add_argument("-hrfd", "--helm_release_filter_days",
                                    type=str,
                                    metavar="<days>",
                                    default=None,
                                    help="Helm release creation days to delete")
            self._parser.add_argument("-lp", "--logpath",
                                    type=str,
                                    metavar="<logpath>",
                                    default=None,
                                    help="Custom Log path name")
            self._parser.add_argument("-lf", "--logfile",
                                    type=str,
                                    metavar="<logfile>",
                                    default=None,
                                    help="Custom Log file name")
        except Exception as error:
            print(f"\nError general exception in define all arguments used on the command line - {error}")

    def _parser_args(self) -> argparse.ArgumentParser.parse_args:
        try:
            return self._parser.parse_args()
        except Exception as error:
            print(f"\nError general exception in parser the arguments from standard input - {error}")

    def _build(self) -> NoReturn:
        try:
            self._adding_arguments()
            self._args = vars(self._parser_args())
        except Exception as error:
            print(f"\nError general exception to populate the parser object with the information - {error}")

    @property
    def args(self) -> Text:
        return self._args
