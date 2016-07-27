from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    list_of_projects_and_grades = hackbright.get_grades_by_github(github)
    return render_template("student_info.html", first=first,
                            last=last, github=github,
                            list_of_projects_and_grades=list_of_projects_and_grades)

@app.route("/student-search")
def get_student_form():
    """ Form to get github name from user. """

    return render_template("student_search.html")

@app.route("/new-student")
def get_new_student_form():
    """ Form to get github name from user. """

    return render_template("new_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    # flash("Success! You've added a new student!")
    return redirect("/student?github=" + github)


@app.route("/project/<project_title>")
def get_project_info(project_title):
    """Get information about project from the title"""

    title, description, max_grade = hackbright.get_project_by_title(project_title)

    return render_template("project_info.html", title=title, 
                            description=description, max_grade=max_grade)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
