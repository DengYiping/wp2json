# -*- coding: utf-8 -*-
import json
import re
import os
import sys
import time


def main():
    RECENT_JSON_PATH = '~/code/DengYiping.github.io/json/blogs.json'
    JSON_FLODER = '~/code/DengYiping.github.io/json/'
    RECENT_JSON_PATH = os.path.expanduser(RECENT_JSON_PATH)
    JSON_FLODER = os.path.expanduser(JSON_FLODER)

    if not os.path.isfile(RECENT_JSON_PATH):
        print('blogs.json file not find, check your path')
        exit(-1)

    if len(sys.argv) < 2:
        print('please specify a markdown file to continue')
        exit(-1)

    md_path = sys.argv[1]
    md_fname = os.path.basename(md_path)
    md_matcher = re.compile('(.+)\\.md')
    match_res = md_matcher.match(md_fname)
    post_name = match_res.group(1) # extract the name of the  blog post

    md_str = ''
    with open(md_path, 'r') as md_f:
        md_str = md_f.read() # read into string

    post_dic = {
        'title': post_name,
        'date': time.strftime('%Y-%m-%d %H:%M'),
        'md': md_str
    }

    # replace space with underscore as the json file name
    output_key = post_name.replace(' ', '_')
    output_fname = output_key + '.json'
    with open(os.path.join(JSON_FLODER, output_fname), 'w') as json_f:
        json_f.write(json.dumps(post_dic)) # write the json

    with open(RECENT_JSON_PATH, 'r+') as blogs_f:
        data = json.loads(blogs_f.read())
        data[output_key] = post_dic
        blogs_f.seek(0)
        blogs_f.truncate()
        blogs_f.write(json.dumps(data))
    print('successfully write to blog file and added to recent blogs')

if __name__ == '__main__':
    main()
