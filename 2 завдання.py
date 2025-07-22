from pathlib import Path

def get_cats_info(path):
    path = Path(path)
    information = []
    try:
        with path.open(encoding="utf-8") as file:
            for line in file:
                id, name, age = line.strip().split(",")
                info = {"id": id, "name": name, "age": age} 
                information.append(info)
    except FileNotFoundError:
        print("Файлу {path} не було знайдено.")
        return None
    return information

information = get_cats_info("goit-algo-hw-04\\second.txt")
# print(information)