from pathlib import Path

def total_salary(path):
    path = Path(path)
    salaries = []
    try:
        with path.open(encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                salary = float(salary)
                salaries.append(salary)

    except FileNotFoundError: 
        print(f"Файл {path} не було знайдено.") 
        return "?", "?" 
     
    if not salaries:
        print("В списку немає зарплат.")
        return 0.0, 0.0

    total = sum(salaries)
    average = total / len(salaries)

    return total, average

total, average = total_salary("goit-algo-hw-04\\first.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



            