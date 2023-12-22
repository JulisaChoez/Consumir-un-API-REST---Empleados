import requests

# URL del API
url = 'https://dummy.restapiexample.com/api/v1/employees'

# Realizar una solicitud GET
response = requests.get(url)

# Obtener el contenido JSON de la respuesta
data = response.json()

# Obtener la lista de empleados
employees = data["data"]

# Contar la cantidad de empleados
employee_count = len(employees)

# promedio de salario de los empleados
salary_sum = 0
for employee in employees:
    salary_sum += employee["employee_salary"]

# promedio de edad de los empleados
age_sum = 0
for employee in employees:
    age_sum += employee["employee_age"]

# Inicializar el salario mínimo y máximo
min_salary = None
max_salary = None

# Iterar sobre la lista de empleados
for employee in employees:
    salary = employee["employee_salary"]

    # Actualizar el salario mínimo si es necesario
    if min_salary is None or salary < min_salary:
        min_salary = salary

    # Actualizar el salario máximo si es necesario
    if max_salary is None or salary > max_salary:
        max_salary = salary

# Inicializar la edad menor y mayor
min_age = None
max_age = None

# Iterar sobre la lista de empleados
for employee in employees:
    age = employee["employee_age"]

    # Actualizar la edad menor si es necesario
    if min_age is None or age < min_age:
        min_age = age

    # Actualizar la edad mayor si es necesario
    if max_age is None or age > max_age:
        max_age = age

# Imprimir los resultados
print(f"La cantidad de empleados es: {employee_count}")
print(f"El promedio de salario es: {salary_sum / employee_count}")
print(f"El promedio de edad es: {age_sum / employee_count}")
print(f"El salario mínimo es: {min_salary}")
print(f"El salario máximo es: {max_salary}")
print(f"La edad mínima es: {min_age}")
print(f"La edad máxima es: {max_age}")