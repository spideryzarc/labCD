from pydantic import BaseModel

class Retangulo(BaseModel):
    base: float
    altura: float

    def area(self) -> float:
        return self.base * self.altura
    
r1 = Retangulo(base=5, altura='bola')
print(r1)