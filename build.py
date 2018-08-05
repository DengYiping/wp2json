import json
import os
import re
import time

INPUT_FOLDER = 'out'
OUTPUT_FOLDER = 'json'
md_matcher = re.compile('(.+)\\.md')

if not os.path.isdir(INPUT_FOLDER):
    os.mkdir(INPUT_FOLDER)

if not os.path.isdir(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

#input file list
input_file_dict = {}
for fname in os.listdir(INPUT_FOLDER):
    match_result = md_matcher.match(fname)
    if match_result:
        input_file_dict[match_result.group(1)] = fname

rst = {}

for key in input_file_dict:
    fname = input_file_dict[key]
    md_str = ''

    with open(os.path.join(INPUT_FOLDER, fname), 'r') as f:
        md_str = f.read()
    
    post = {
        'title': key,
        'date': time.strftime('%Y-%m-%d %H:%M'),
        'md': md_str
    }

    output_key = key.replace(' ', '_')
    rst[output_key] = post

    with open(os.path.join(OUTPUT_FOLDER, output_key + '.json'), 'w') as f:
        f.write(json.dumps(post))

with open(os.path.join(OUTPUT_FOLDER, 'posts.json'), 'w') as f:
    f.write(json.dumps(rst))