# flask --app app run
#
from flask import Flask, render_template, request

app = Flask(__name__)

name=''
@app.route('/params')
def hello():
    args = request.args
    print(request.__dict__)
    print(args)
    params = [{"key": k, "value": v} for k, v in args.items()]
    print(params)
    name=args['name']
    return render_template('params_ola.html', params=params,template_name=name)
