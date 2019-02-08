import csv


def read_routes(filepath):
    routes = []
    with open(filepath) as file:
        for row in csv.DictReader(file, delimiter=";"):
            routes.append(row)
    routes = [
        {key: value.strip() for key, value in row.items()}
        for row in routes
    ]
    return routes


def format_routes(routes):
    formated_routes = []
    for route in routes:
        formated_routes.append(
            route["Dep. Airport"] + " - "
            + route["Arr. Airport"] + ": from "
            + route["Starting From"] + " till "
            + route["Running Till"] + ", "
            + route["Frequency"]
        )
    return formated_routes


def write_routes_to_file(filepath, routes):
    with open(filepath, "w") as file:
        for route in routes:
            file.write(route + "\n")


if __name__ == "__main__":
    routes = read_routes("I:/python/lessons/lesson_2/files/data.csv")
    routes = format_routes(routes)
    print(routes)
    write_routes_to_file("I:/python/lessons/lesson_2/files/data.txt", routes)
