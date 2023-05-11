# library to call apis mainly based on ubco-canvasapi-collection
# -*- coding: utf-8 -*-


import dotenv
import os
import requests




# load variables from .env file
dotenv.load_dotenv(dotenv.find_dotenv())


# ensure access token is available
token = os.environ.get('CANVAS_ACCESS_TOKEN')

if token == None:
    print("No access token found. Please set `CANVAS_ACCESS_TOKEN`")
    exit()


# retrieve base URL of canvas
url = os.environ.get('CANVAS_URL')

# Static settings
# retrieve entries per page

per_page = int(os.environ.get('CANVAS_PER_PAGE'))

# ensure access token is available

auth_header = {'Authorization': 'Bearer ' + token} # setup the authorization header to be used later

# ensure that COURSE_STATE is valid
COURSE_STATE = os.environ.get('CANVAS_COURSE_STATE')

if not COURSE_STATE in ["unpublished", "available", "completed", "deleted"]:
    print("Invalid course state. Please set `CANVAS_COURSE_STATE` to one of [unpublished, available, completed, deleted]")
    exit()




#read url and token from config file
# config = ConfigParser()
# config.read('canvas.cfg')
# environment = config['default']['env']



#api calls
def getAssignments(courseID):
    assignments = []
    page = 1
    while True:
        request_url = url + '/api/v1/courses/' + str(courseID) + '/assignments'
        params = {"per_page": str(per_page), "page": str(page)}
        r = requests.get(request_url, headers=auth_header, params=params)
        r.raise_for_status()
        data = r.json()
        if len(data) == 0:
            break
        assignments += data
        page+=1
        if len(assignments) == 0:
            print("No students found to report on.")
            exit()
    return assignments

def getAssignmentSubmission(courseID, assignmentID):
    assignments = []
    page = 1
    while True:
        request_url = url + '/api/v1/courses/' + str(courseID) + '/assignments/' + str(assignmentID) + '/submissions'
        params = {"per_page": str(per_page), "page": str(page), 'include[]': ['submission_comments', 'user']}
        r = requests.get(request_url, headers=auth_header, params=params)
        r.raise_for_status()
        data = r.json()
        if len(data) == 0:
            break
        assignments += data
        page+=1
        if len(assignments) == 0:
            print("No students found to report on.")
            exit()
    return assignments   

def getCourseDetails(courseID):
    courseDetails = requests.get(url + '/api/v1/courses/' + str(courseID),
                                 headers = {'Authorization': 'Bearer ' + token})
    return courseDetails.json()
	
def getCourseStudents(courseID):
    courseStudents = []
    page = 1
    while True:
        request_url = url + '/api/v1/courses/' + str(courseID) + '/users'
        params = {"per_page": str(per_page), "page": str(page), 'enrollment_type': 'student'}
        r = requests.get(request_url, headers=auth_header, params=params)
        r.raise_for_status()
        data = r.json()
        if len(data) == 0:
            break
        courseStudents += data
        page+=1
        if len(courseStudents) == 0:
            print("No students found to report on.")
            exit()
    return courseStudents