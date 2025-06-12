from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'very_secret_key'  # Use env variable in production

# Fake user for demo
users = {'admin': 'password'}

# Fake post
post = {
    "id": 1,
    "title": "Welcome to the XSS Demo Blog",
    "content": "Here's a demo of a stored XSS vulnerability. Submit a script in the comments!",
    "comments": []
}

@app.route('/')
def index():
    return redirect('/post/1')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if users.get(username) == password:
            session['username'] = username
            return redirect('/post/1')
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        comment = request.form.get('comment')
        post['comments'].append(comment)  # Still vulnerable to XSS
        return redirect(url_for('show_post', post_id=post_id))

    # Inject a malicious comment every time the post is viewed
    post['comments'].append("""<script>alert('XSS from auto-submitted comment');alert('This is a stored XSS demo!');alert('Welcome back! This message was injected via XSS');</script>""")

    return render_template('post.html', post=post, user=session['username'])


if __name__ == '__main__':
    app.run(debug=True)
