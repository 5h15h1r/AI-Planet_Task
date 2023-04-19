## Aplication Overview
1. Create hackathons by authorized users only. All the hackathons should have some basic fields like 
    - Title
    - description
    - Background image
    - Hackathon image
    - type of submission - Only one of these types should be selected while creating the hackathon - image, file or a link. You can assume that this field cannot be changed after the hackathon has started.
    - Start datetime
    - End datetime
    - Reward prize
 
2. Listing of hackathons
3. Register to a hackathon
4. Make Submissions
    - Submissions should contain the following information
    - A name for the submission
    - Summary of the submission
    - Submission - Based on the type of submission mentioned above, submissions should be accepted. API should validate it.
5. Users should be able to list the hackathons they are enrolled to
6. Users should be able to view their submissions in the hackathon they were enrolled in.

## Endpoints


| Endpoints            | Request Type  | Parameters  |
| -------------        |:-------------:|:-------------:      |
| /api/v1/register     | POST          |username, email, paasword|
| /api/v1/token        | POST          |email,password|
| /api/v1/token/refresh| POST          |refresh token|
| /api/v1/hackathons   | GET           |NA|
| /api/v1/hackathons   | POST          |title,description,hackathonImage,typeofSubmission,start,end,reward|
| /api/v1/enroll/<int:pk>|POST         |pk:primary key of hackathon|
| /api/v1/enrolled     | GET           |NA|
| /api/v1/submission/<int:pk>| POST    |name,summary,submission|
| /api/v1/getsubmission| GET           |NA|

## Problem Statement
 The hackathon oraganiser can provide different options, but now the User has the option to choose from different type of submission while submitting

# Solution
class SubmissionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hackathon(models.Model):
    title = models.CharField(max_length=100, null=True) 
    description = models.CharField(max_length=500, null=True)
    hackathonImage = models.ImageField(upload_to='images')
    start = models.DateField()
    end = models.DateField()
    reward = models.CharField(max_length=100, null=True)
    participants = models.ManyToManyField(User, related_name="hackathons", blank=True)
    submission_types = models.ManyToManyField(SubmissionType, related_name="hackathons", blank=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    name = models.CharField(max_length=50, null=True)
    summary = models.CharField(max_length=300, null=True)
    participant = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    hackathon = models.ForeignKey(Hackathon, null=True, on_delete=models.SET_NULL)
    submission_type = models.ForeignKey(SubmissionType, null=True, on_delete=models.SET_NULL)
    fileSubmission = models.FileField(upload_to='hackathon/submissions/',null=True,validators=[FileExtensionValidator(['pdf'])]) 
    imageSubmission = models.ImageField(upload_to='hackathon/submissions/images',null=True,validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'svg'])]) 
    urlSubmission = models.URLField(null=True,validators=[URLValidator()])

