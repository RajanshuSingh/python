from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

SAVE_DIRECTORY = 'attendance_files'

# Create the directory if it doesn't exist
if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    student_name = request.form['student-name']
    roll_number = request.form['roll-number']
    date = request.form['date']
    class_type = request.form['class-type']
    subject_name = request.form['subject-name']
    attendance_status = request.form['attendance-status']

    full_form = {
        't': 'Theory',
        'p': 'Practical',
        'p': 'Present',
        'a': 'Absent'
    }

    data = {
        'Student Name': [student_name],
        'Roll Number': [roll_number],
        'Date': [date],
        'Class Type': [full_form[class_type[0]]],
        'Subject Name': [subject_name],
        'Attendance Status': [full_form[attendance_status[0]]],
    }

    file_name = f"{subject_name}_attendance.xlsx"
    file_path = os.path.join(SAVE_DIRECTORY, file_name)

    try:
        if os.path.exists(file_path):
            df_existing = pd.read_excel(file_path)
            df_new = pd.DataFrame(data)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_excel(file_path, index=False)
        else:
            df_new = pd.DataFrame(data)
            df_new.to_excel(file_path, index=False)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
