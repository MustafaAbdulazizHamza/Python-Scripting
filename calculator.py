import argparse as ar
des = 'This prgram is used to add or subtract two numbers'
arg_parser = ar.ArgumentParser(description=des)
arg_parser.add_argument('-n1', '--num1', required=True, help='First number.')
arg_parser.add_argument('-n2', '--num2', required=True, help="Second number.")
arg_parser.add_argument('-s', '--subtract', action='store_true', help="To enable subtraction mode.")
arg = arg_parser.parse_args()
n1 = int(arg.num1)
n2 = int(arg.num2)
if arg.subtract: print(n1 - n2)
else: print(n1 + n2)



