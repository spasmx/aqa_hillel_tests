import argparse

parser = argparse.ArgumentParser(add_help=False, description='myparser')

parser.add_argument('--name', '-n', type=str)
parser.add_argument('--help', '-h', action='store_true')

args = parser.parse_args()

if args.help:
    print('Тут могла бути ваша... допомога =)')

if args.name is not None:
    if args.name == 'Валєнтін':
        print('Валєнтін, японскій бог, ти зачєм у ката яйца-та аткрутіл?!')
    else:
        print(f'Welcome, {args.name}!')






