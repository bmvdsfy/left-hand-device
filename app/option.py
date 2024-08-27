from argparse import ArgumentParser

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument("--host", action="store_true")

    return argparser.parse_args()