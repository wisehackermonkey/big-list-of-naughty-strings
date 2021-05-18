import sys
import requests
def print_all_naughty_strings(text="",file_output_name="../output/output_v1.txt"):
    with open('../blns.txt', 'r') as f:

        # put all lines in the file into a Python list
        content = f.readlines()
        
        # above line leaves trailing newline characters; strip them out
        content = [x.strip('\n') for x in content]
        
        # remove empty-lines and comments
        content = [x for x in content if x and not x.startswith('#')]
        # print(len(content))
        with open(file_output_name,"w") as file:
            for string in content:
                new_url = text + string 

                print("====================\nURL:" +new_url)
                print(requests.get(new_url).text)
                file.write(requests.get(new_url).text)
                file.write("=============================\n")

if __name__ == "__main__":
    try:
        args = sys.argv
        print(len(args))
        if 3 > len(args) > 1:
            input_text = " ".join(args[1:])
            print("INPUT:" + input_text)
            print("==== OUTPUT ======")
        if len(args) == 3:
            input_text = args[1]
            output_filename = args[2]
            print("INPUT:" + input_text)
            print("==== OUTPUT ======")
            
            print("==== OUTPUT filename ======")
            print(output_filename)
            print("==========")

            print_all_naughty_strings(input_text,output_filename) 
        else:
            print("Useage: python3 txt_to_json.py <custom text here> <output filename>")
            print("EX: Input:  python3 txt_to_json.py  'http://example.com/'")
            print('    Output: "http://example.com/() { 0; }; touch /tmp/blns.shellshock1.fail;"')
            # print_all_naughty_strings()
    except KeyboardInterrupt:
        print("\b\b\n\nshutting down")