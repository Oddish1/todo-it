from flask import Flask
from flask import render_template
import os


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
  )

  if test_config is None:
    # load the instance config
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config
    app.config.from_mapping(test_config)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  """@app.route('/')
  def index():
    return render_template('index.html')


  @app.route('/tasks')
  def tasks():
    return render_template('tasks.html', tasks=tasks)


  @app.route('/tasks/<int:task_id>')
  def show_task():
    task_id = task_id
    return render_template('edit-task.html', task_id=task_id)


  @app.route('/habits')
  def habits():
    return render_template('habits.html', habits=habits)


  @app.route('/habits/<int:habit_id>')
  def show_habit():
    habit_id = habit_id
    return render_template('edit-habit.html', habit_id=habit_id)


  @app.route('/stats')
  def stats():
    return render_template('stats.html')"""

  @app.route('/')
  def index():
    return 'Hello, World!'

  return app