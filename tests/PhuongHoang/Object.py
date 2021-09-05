class person:
    def __init__(self, first_name, last_name, age): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def introduce(self):
        return f"Hi. I'm {self.first_name}. {self.last_name}. I'm {self.age} years old"



Phuong  = person ('Phoang', 'hoang', 25)

full_name = Phuong.get_full_name

print(f"{full_name}: {Phuong.introduce()}")

#print (f" i'm {Phuong.first_name} {Phuong.last_name}. I'm {Phuong.age} years old")

#https://www.youtube.com/c/TechWithTim/playlists