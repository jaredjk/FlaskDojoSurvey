from flask import Flask, render_template, request, redirect
                                          
app = Flask(__name__)                     
                                          
@app.route('/')                                                                                 
def whatsyourname():
    
    return render_template('index.html')  

@app.route('/result', methods=['POST'])                                                                                 
def your_name():
    
    name2 = request.form['name1']
    location2 = request.form['location1']
    language2 = request.form['language1']
    comment2 = request.form['comment1']
    return render_template('result.html', name3 = name2,location3 = location2, language3 = language2, comment3 = comment2)    
    return redirect('/')

app.run(debug=True)