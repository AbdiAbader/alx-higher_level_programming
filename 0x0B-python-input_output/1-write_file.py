#!/usr/bin/python3
#""" Function that writes to file """


#def write_file(filename="", text=""):
 #   """ write to file """
  #  with open(filename,'w', encoding='utf-8') as f:
   #     return f.write(text)
       

"""
Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
