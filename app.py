from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story as story_1



app = Flask(__name__)
STORIES = [story_1]

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def get_home():
  # prompts = [{"type": st } for st in story.prompts ]
  story_options = [i for i in range(1, len(STORIES)+1)]
  return render_template('home_select.html', story_options=story_options)

@app.route("/story_prompt")
def render_story_prompt():
  """Generate form content dynamically for a given story"""
  # get storyIndex, options are 1-indexed but STORIES is 0 indexed
  story_index = int(request.args["story_option"]) - 1
  story = STORIES[story_index]
  prompts = [{"type": st } for st in story.prompts ]
  return render_template('story_form.html', prompts=prompts, story_option=(request.args["story_option"]))


@app.route("/story", methods=["GET"])
def get_story():
  # get storyIndex, options are 1-indexed but STORIES is 0 indexed
  story_index = int(request.args["story_option"]) - 1

  story = STORIES[story_index].generate(request.args)
  return render_template('finished_story.html', story=story)

