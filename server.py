from flask import Flask, request, render_template
from search import request_base
import re


app = Flask(__name__)


@app.route(
    "/", methods=["GET"],
)
def search():
    phone_number = request.args.get(
        'phone',
        type=str,
        default=''
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
    if re.search(r'[9]{1}\d{5,}', phone_number):
        phone_number = re.findall(r'[9]{1}\d{5,}', phone_number)[0]
    else:
        phone_number = ''
    print(phone_number)
    match, get_records = request_base(phone=phone_number, name=name)

    return render_template(
        'index.html',
        match=match,
        action=action,
        get_records=get_records
    )


if __name__ == '__main__':
    app.run()