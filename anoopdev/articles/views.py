from flask import flash, redirect, render_template,Blueprint, url_for
from flask_login import login_required, current_user

articles_view =  Blueprint('articles',__name__,url_prefix='/articles',template_folder='templates')

@articles_view.route('/')
@login_required
def articles():
    return render_template('articles/articles.html')