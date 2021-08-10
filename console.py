import pdb
from models.staff import Staff
from models.animals import Animals
import repositories.staff_repository as staff_repository
import repositories.animal_repository as animal_repository

staff_repository.delete_all()

person1 = Staff("Jimz", "01/01/2000", "snake house", 5)
staff_repository.save(person1)

person2 = Staff("Susan", "02/02/2020", "lion den", 1)
staff_repository.save(person2)


staff_repository.select_all()

results = staff_repository.select_all()

for person in results:
    print(person.__dict__)


pdb.set_trace()