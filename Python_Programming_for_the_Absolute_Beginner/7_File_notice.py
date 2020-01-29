""" 
        Mode Description

"r"     Read from a text file. If the file doesn’t exist, Python will complain with an error.
"w"     Write to a text file. If the file exists, its contents are overwritten. If the file doesn’t exist, it’s created.
"a"     Append a text file. If the file exists, new data is appended to it. If the file doesn’t exist, it’s created.
"r+"    Read from and write to a text file. If the file doesn’t exist, Python will complain with an error.
"w+"    Write to and read from a text file. If the file exists, its contents are overwritten. If the file doesn’t exist, it’s created.
"a+"    Append and read from a text file. If the file exists, new data is appended to it. If the file doesn’t exist, it’s created.

"rb"    Read from a binary file. If the file doesn’t exist, Python will complain with an error.
"wb"    Write to a binary file. If the file exists, its contents are overwritten. If the file doesn’t exist, it’s created.
"ab"    Append a binary file. If the file exists, new data is appended to it. If the file doesn’t exist, it’s created.
"rb+"   Read from and write to a binary file. If the file doesn’t exist, Python will complain with an error.
"wb+"   Write to and read from a binary file. If the file exists, its contents are overwritten. If the file doesn’t exist, it’s created.
"ab+"   Append and read from a binary file. If the file exists, new data is appended to it. If the file doesn’t exist, it’s created.
"""

""" 
        Method Description
close()                 Closes the file. A closed file cannot be read from or written to until openedagain.
read([size])            Reads size characters from a file and returns them as a string. If size is not specified, the method returns all of the characters from the current position
to the end of the file.
readline([size])        Reads size characters from the current line in a file and returns them as a string. If size is not specified, the method returns all of the characters from
the current position to the end of the line.
readlines()             Reads all of the lines in a file and returns them as elements in a list.
write(output)           Writes the string output to a file.
writelines(output)      Writes the strings in the list output to a file.
"""


""" 
pickle a variety of objects, including:
• Numbers
• Strings
• Tuples
• Lists
• Dictionaries
"""