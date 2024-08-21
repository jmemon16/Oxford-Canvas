
import dotenv
import os
import requests
import pandas as pd

from canvasapi import Canvas

# Collect following information from your canvas site

course_id = 229557   # minidrone (204336)
assignment_id = 629048 # Minidrone Workshop HT24 Submission (673096)


# load variables from .env file
dotenv.load_dotenv(dotenv.find_dotenv())

# read TOKEN from .env
TOKEN = os.environ.get('CANVAS_ACCESS_TOKEN')


# ensure token is defined in dotenv
if TOKEN == None:
    print("No access token found. Please set `CANVAS_ACCESS_TOKEN`")
    exit()


# retrieve base URL of canvas
BASE_URL = os.environ.get('CANVAS_URL')

# open canvas as canvas_obj
canvas_obj = Canvas(BASE_URL, TOKEN)

# open course 
course_obj = canvas_obj.get_course(course_id)      # 202533 is course ID (see in URL)

# show course name
print(course_obj.name)

assig_obj= course_obj.get_assignment(assignment_id)     # 616096 is assignment ID (see in URL)



# show assignment name
print(assig_obj.name)

# get_submissions
submissions = assig_obj.get_submissions()


for submission in submissions:

    if submission.score is not None:
        print("Score: ", submission.score, "Number of Attempts: ",submission.attempt)      # print score of each submission
        #newscore = submission.score  # keep previous scope
    else:
        # Treat no submission as 0 points
        #newscore = 0
        print(submission.user_id)          # print user id of each submission

    #submission.edit(submission={'posted_grade': newscore})
    





"""
#create an assignment

from datetime import datetime

new_assignment = course.create_assignment({
    'name': 'Assignment 3',
    'submission_types': ['online_upload'],
    'allowed_extensions': ['docx', 'doc', 'pdf'],
    'notify_of_update': True,
    'points_possible': 100,
    'due_at': datetime(2018, 12, 31, 11, 59),
    'description': 'Please upload your homework as a Word document or PDF.',
    'published': True
})

print(new_assignment)



"""



"""
# Set `score` to a Int value
submission = assignment.get_submission(student_id)
submission.edit(submission={'posted_grade':score})

"""
