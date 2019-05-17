from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

posts_data = [
  {
    'id': '111',
    'title': '關於蝦皮 1元奪寶戰',
    'content': '111內容',
    'category': '網路購物',
    'creattime': datetime.strptime('2019-05-01', '%Y-%m-%d')
  }, {
    'id': '222',
    'title': '關於蝦皮 1元奪寶戰',
    'content': '222內容',
    'category': '網路購物',
    'creattime': datetime.strptime('2019-05-02', '%Y-%m-%d')
  }, {
    'id': '333',
    'title': '關於蝦皮 1元奪寶戰',
    'content': '333內容',
    'category': '網路購物',
    'creattime': datetime.strptime('2019-05-03', '%Y-%m-%d')
  }, {
    'id': '444',
    'title': '關於蝦皮 1元奪寶戰',
    'content': '444內容',
    'category': '網路購物',
    'creattime': datetime.strptime('2019-05-04', '%Y-%m-%d')
  }, {
    'id': '555',
    'title': '關於蝦皮 1元奪寶戰',
    'content': '555內容',
    'category': '網路購物',
    'creattime': datetime.strptime('2019-05-05', '%Y-%m-%d')
  }, {
    'id': '666',
    'title': '關於蝦皮 1元奪寶戰',
    'content': '666內容',
    'category': '網路購物',
    'creattime': datetime.strptime('2019-05-06', '%Y-%m-%d')
  },
]

@app.route('/')
def index():
  return render_template('index.html', posts=posts_data)

@app.route('/posts/<id>')
def posts(id):
  return render_template('posts.html', id=id)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

if __name__ == '__main__':
  app.run(debug=True)