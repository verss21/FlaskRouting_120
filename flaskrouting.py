from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/index',methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
   
@app.route('/')
def m():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)

   user = request.form['nm']
