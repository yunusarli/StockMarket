import re
 
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
 
def control(email,password):
    if(re.search(regex, email) and len(password)>=4):
        return True
    else:
        return False