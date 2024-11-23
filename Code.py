class Solution:
    def simplifyPath(self, path: str) -> str:
  
        name = path.split('/')
        stack = []

        for part in name:
            if part == "..":
                if stack:  
                    stack.pop()
            elif part == "." or not part:  
                continue
            else:  
                stack.append(part)
        return "/" + "/".join(stack)
