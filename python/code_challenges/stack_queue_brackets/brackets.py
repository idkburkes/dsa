


def validate_brackets(string):
    open_brackets, stack = ('(', '{', '['), []
    bracket_dict ={ ']':'[', '}':'{', ')':'(' }
  
    for char in string:
        if char in open_brackets:
             # push open bracket to stack
            stack.append(char)
        elif char in bracket_dict:
             # check if last open bracket on stack matches current closed bracket
            if not stack or (stack.pop() != bracket_dict[char]):
                return False
    # If the stack has remaining brackets then return false
    return not stack
                
      