#import moduls and global variabls
from abc import ABC,abstractmethod
from string import digits , ascii_letters
import random


#create  password genarator abstract calass
class PasswordGeneratorAbstraction(ABC):
    @abstractmethod
    def generator(self,length=8):
        pass

#create numeris password generator
class NumericPasswordGenerator(PasswordGeneratorAbstraction):
    letters= digits
    def generator(self,length=8):
        return "".join (random.choice(self.letters) for _ in range(length))

#create letters password generator
class LettersPasswordGenerator(PasswordGeneratorAbstraction):
    letters= ascii_letters
    def generator(self,length=8):
        return "".join (random.choice(self.letters) for _ in range(length))

#craete combine password generator
class MixedPasswordGenerator(PasswordGeneratorAbstraction):
    letters= ascii_letters + digits
    def generator(self,length=8):
        return "".join (random.choice(self.letters) for _ in range(length))

#run application
generator = MixedPasswordGenerator()
print(generator.generator())