from flask import Flask,request, render_template

import numpy

import joblib
filename='model_joblib_mental_health'
model=joblib.load(open(filename,'rb'))

app = Flask(__name__,template_folder='template')


# @app.route('/')
# def pred():
#     return render_template('index.html')
@app.route('/')
def home():

    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # name=str(request.form['Name'])
        Age = int(request.form['Age'])
        Gender = int(request.form['Gender'])
        self_employed = int(request.form['self_employed'])
        family_history = int(request.form['family_history'])
        work_interfere = int(request.form['no_employees'])
        no_employees = int(request.form['no_employees'])
        remote_work = int(request.form['remote_work'])
        tech_company = int(request.form['tech_company'])
        benefits = int(request.form['benefits'])
        care_options = int(request.form['care_options'])
        wellness_program = int(request.form['wellness_program'])
        seek_help = int(request.form['seek_help'])
        anonymity = int(request.form['anonymity'])
        leave = int(request.form['leave'])
        mental_health_consequence = int(request.form['mental_health_consequence'])
        phys_health_consequence = int(request.form['phys_health_consequence'])
        coworkers = int(request.form['coworkers'])
        supervisor = int(request.form['supervisor'])
        mental_health_interview = int(request.form['mental_health_interview'])
        phys_health_interview = int(request.form['phys_health_interview'])
        mental_vs_physical = int(request.form['mental_vs_physical'])
        obs_consequence = int(request.form['obs_consequence'])
        age_range=1
        if 0 < Age > 20 :
            age_range=0
        elif 21 < Age > 30:
            age_range = 1
        else:
            age_range=2


        data = numpy.array([[Age, Gender, self_employed, family_history, work_interfere, no_employees,
                             remote_work, tech_company, benefits,
                             care_options, wellness_program, seek_help,
                             anonymity, leave, mental_health_consequence,
                             phys_health_consequence, coworkers,
                             supervisor, mental_health_interview,
                             phys_health_interview, mental_vs_physical,
                             obs_consequence,age_range

            ]])
        res = model.predict(data)

        return render_template('result.html', prediction=res)
        #return res


if __name__ == '__main__':
    app.run(debug=True)