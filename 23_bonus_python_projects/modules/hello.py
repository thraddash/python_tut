#!/usr/bin/env python
import argparse

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('person_name')
    args = parser.parse_args(argv)

    greet = f"Hello {args.person_name}"
    print(greet)
    return greet

if __name__ == '__main__':
   main()

