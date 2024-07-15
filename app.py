from flask import Flask

import utils

app = Flask(__name__)

@app.route("/")
def page_index():
    candidates = utils.load_candidates()
    return utils.wrote_name_pos_skills_for_all(candidates)

@app.route("/candidate/<x>")
def page_candidate(x):
    return utils.wrote_img_name_pos_skills_by_pk(x)


@app.route("/skills/<x>")
def find_by_skill(x):
    candidates = utils.get_by_skill(x)
    return utils.wrote_name_pos_skills_for_all(candidates)

app.run()
