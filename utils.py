import json


def load_candidates():
    """которая загрузит данные из файла"""
    with open("candidates.json", "r") as file:
        file_str = json.load(file)
    return file_str

#print(load_candidates())


def get_all(candidates):
    """которая покажет всех кандидатов"""
    candidates_list = []
    for candidate in candidates:
        candidates_list.append(candidate["name"])
    return candidates_list

# candidates = [{'pk': 1, 'name': 'Adela Hendricks', 'picture': 'https://picsum.photos/200', 'position': 'Go разработчик', 'gender': 'female', 'age': 40, 'skills': 'go, python'}, {'pk': 2, 'name': 'Sheri Torres', 'picture': 'https://picsum.photos/200', 'position': 'Delphi developer', 'gender': 'female', 'age': 26, 'skills': 'Delphi, pascal, fortran, basic'}, {'pk': 3, 'name': 'Burt Stein', 'picture': 'https://picsum.photos/200', 'position': 'Team lead', 'gender': 'male', 'age': 33, 'skills': 'делегирование, пользоваться календарем, обсуждать важные вопросы'}, {'pk': 4, 'name': 'Bauer Adkins', 'picture': 'https://picsum.photos/200', 'position': 'CTO', 'gender': 'male', 'age': 37, 'skills': 'very important face'}, {'pk': 5, 'name': 'Day Holloway', 'picture': 'https://picsum.photos/200', 'position': 'HR manager', 'gender': 'male', 'age': 35, 'skills': 'LinkedIn, telegram, spam, spam, spam'}, {'pk': 6, 'name': 'Austin Cochran', 'picture': 'https://picsum.photos/200', 'position': 'python-develop', 'gender': 'male', 'age': 26, 'skills': 'python, html'}, {'pk': 7, 'name': 'Sheree Love', 'picture': 'https://picsum.photos/200', 'position': 'Django developer', 'gender': 'female', 'age': 33, 'skills': 'Python, Django, flask'}]
# print(get_all(candidates))

def get_by_pk(pk):
    """которая вернет кандидата по pk"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["pk"] == int(pk):
            return candidate

#print(get_by_pk("2"))

def get_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    candidates_list = []
    candidates = load_candidates()
    for candidate in candidates:
        list_of_skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in list_of_skills:
             candidates_list.append(candidate)
    return candidates_list

#print(get_by_skill("LinkedIn"))

def wrote_name_pos_skills_for_all(candidates):
    string_for_print = "<pre>\n"
    for candidate in candidates:
        string_for_print += f"Имя кандидата - {candidate['name']}\nПозиция кандидата {candidate['position']}\nНавыки {candidate['skills']}"
        string_for_print += f"\n\n"
    string_for_print += "<pre>"
    return string_for_print

# print(load_name_pos_skills())

def wrote_img_name_pos_skills_by_pk(pk):
    candidate = get_by_pk(pk)
    string_for_print = f"<img src={candidate['picture']}>"
    string_for_print += "<pre>\n"
    string_for_print += f"Имя кандидата - {candidate['name']}\nПозиция кандидата {candidate['position']}\nНавыки {candidate['skills']}"
    string_for_print += f"\n<pre>"
    return string_for_print

#print(wrote_img_name_pos_skills_by_pk("2"))
# candidates = get_by_skill("python")
# print(wrote_name_pos_skills_for_all(candidates))
