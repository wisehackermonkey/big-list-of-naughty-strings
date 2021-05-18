###	Quick Python Script to convert the Big List of Naughty Strings into a JSON file
### 
###	By Max Woolf
import sys
import json

def print_all_naughty_strings(text=""):
    with open('../blns.txt', 'r') as f:

        # put all lines in the file into a Python list
        content = f.readlines()
        
        # above line leaves trailing newline characters; strip them out
        content = [x.strip('\n') for x in content]
        
        # remove empty-lines and comments
        content = [x for x in content if x and not x.startswith('#')]
        print(len(content))
        for string in content:
            print(text + string)
        # insert empty string since all are being removed
        # content.insert(0, "")
        
        # special case: convert "\" to "\\" for valid JSON
        #content = map(lambda x: x.replace('\','\\'), content)
        
# with open('../blns.json', 'wb') as f:
# 	# write JSON to file; note the ensure_ascii parameter
# 	json.dump(content, f, indent=2, ensure_ascii=False)
    
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        input_text = " ".join(args[1:])
        print(input_text)
        print_all_naughty_strings(input_text) 
    else:
        print("Useage: python3 txt_to_json.py <custom text here>")
        print("EX: Input:  python3 txt_to_json.py  'http://example.com/'")
        print('    Output: "http://example.com/() { 0; }; touch /tmp/blns.shellshock1.fail;"')
        # print_all_naughty_strings()