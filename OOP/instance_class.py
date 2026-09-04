# In Python, an instance object is an individual object created from a class, When we create an object from a class, it is referred to as an instance.

class JobProfile:
    CompanyLeader = "Suresh"
    def __init__(self,jobRole,jobprofile,CompanyLeader):
        self.jobRole = jobRole
        self.jobProfile = jobprofile
        self.CompanyLeader = CompanyLeader
        
    def get_AllInfo(self):
        print(f"My Company role is {self.jobRole} and my jobProfile is {self.jobProfile} and CompanyLeader was {self.CompanyLeader}")


Job_info = JobProfile("Advisor", "Verification","Anil")
Job_info.get_AllInfo()

print(Job_info.CompanyLeader)

print(dir(Job_info))
        