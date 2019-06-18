def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename)-1:
        index = pos if has_dot else pos+1 #? ternary operation
        return filename[index:]
    else:
        return ''