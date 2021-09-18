import json

from django.shortcuts import render
from django.views import View

from . import classes
from . import models



class RegisterView(View):

    response_dict = {}
    form_template = 'index.html'
    result_template = 'result.html'

    def get(self, request):
        return render(request, self.form_template)

    def post(self, request):
        req = models.Request()
        res = models.Response()
        user = classes.User(firstname=request.POST['first_name'], middlename=request.POST['middle_name'],
                            lastname=request.POST['last_name'], dateofbirth=request.POST['date_of_birth'],
                            gender=request.POST['gender'],
                            nationality=request.POST['nationality'], city=request.POST['city'],
                            state=request.POST['state'], pincode=request.POST['pincode'],
                            qualification=request.POST['qualification'], salary=request.POST['salary'],
                            pannumber=request.POST['pan_number'])
        user.validate_details()
        req.first_name = user.first_name
        req.middle_name = user.middle_name
        req.last_name = user.last_name
        req.date_of_birth = user.date_of_birth
        req.gender = user.gender
        req.nationality = user.nationality
        req.city = user.city
        req.state = user.state
        req.pincode = user.pincode
        req.qualification = user.qualification
        req.salary = user.salary
        req.pan_number = user.pan_number

        req.save()

        res.request_id = models.Request.objects.latest('id').id
        res.response = user.success_or_failure
        res.reason = user.reason

        res.save()


        if res.response == "Success":
            self.response_dict["Request_id"] = res.request_id
            self.response_dict["Response"] = res.response
        elif res.response == "Failure":
            self.response_dict["Request_id"] = res.request_id
            self.response_dict["Response"] = res.response
            self.response_dict["Reason"] = res.reason

        json_dump = json.dumps(self.response_dict)
        json_object = json.loads(json_dump)

        return render(request, self.result_template, {'json': json_object})
