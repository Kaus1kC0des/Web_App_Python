from flask import Flask, render_template, request, redirect, url_for
import pymysql as sql

db = sql.connect(host='localhost',user='root',password='Govind@1950',database='FlaskApp')
app = Flask(__name__)
# posts = {
#     0: {
#         'title': 'Hello, world',
#         'content': 'This is my first blog post!'
#     }
# }
cursor = db.cursor()
cursor.execute('SELECT * FROM posts')
posts = {}
values = cursor.fetchall()
for i in range(len(values)):
    posts[i] = {'title':values[i][1],'content':values[i][2]}



@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM posts WHERE id = %s', (int(post_id)))
    post = {'post_id':cursor.fetchone()[0],'title':cursor.fetchone()[1],'content':cursor.fetchone()[2]}
    if not post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    return render_template('post.jinja2', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        # posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        cursor = db.cursor()
        cursor.execute("INSERT INTO posts (title,content) VALUES (%s,%s)",(title,content))
        db.commit()
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
