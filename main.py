class Student:
    # [assignment] Skeleton clnass. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    print("Details of new student:")

    def change_name(self, new_name):
        self.name = new_name
        print("Name: ", self.name)

    def change_age(self, new_age):
        self.age = new_age
        print("Age: ", self.age)

    def add_track(self, new_tracks):
        self.tracks = self.tracks + new_tracks 
        #self.tracks = self.tracks.append(new_tracks)
        print("Tracks: " , self.tracks)
    
    def get_score(self):
        print("Score: ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track(["UI/UX"])
Bob.get_score()
