from institutes.models import Course


import json

def prepareCourseList(institute_id):
    courses = Course.objects.filter(institute_id=institute_id)

    course_list = []
    for course in courses:
        course_list.append((course.id, course.name))
    print('++++++', course_list, '++++++++')

    return course_list

# def reCaptchaTest(request):
#     grecapresp = request.POST.get('g-recaptcha-response')
#     secretkey = '6Lc1r9waAAAAAHqwW1Exk7eo4SwCU8qYjnh3Ak1X'

#     url = 'https://www.google.com/recaptcha/api/siteverify'

#     postparams = {'secret': secretkey, 'response': grecapresp}

#     resp = requests.post(url, data=postparams)

#     respdict = json.loads(resp.text)

#     return respdict['success']