
# Challenge Summary
Write a function called validate brackets
- Arguments: string
- Return: boolean representing whether or not the brackets in the string are balanced

There are 3 types of brackets:

- Round Brackets : `()`
- Square Brackets : `[]`
- Curly Brackets : `{}`

## Approach & Efficiency
My approach to solve this problem is to use a stack and iterate over the string once. Each time I encounter an open bracket I will push it to the stack.
Each time I encounter a closed bracket, I will pop the first value of the stack and use a dictionary to compare it to the expected opening bracket for the closed bracket I encountered. If they don't match, or this is nothing on the stack then we'll return false.
Finally, we will check to see if the stack has any remaining items. If it does then we know the brackets are not balanced because there were more opening brackets than closing brackets

Time Complexity: O(n)

Space Complexity: O(1)

## Inputs & Outputs
- `"{}"`                     -> `TRUE`
- `"{}(){}"`                 -> `TRUE`
- `"()[[Extra Characters]]"` -> `TRUE`
- `"(){}[[]]"`               -> `TRUE`
- `"{}{Code}[Fellows](())"`  -> `TRUE`
- `"[({}]"`                  ->	`FALSE`
- `"(]("`                    ->	`FALSE`
- `"{(})"`                   ->	`FALSE`