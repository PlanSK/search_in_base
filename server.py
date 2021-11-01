from flask import Flask, request, render_template
from search import request_base


app = Flask(__name__)


@app.route(
    "/", methods=["GET"],
)
def search():
    phone_number = request.args.get(
        'phone',
        type=str,
        default=0
    )
    name = request.args.get(
        'name',
        type=str,
        default=''
    )
    action = request.args.get(
        'action',
        default=False,
        type=bool
    )
    match = request_base(phone=phone_number, name=name)

    return render_template('index.html', match=match, action=action)


if __name__ == '__main__':
    app.run()