import argparse

p = argparse.ArgumentParser()
p.add_argument('-p',help='Optional parameters')
p.add_argument('-a',help='Optional parameters')
p.add_argument('-b',help='Optional parameters')
p.add_argument('-c',help='Optional parameters')

args = p.parse_args()['a']
