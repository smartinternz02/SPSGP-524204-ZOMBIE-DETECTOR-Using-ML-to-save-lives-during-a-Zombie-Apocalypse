from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open(r'C:/Users/Kapil/Desktop/Zombie Flask/model.pkl', 'rb'))
SS = pickle.load(open(r'C:/Users/Kapil/Desktop/Zombie Flask/scaler.pkl', 'rb'))

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    a = request.form["age"]
    r = request.form["rurality"]
    f = request.form["food"]
    m = request.form["medicine"]
    s = request.form["sanitation"]
    w = request.form["water"]

    r1, r2, r3 = 0, 0, 0  # Assign default values

    if r == "Urban":
        r1, r2, r3 = 0, 0, 1
    elif r == "Sub-Urban":
        r1, r2, r3 = 0, 1, 0
    elif r == "Rural":
        r1, r2, r3 = 1, 0, 0

    f1, f2 = 0, 0  # Assign default values

    if f == "Food":
        f1, f2 = 1, 0
    elif f == "No Food":
        f1, f2 = 0, 1

    m1, m2 = 0, 0  # Assign default values

    if m == "Medicine":
        m1, m2 = 1, 0
    elif m == "No Medicine":
        m1, m2 = 0, 1

    s1, s2 = 0, 0  # Assign default values

    if s == "Sanitation":
        s1, s2 = 1, 0
    elif s == "No Sanitation":
        s1, s2 = 0, 1

    t = [[int(a), int(w), int(r1), int(r2), int(r3), int(f1), int(f2), int(m1), int(m2), int(s1), int(s2)]]
    scaled_input_data = SS.transform(t)
    output = model.predict(scaled_input_data)

    if output == 1:
        res = "Stay away, this person tends to become a Zombie"
    else:
        res = "Fear Not, this person stays Human"

    return render_template("index.html", y= res)

if __name__ == '__main__':
    app.run(debug=True)
