#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(log):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++

  ufile = urllib.urlopen(log)
  ufiletext = ufile.read()
  #print ufiletext

  url = re.findall(r'GET\s([\S]+)\.jpg\s',ufiletext)
  #print url

  url_list = []
  for u in url:
    if not u in url_list:
      url_list.append('http://code.google.com' + u + '.jpg')

  url_list_duped = []

  for d in url_list:
    if not d in url_list_duped:
      url_list_duped.append(d)

  return sorted(url_list_duped)
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    print "Directory does not exist; creating..."
    os.makedirs(dest_dir)

  i = 0
  for u in img_urls:
    print("Retrieving..." + u)
    urllib.urlretrieve(u, os.path.join(dest_dir, str(i) + '.jpg'))
    i += 1

  f = open(os.path.join(dest_dir,'index.html'), 'w')
  index_head = '<verbatim> <html> <body>'
  index_foot = '</body></html>'
  f.write(index_head)

  image_paths = os.listdir(dest_dir)
  #print sorted(image_paths)
  #sys.exit(0)
  n = 0
  for image_url in img_urls:
    local_name = 'img%d.jpg' % n
    f.write('<img src="' + os.path.abspath(os.path.join(dest_dir,local_name) + '">'))
    n += 1

  #for image in sorted(image_paths):
  #  i = re.search(r'(\d+)\.jpg',image)
  #  if i:
  #    f.write('<img src="'+ os.path.abspath(os.path.join(dest_dir,image[0])) + '.jpg">')

  f.write(index_foot)
  f.close()

  #<img src="/edu/python/exercises/img0"><img src="/edu/python/exercises/img1"><img src="/edu/python/exercises/img2">...</body></html>'

  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
