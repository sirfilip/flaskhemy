from flask import Flask, render_template, url_for, request, redirect

from models import PostRepo
from forms import PostForm

post_repo = PostRepo()


app = Flask(__name__)



@app.route('/')
def list_posts():
    return render_template('posts/home.html', posts=post_repo.all())

@app.route('/posts/create', methods=['POST', 'GET'])
def create_post():
    form = PostForm(request.form)

    if request.method == 'POST' and form.validate():
        post = post_repo.create(title=form.title.data, body=form.body.data)
        return redirect(url_for('show_post', post_id=post.id))
        
    return render_template('posts/new.html', form=form)

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = post_repo.find(post_id)
    return render_template('posts/show.html', post=post)

@app.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = post_repo.find(post_id)
    form = PostForm(request.form, post)
    if request.method == 'POST' and form.validate():
        form.populate_obj(post)
        post_repo.update(post)
        return redirect(url_for('show_post', post_id=post.id))
    return render_template('posts/edit.html', form=form, post=post)

@app.route('/posts/delete/<int:post_id>')
def delete_post(post_id):
    post = post_repo.find(post_id)
    post_repo.delete(post)
    return redirect(url_for('list_posts'))


if __name__ == '__main__':
    app.run(debug=True)
