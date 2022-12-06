from flask import Blueprint, request, render_template, flash, redirect
from flask.json import jsonify
from flask_login import current_user

import service
warehouse_api = Blueprint("warehouse_api", __name__)




@warehouse_api.route('/', methods=['POST', 'GET'])
def get_warehouses():
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        warehouses = service.Warehouse.get_ware_houses(current_user.id)
        return render_template('users.html', context=warehouses)


@warehouse_api.route('/delete/<int:id>')
def get_detail(warehouse_id):
    if request.method == 'DELETE':
        return render_template('dashboard.html')
    else:
        warehouse = service.Warehouse.get_ware_houses(current_user.id)
        return render_template('users.html', context=warehouses)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
