from datetime import datetime
from application import salary
from application.db import people

if __name__ == '__main__':
    print(datetime.now())
    print(salary.calculate_salary())
    print(people.get_employees())


