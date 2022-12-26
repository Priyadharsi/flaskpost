from flask import Flask, render_template,request,redirect

app = Flask(__name__)

'''my_post = [{"id":1, "title":"This is the title of the post", "Content":"This is the content of the post", "Author":"Surendar"},{"title":"This is the title of the second post", "Content":"This is the content of the second post", "Author":"Manoj"}]'''
my_post = [{"title":"This is the title 2","content":"this is the content 2","published":True,"id":2,"created_at":"2022-12-15T08:41:44.888493+05:30"},{"title":"This is the title 4","content":"this is the content 4","published":True,"id":4,"created_at":"2022-12-15T08:42:21.689495+05:30"},{"title":"This is the title 5","content":"this is the content 5","published":True,"id":5,"created_at":"2022-12-15T08:42:29.122437+05:30"},{"title":"This is the title 6","content":"this is the content 6","published":True,"id":6,"created_at":"2022-12-15T08:48:46.036579+05:30"},{"title":"This is the title 7","content":"this is the content 7","published":True,"id":7,"created_at":"2022-12-15T08:49:36.170970+05:30"},{"title":"This is the title 8","content":"this is the content 8","published":True,"id":8,"created_at":"2022-12-15T08:54:30.602010+05:30"},{"title":"hi again","content":"hello again","published":True,"id":3,"created_at":"2022-12-15T08:42:15.566597+05:30"},{"title":"This is the title 9","content":"this is the content 9","published":True,"id":9,"created_at":"2022-12-15T22:42:46.765041+05:30"},{"title":"This is the title 11","content":"this is the content 11","published":True,"id":11,"created_at":"2022-12-15T22:45:41.168004+05:30"},{"title":"This is the title 12","content":"this is the content 12","published":True,"id":12,"created_at":"2022-12-15T22:47:57.880590+05:30"},{"title":"This is the title 13","content":"this is the content 13","published":True,"id":13,"created_at":"2022-12-15T22:52:03.893427+05:30"},{"title":"This is the title 14","content":"this is the content 14","published":True,"id":14,"created_at":"2022-12-15T22:53:24.159921+05:30"},{"title":"Nineth post updated","content":"This is the content for Nineth post","published":True,"id":10,"created_at":"2022-12-15T22:45:05.874094+05:30"}]

@app.route("/")
def Hello_world():
     '''test = my_post[0]["Content"]+my_post[1]["Content"]'''
     '''for item in my_post:
          print(item["content"])'''
     output = ''
     for i in range(len(my_post)):
          output +=my_post[i].get("content")
     return render_template('index.html',data=output)

@app.route("/")
def user_info(username):
      return render_template('index.html',data = username)
      
@app.route("/create",methods=["POST","GET"])
def create_post():
     title=request.form["title"]
     content=request.form["content"]
     author=request.form["author"]
     temp={
          "title":title,"content":content,"author":author
     }
     my_post.append(temp)
     return render_template('create_post.html',data=my_post)
 

'''app.route("/<index>")
def get_post(index):
     return render_template('index.html',data=my_post[int(index)])

'''


if __name__ == "__main__":
    app.run(debug=True)
     