from flask import Flask, render_template, request

app = Flask(__name__)

slang_dictionary = {
"cap":"You're lying",
"no cap":"I'm not lying",
"lit":"Really good or exciting",
"bet":"Agreement or confirmation",
"fr":"For real",
"ong":"On God or more accurately I swear on god",
"no shot":"No way or no chance",
"ratio'd":"The ratio of comments to likes on your social media post is unfavourable so your opinion is bad",
"ratiod":"The ratio of comments to likes on your social media post is unfavourable so your opinion is bad",
"fell off":"The person in question is no longer relevant",
"who asked":"Maybe the one literal zoomer slang in existence. Used to invalidate your opinion by implying no one asked for it",
"bussin":"Extremely good or tasty",
"bussin'":"Extremely good or tasty",
"bussing":"Extremely good or tasty",
"drip":"Nice, cool or otherwise trendy clothing",
"boomer":"Derogatory term for literally anyone older than them, even if you're a millenial it matters not",
"slaps":"This is excellent or amazing, usually referring to music but can be used in other contexts too",
"this slaps":"This is excellent or amazing, usually referring to music but can be used in other contexts too",
"say less":"Stop talking, I understand and am on board with what you're saying",
"low key":"Moderate, quiet or restrained enthusiasm for something or someone",
"high key":"Open and earnest enthusiasm for something or someone",
"rizz":"Charm or the ability to effortlessly flirt with others. Short for charisma.",
"yeet":"To throw something with force",
"goat":"Greatest of all time",
"yolo":"You only live once",
"g.o.a.t":"Greatest of all time"
}

def translate_zoomer(slang):
  slang = slang.lower()
  if slang in slang_dictionary:
    return slang_dictionary[slang]
  else:
    return "Slang not found"

@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ''
    if request.method == 'POST':
        slang = request.form.get('slang')
        translation = translate_zoomer(slang)
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=19080, debug=False)
