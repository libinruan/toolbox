# %%
"""
getCode is a function to extract code snippets from a markdown file. 
type: {string} input: name of markdown file (.md)
      {string} output: name of the output python file (.py)
      {bool} comment_flag: if True, keep comments; otherwise, discard coments. 
      {bool} jupyter_flag: if True, add '# %%' to first line of a code block. 
      {bool} packed_flag: if True, add one change line after the last line of a code block.
rtype: None
"""
import sys, getopt, re

def getCode(input, output, comment_flag, jupyter_flag, packed_flag):
    with open(input,'r') as ofile, open(output,'w') as nfile:
        text = []
        cnt = 0
        for line in ofile.readlines():
            str = line.split('#')[0]
            if '```' in str and 'python' in str:   
                if jupyter_flag: nfile.write('# %%\n')    
                cnt += 1
            elif '```' in str and cnt % 2 == 1:
                if not packed_flag: nfile.write('\n')
                cnt += 1
            elif not '```' in str and cnt % 2 == 1:
                if comment_flag == False:
                    nfile.write(str)
                else:
                    nfile.write(line)

def main(argv):
    input_file = ''
    output_file = ''
    comment_flag = False
    jupyter_flag = False
    packed_flag = False
    try: 
        opts, args = getopt.getopt(argv, "hi:o:cjp", ['ifile=', 'ofile', 'comment', 'jupyter', 'packed'])
    except getopt.GetoptError:
        print('python getCode.py -i <input filename> -o <output filename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python getCode.py -i <input filename> -o <output filename>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
        elif opt in ('-c', '--comment'):
            comment_flag = True
        elif opt in ('-j', '--jupyter'):
            jupyter_flag = True
        elif opt in ('-p', '--packed'):
            packed_flag = True            
    getCode(input_file, output_file, comment_flag, jupyter_flag, packed_flag)

if __name__ == "__main__":
    main(sys.argv[1:])