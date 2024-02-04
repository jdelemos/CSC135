def has_duplicate_value(d):
    s = set()
    
    for v in d.values():
        if v in s:
            return True
        s.add(v)
    
    return False
