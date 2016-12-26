from argparse import ArgumentParser
from webscrape import call_Yelp

parser = ArgumentParser(prog="findinyelp")
parser.add_argument('desc', type=str)
parser.add_argument('loc', type=str)
parser.add_argument('-results', type=int)

args = parser.parse_args()
if args.results is None:
	call_Yelp(desc=args.desc, loc=args.loc)
else:
	call_Yelp(desc=args.desc, loc=args.loc, nos=int(args.results))
# call_Yelp(desc=args.desc, loc=args.loc, nos=nos)