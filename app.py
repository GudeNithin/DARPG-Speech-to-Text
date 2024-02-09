# from flask import Flask, request, render_template
# from werkzeug.utils import secure_filename
# import os
# import subprocess

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'mp3'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Global variable to store the filename
# uploaded_filename = ""

# def allowed_file(filename):
#   return '.' in filename and filename.rsplit(
#       '.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#   return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#   global uploaded_filename

#   if 'file' not in request.files:
#     return 'No file part'

#   file = request.files['file']

#   if file.filename == '':
#     return 'No selected file'

#   if file and allowed_file(file.filename):
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(file_path)
#     uploaded_filename = filename
#     print(filename)    # Set the global variable to store the filename
#     return f'File {filename} uploaded successfully'
#   else:
#     return 'File not allowed or invalid file type'

# @app.route('/translate', methods=['POST'])
# def translate_file():
#   global uploaded_filename
#   print(uploaded_filename)

#   if uploaded_filename:
#     # Get the path of the uploaded file
#     uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'],
#                                       uploaded_filename)

#     # Execute translation.py using subprocess with the uploaded file path as an argument
#     subprocess.run(['python', 'uploads/translation.py', uploaded_file_path])

#     return 'Translation process initiated...'
#   else:
#     return 'No file uploaded'

# if __name__ == '__main__':
#   app.run(debug=True, host='0.0.0.0')
# from flask import Flask, request, render_template
# from werkzeug.utils import secure_filename
# import os
# import subprocess

# app = Flask(_name_)

# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'mp3'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Global variable to store the filename
# uploaded_filename = ""

# def allowed_file(filename):
#   return '.' in filename and filename.rsplit(
#       '.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#   return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#   global uploaded_filename

#   if 'file' not in request.files:
#     return 'No file part'

#   file = request.files['file']

#   if file.filename == '':
#     return 'No selected file'

#   if file and allowed_file(file.filename):
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(file_path)
#     uploaded_filename = filename  # Set the global variable to store the filename
#     return f'File {filename} uploaded successfully'
#   else:
#     return 'File not allowed or invalid file type'

# @app.route('/translate', methods=['POST'])
# def translate_file():
#   global uploaded_filename

#   if uploaded_filename:
#     # Get the path of the uploaded file
#     uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'],
#                                       uploaded_filename)

#     # Execute translation.py using subprocess with the uploaded file path as an argument
#     subprocess.run(['python', 'uploads/translation.py', uploaded_file_path])

#     return 'Translation process initiated...'
#   else:
#     return 'No file uploaded'

# if _name_ == '_main_':
#   app.run(debug=True, host='0.0.0.0')
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Global variable to store the filename
uploaded_filename = ""
translated_text = ""  # Variable to store translated text


def allowed_file(filename):
  return '.' in filename and filename.rsplit(
      '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
  return render_template('index.html', translated_text=translated_text)


@app.route('/upload', methods=['POST'])
def upload_file():
  global uploaded_filename

  if 'file' not in request.files:
    return 'No file part'

  file = request.files['file']

  if file.filename == '':
    return 'No selected file'

  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    uploaded_filename = filename  # Set the global variable to store the filename

    # Clear previous translated text
    global translated_text
    translated_text = ""

    return f'File {filename} uploaded successfully!! Please go back to the home page to translate the file'
  else:
    return 'File not allowed or invalid file type'


@app.route('/translate', methods=['POST'])
def translate_file():
  global uploaded_filename
  global translated_text

  if uploaded_filename:
    # Get the path of the uploaded file
    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                      uploaded_filename)

    # Execute translation.py using subprocess with the uploaded file path as an argument
    subprocess.run(['python', 'uploads/translation.py', uploaded_file_path])

    # Read translated text from a file (translation.py should write the translated text to a file)
    with open('translated_text.txt', 'r') as f:
      translated_text = f.read()

    return render_template('translation.html', translated_text=translated_text)
  else:
    return 'No file uploaded'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
