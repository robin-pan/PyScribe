from argparse import ArgumentParser

class ArgParser:
  def parse(self):
    argParser = ArgumentParser()
    argParser.add_argument('filename', metavar='filename', type=str,
                        help='path to musicxml file')
    return argParser.parse_args()