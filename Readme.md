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