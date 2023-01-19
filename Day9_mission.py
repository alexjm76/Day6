#class

class Pokemon:
    def __init__(self,name,owner,skills): #객체 생성시 동작
        #print("포케몬 객체 생성됨")
        self.name = name
        self.owner = owner
        self.skills = skills.split("/")
        print(f"포케몬 {name}생성됨")
    def info(self):
        print(f"{self.owner}의 포켓몬은 {self.name}입니다")
        for skill in self.skills:
            print(skill)
class Pikachu(Pokemon):
    pass

pil = Pikachu("피카츄", "덴트", "번개")
pil.info()
p1 = Pokemon("피카츄", "한지우" , "50만 볼트/100만볼트/번개")
p2 = Pokemon("꼬부기", "오바람", "고속스핀/커품/몸통박치기/하이드로펌프")

# print(p1, p2)
# print(f"{p1.name}의 포켓몬은 {p1.owner}입니다")
print(p1.skills)
p2.info()
p1.info()