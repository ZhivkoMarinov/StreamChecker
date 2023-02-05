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
            parser.add_argument(arg, args_map[arg]['name'],
                                type=args_map[arg]['type'],
                                nargs=args_map[arg]['nargs'],
                                help=args_map[arg]['help'],
                                required=True)
        return parser

    @property
    def argument_parser(self):
        """:return argument parser"""
        return self.__argument_parser.parse_args()
