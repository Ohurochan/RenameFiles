# Python program to rename all file
# names in your directory
from asyncio.windows_events import NULL
import os
import sys
import argparse

def get_args():
    # Generate ArgParser
    argParser = argparse.ArgumentParser()
    argParser.add_argument("srcDir")
    argParser.add_argument("findKey")
    argParser.add_argument("--replaceKey", help="optional")

    # 結果を受ける
    args = argParser.parse_args()

    return(args)

def RemoveKeyword(srcDir, findKey):
    for count, fname in enumerate(os.listdir(srcDir)):
        f_name, f_ext = os.path.splitext(fname)
        f_name = f_name.replace(findKey, "")

        new_name = f'{f_name}{f_ext}'
        os.rename(f'{srcDir}/{fname}', f'{srcDir}/{new_name}')
        # print(fname, "==>", new_name)

def ReplaceKeyword(srcDir, findKey, replaceKey):
    for count, fname in enumerate(os.listdir(srcDir)):
        f_name, f_ext = os.path.splitext(fname)
        f_name = f_name.replace(findKey, replaceKey)

        new_name = f'{f_name}{f_ext}'
        os.rename(f'{srcDir}/{fname}', f'{srcDir}/{new_name}')
        # print(fname, "==>", new_name)

# Driver Code
if __name__ == '__main__':
    # Get argments
    args = get_args()

    # Call Function
    if args.replaceKey is None:
        # Remove keyword
        RemoveKeyword(args.srcDir, args.findKey)
    else:
        # Replace keyword
        ReplaceKeyword(args.srcDir, args.findKey, args.replaceKey)
