import os

from flask import Blueprint, Markup, url_for


class SOEditor:

    def __init__(self, app=None):
        """Flask-SOEditor extension"""
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """create and register a blueprint with the Flask application.
        
        :param app: 
            An application instance
        """
        soeditor = Blueprint('soeditor', __name__,
                             static_folder='static',
                             static_url_path='/soeditor/static')
        app.register_blueprint(soeditor)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['soeditor'] = self
        app.context_processor(lambda: {'soeditor': self})

    @property
    def css(self):
        """use to load the css file"""
        return Markup('''
        <link rel="stylesheet" href="%s">
        <link rel="stylesheet" href="%s">
        ''' % (url_for('soeditor.static', filename='css/soeditor.css'),
               url_for('soeditor.static', filename='css/markdown.css')))

    @property
    def js(self):
        """use to load the js file"""
        return Markup('''
        <script type="text/javascript" src="%s"></script>
        <script type="text/javascript" src="%s"></script>
        <script type="text/javascript" src="%s"></script>
        <script type="text/javascript" src="%s"></script>
        ''' % (url_for('soeditor.static', filename='js/Markdown.Converter.js'),
               url_for('soeditor.static', filename='js/Markdown.Sanitizer.js'),
               url_for('soeditor.static', filename='js/Markdown.Editor.js'),
               url_for('soeditor.static', filename='js/soeditor.js')))
