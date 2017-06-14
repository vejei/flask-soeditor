# Flask-SOEditor
A Stack Overflow editor extension for Flask.
## Installation
`pip install Flask-SOEditor`
## Usage
### Initialization
The first step is to initialize the extension:
```Python
from flask import Flask, render_template
from flask_soeditor import SOEditor

app = Flask(__name__)

soeditor = SOEditor(app)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
```
Alternatively, you could use the `init_app()` method, like this:
```Python
from flask import Flask, render_template
from flask_soeditor import SOEditor

soeditor = SOEditor()

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)
  
  soeditor.init_app(app)
  ...
```

### Add editor in template
First, you have to load the css and js files, and then replace your textarea:
```Html
<!DOCTYPE html>
<html>
<head>
	<title>Flask-SOEditor example</title>
	<script type="text/javascript" src="{{ url_for('static', filename='jquery-3.1.1.js') }}">
	{{ soeditor.css }}
	{{ soeditor.js }}
</head>
<body>
<textarea id="mdeditor"></textarea>
<script type="text/javascript">
	var soeditor = new SOEditor("textarea#mdeditor");
</script>
</body>
</html>
```
