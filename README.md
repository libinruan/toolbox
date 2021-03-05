1. getCode.py extracts code snippets from a markdown file
   type: 
       {string} input: name of markdown file (.md)
       {string} output: name of the output python file (.py)
       {bool} comment_flag: if True, keep comments; otherwise, discard coments. 
       {bool} jupyter_flag: if True, add '# %%' to first line of a code block. 
       {bool} packed_flag: if True, add one change line after the last line of a code block.
   rtype: None

