from flask import Flask
import markdown
import urllib

app = Flask(__name__)

@app.route('/archives/<post>')
def posts(post):
    # todo make this an environment variable
    link = 'https://raw.githubusercontent.com/duizendstra/jadu-home/master/articles/' + post.split('.')[0] + '.md'
    f = urllib.request.urlopen(link)
    data = f.read().decode()
    
    md = markdown.Markdown(extensions = ['meta'])
    raw_html = md.convert(data)

    title = md.Meta.get('title')[0]
    
    print(md.Meta.get('title'))
    print(md.Meta)

    html = """<!doctype html><html lang="en"><head><meta charset="UTF-8">"""
    html += "<title>" + title + "</title>"
    html += """<link rel="stylesheet" href="/css/modest.css"></head><body>"""
    html += raw_html
    html += """</body></html>"""
    return html
 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
