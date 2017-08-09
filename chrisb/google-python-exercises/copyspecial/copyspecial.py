#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dirname):

  file_paths = []

  filenames = os.listdir(dirname)
  for filename in filenames:
    file = re.search(r'__(\w+)__', filename)
    if file:
      file_paths.append(os.path.abspath(os.path.join(dirname, filename)))
  
  return file_paths

def copy_to(paths, dir):

  if not os.path.exists(dir):
    print "Directory does not exist; creating..."
    os.makedirs(dir)
  
  for file in paths:
    name = os.path.basename(file)
    shutil.copy(file, os.path.join(dir,name))

def zip_to(paths, zipfile):

  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "I'm going to zip this bitch: ", cmd
  (status, output) = commands.getstatusoutput(cmd)

  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  files = []
  for file in args:
    files.extend(get_special_paths(file))

  if todir:
    copy_to(files, todir)

  elif tozip:
    zip_to(files,tozip)

  else:
    print '\n'.join(files)
  
if __name__ == "__main__":
  main()
