from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for
)
from werkzeug.exceptions import abort

from todo_it.auth import login_required
from todo_it.db import get_db

bp = Blueprint('tasks', __name__)

@bp.route('/')
@login_required
def index():
    user_id = g.user['user_id']
    error = None
    if not user_id:
        error = 'User is not logged in!'
    if error is not None:
        flash(error)
    else:
        tasks = get_db().execute(
            'SELECT * FROM tasks JOIN users ON tasks.owner_id = users.user_id'
            ' ORDER BY tasks.due_date DESC'
        ).fetchall()
        tasks = [x for x in tasks if x['user_id'] == user_id]
    return render_template('tasks/index.html', tasks=tasks)


@bp.route('/new', methods=('GET', 'POST'))
@login_required
def new():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        task_priority = request.form['task_priority']
        due_date = request.form['due_date']
        error = None

        if not task_name:
            error = 'Your task needs a name!'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO tasks (task_name, task_description, task_priority, due_date, owner_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (task_name, task_description, task_priority, due_date, g.user['user_id'])
            )
            db.commit()
            return redirect(url_for('tasks.index'))
    return render_template('tasks/new.html')


def get_task(task_id, check_owner=True):
    task = get_db().execute(
        'SELECT t.task_id, owner_id, created, due_date, task_name, task_description, task_priority, task_complete'
        ' FROM tasks t JOIN users u ON t.owner_id=u.user_id'
        ' WHERE t.task_id = ?',
        (task_id,)
    ).fetchone()

    if task is None:
        abort(404, f'Task id {task_id} doesn\'t exist.')
    if check_owner and task['owner_id'] != g.user['user_id']:
        abort(403)
    
    return task

@bp.route('/<int:task_id>/update', methods=('GET', 'POST'))
@login_required
def update(task_id):
    task = get_task(task_id)

    if request.method == 'POST':
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        error = None
        if not task_name:
            error = 'Your task needs a name!'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE tasks SET task_name = ?, task_description = ?'
                ' WHERE task_id = ?',
                (task_name, task_description, task_id)
            )
            db.commit()
            return redirect(url_for('tasks.index'))
    return render_template('tasks/update.html', task=task)

@bp.route('/<int:task_id>/delete', methods=('POST',))
@login_required
def delete(task_id):
    get_task(task_id)
    db = get_db()
    db.execute('DELETE FROM tasks WHERE task_id = ?', (task_id,))
    db.commit()
    return redirect(url_for('tasks.index'))