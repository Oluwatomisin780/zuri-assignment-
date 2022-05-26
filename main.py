
from audioop import add


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,track,score):
        self.name =name;
        self.age = age;
        self.track =track
        self.score = score
    def  initialization(self):
        print(f'Name={self.name},Age={self.age},Track ={self.track}, Score= {self.score}')
    def  change_name(self,change_name):
        self.change_name  = change_name
        print(f'{change_name}')
    def change_age(self,change_age):
        self.change_age = change_age
        print(f'{change_age}')
    def add_track(self,add_track):
        self.add_track = add_track 
        print(f'{add_track}')
    def get_score(self,get_score):
        self.get_score =get_score
        return get_score



bob = Student('oluwatomisin',23,'fullstack',50);
bob.initialization()
bob.change_name('peter')
bob.change_age(34)
bob.add_track('ui/ux')
bob.get_score(40)
# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
