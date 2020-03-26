from application.db.people import get_employees
from application.sallary import calculate_salary
import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    time = datetime.datetime.now()
    print(time.strftime("%d-%m-%Y"))

