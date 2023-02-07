import argparse

ARGUMENTS = {
    '-o': {'type': str.lower, 'name': '--operator', 'nargs': None,
           'help': 'Operator name'},
    '-st': {'type': int, 'name': '--start_time', 'nargs': None,
            'help': 'in which minute to start'},
    '-i': {'type': int, 'name': '--interval', 'nargs': None,
           'help': 'interval between checks'},
}


class CommandLineArguments:
    """
    Class responsible for reading and parsing command line arguments.
    """

    def __init__(self):
        self.__argument_parser = self.create_parser(ARGUMENTS)
        self.__is_complete = False
        self.check_is_complete()

    def __str__(self):
        return self.__argument_parser

    @staticmethod
    def create_parser(args_map):
        """
        Creates arg parser from arguments dict
        :param args_map: ARGUMENTS dict
        :return: parsed data
        """
        parser = argparse.ArgumentParser(description="StreamChecker")
        for arg in args_map:
            parser.add_argument(
                arg,
                args_map[arg]['name'],
                type=args_map[arg]['type'],
                nargs=args_map[arg]['nargs'],
                help=args_map[arg]['help'],
            )
        return parser

    def check_is_complete(self):
        if self.argument_parser.operator is not None and\
                self.argument_parser.start_time is not None and\
                self.argument_parser.interval is not None:
            self.__is_complete = True

    @property
    def argument_parser(self):
        """:return argument parser"""
        return self.__argument_parser.parse_args()

    @property
    def is_complete(self):
        return self.__is_complete
