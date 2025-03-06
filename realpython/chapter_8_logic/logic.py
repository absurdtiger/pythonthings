# 8.2 add some logic

# and logic gate: returns true if both booleans are true
# or logic gate: returns true if at least one booleans is true
# not: reverses the value of a single expression
# for booleans you need to watch out for operator precedence

# operator order is as follows:
# [highest] < <= == >= >
# [] not
# [] and
# [lowest] or

# for False == not True, python tries to evaluate False == not, which is not valid
# it's better to group with parenthesis
# meanwhile you can use not with the worded logic gates without issue

# try:
# True and False == True and False
# operators have higher precedence
# True and (False == True) and False
# True and False and False
# False


