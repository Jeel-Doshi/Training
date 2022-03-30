# You have two files named questions.txt and answer.txt. You need to create a file that contains questions and answers. But both input files contain random questions followed by a numeric value. You need to match both values and then copy the question-answer pair in a new file.
# -> Optimize code properly.
# Sample file: question.txt:
#   3. What is your Hobby?
#   1. What is your name?
#   2. Where are you from?
# Sample file: answer.txt:
# 	2. India
# 	1. Bob
# 	3. Swimming
# Output file:
#   1. What is your name?
#   1. Bob
#   2. Where are you from?
#   2. India
#   3. What is your Hobby?
# 	3. Swimming

import os
import sys

with open(os.path.join(sys.path[0],'Question.txt'),'w') as questions:
    questions.write('3. What is your Hobby?\n1. What is your name?\n2. Where are you from?')
with open(os.path.join(sys.path[0],'Answer.txt'),'w') as answers:
    answers.write('2. India\n1. Bob\n3. Swimming')

with open('File_Handling/Question.txt','r') as questions:
    with open('File_Handling/Answer.txt','r') as answers:
        result = questions.read() +'\n'+ answers.read()
        list_result = result.splitlines()
        list_result.sort(key = lambda value:int(value[0]))

        with open('File_Handling/Result.txt','w') as result:
            result.write('\n'.join(list_result))