from bottle import route, static_file,post,get,request,redirect,response, default_app

@route('/upload')
def query_file_to_upload():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

"""
@post('/upload')
def do_upload():
    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = get_save_path_for_category(category)
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'
"""
@route('/hi')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@post('/hi')
def cookie_demo():
    name = request.forms.get('name')
    forget_me =  request.forms.get('forget_me')
    if forget_me == "detete":
        response.set_cookie("name", "")
        return "OK, you'd never been here"
    if request.get_cookie("name") == name:
        return "Welcome back! Nice to see you again " + name
    else:
        response.set_cookie("name", name)
        return "Hello there! Nice to meet you " + name



@route('/wrong/url')
def wrong():
    redirect("http://www.google.com")

@route('/get_file/<path:path>')
def send_file(path = None):
    if path is not None:
        return static_file(path, "...",'auto', False, 'UTF-8')

@route('/any_path/<filepath:path>')
def send_file_(filepath):
    if filepath is not None:
        return static_file(filepath)
    else:
        return "no file name..."
        

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

def check_login(username, password):
    return True

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.<br>Greetings to you dear %s</p>" % username
    else:
        return "<p>Login failed.</p>"


@post('/person')
def hello_personalize():
    person = request.forms.get('person')
    if person == "":
        person = "stranger"
    return "Hello " + person

def bottels(nBottles):
    """
    99 bottles of beer on the wall, 99 bottles of beer.
    Take one down and pass it around, 98 bottles of beer on the wall.
    """
    lines = []
    if nBottles <= 0:
        return lines
    
    for i in range(nBottles - 1):
        num_str =  str(nBottles - i)
        print num_str
        lines.append(num_str + " bottles of beer on the wall, " + num_str +" bottles of beer")
        num_str =  str(nBottles - i - 1)
        lines.append("Take one down and pass it around, "+ num_str +"  bottles of beer on the wall" )  
        lines.append("" )   
        
    lines.append("1 bottle of beer on the wall, 1 bottle of beer." )
    lines.append("Take one down and pass it around, no more bottles of beer on the wall." )
    lines.append("" )
    lines.append("No more bottles of beer on the wall, no more bottles of beer. " )
    lines.append("Go to the store and buy some more, %d bottles of beer on the wall." % nBottles )

    return lines

@post('/bottles')
def bottles_on_the_wall():
    bottles=request.forms.get('bottles')
    if bottles == "" or not bottles.isalnum():
        return "Wrong input"
    bottles_song = ""
    bottle_lines = bottels( int(bottles))
    for i in bottle_lines:
        bottles_song +=  i + "<br>\n"
    
    return bottles_song
    
@post('/palindrome')
def is_it_a_palindrome():
    tested_palindrome=request.forms.get('tested_palindrome')
    if tested_palindrome == "":
        return "Wrong input"
    answer = tested_palindrome + " is "
    if tested_palindrome == tested_palindrome[::-1]:
        answer += "a palindrome"
    else:
        answer += "not a palindrome"
    return answer

def get_next_word(text):
    word = ""
    b_inside_word = text[0].isalpha()
    for next_letter_index  in range(len(text)):
        if text[next_letter_index].isalpha():
            b_inside_word = True
            word += text[next_letter_index]
        else:
            if b_inside_word:
                b_inside_word = False
                return word, next_letter_index,b_inside_word
            
                
    return word, next_letter_index,b_inside_word     

def pal_words_list_get(text):
    pal_words_list = []
    letter_index = 0;
    while letter_index < len(text):
        word, next_space_index, b_inside_word =  get_next_word(text[letter_index:])
        
        if word is not "" :
            if word == word[::-1]:
                pal_words_list.append(word)
            letter_index += next_space_index
            if b_inside_word:
                return pal_words_list
        else:
            return pal_words_list
        
def words_list_get(text):
    words_list = []
    letter_index = 0;
    while letter_index < len(text):
        word, next_space_index,b_inside_word =  get_next_word(text[letter_index:])
        if word != "":
            words_list.append(word)
            letter_index += next_space_index
            if b_inside_word:
                return words_list
        else:
            return words_list
    

def text_list_to_html_list(lines_list, b_ordered):
    tag_string = "ul"    
    if b_ordered:
        tag_string = "ol"
    html_output = "<"+ tag_string + ">"
    for line in lines_list:
        html_output += ("<li>"+ line + "</li>\n")
    html_output += "</"+ tag_string + ">\n"    
    
    return html_output


def text_to_html_list(text, b_ordered):
    lines_list = text.splitlines()
    tag_string = "ul"    
    if b_ordered:
        tag_string = "ol"
    html_output = "<"+ tag_string + ">"
    for line in lines_list:
        html_output += ("<li>"+ line + "</li>\n")
    html_output += "</"+ tag_string + ">\n"    
    
    return html_output
    
@post('/palindromes')
def extract_palindrome_words_only():
    tested_text=request.forms.get('tested_text')
    
    if tested_text == "":
        return "Wrong input"
    pal_words_list = pal_words_list_get(tested_text)
    #pal_words_list = ["ddd", "sss"]
    answer = "Palindrome words only are:\n" + text_list_to_html_list(pal_words_list, True)

    return answer

def matrix_to_html(matrix):
    output_string = '<table border="1">\n'
    
    for row in range(len(matrix)):
        output_string += "<tr>\n"
        for col in range(len(matrix[row])):
            output_string += "<td>" + str(matrix[row][col]) + "</td>"
        output_string += "</tr>\n"
        
    output_string += "</table>"
    return output_string

  
    
@post('/multiplication')
def  multiplication_matrix ():
    size=request.forms.get('size')
    if size is None:
        return "No input"
    if not size.isalnum():
        return "Wrong input"
                       
    matrix = [[ c * row for c in range(int(size))] for row in range(int(size))]

    answer = "<h1>Multiplication matrix size " + size + "</h1>\n"
    answer += matrix_to_html(matrix)
    return answer



def common_word_is(text):
    """
A function that given a text returns find the word which occurs most often in it    
    """
    words_list = words_list_get(text)
    count_max = 0
    abundant_word = ''
    for word in words_list:
        occurances = words_list.count(word)
        if count_max < occurances:
            count_max = occurances
            abundant_word = word
            
       
    return(abundant_word)

@post("/most_common_word")
def most_common_word(tested_text=None):
    tested_text =request.forms.get('tested_text')
    return "Most common word is " + common_word_is(tested_text)


import cgi

def text_matrix_to_html(matrix):
    output_string = '<table border="1">\n'
    
    for row in range(len(matrix)):
        output_string += "<tr>\n"
        for col in range(len(matrix[row])):
            output_string += "<td>" + cgi.escape(matrix[row][col]) + "</td>"
        output_string += "</tr>\n"
        
    output_string += "</table>\n"
    return output_string

@post("/python-basics-selection")
def answer_selection():
    selection = request.forms.get('selection')    
    if selection is "":
        return "??"
    

    if selection == "Hello world":
        return "Hello World!"
    
    
    if selection == "Hello You":
        return """
        <form action="/person" method="post">
            What is your name?: <input type="text" name="person">
            <input value="submit" type="submit" />
        </form>
       """
    
    if selection == "N bottles of beer on the wall":
        return  """
        <form action="/bottles" method="post">
            How Many bottles on the wall? <input type="text" name="bottles">
            <input value="Let's sing" type="submit" />
        </form>
       """
    if selection == "Palindrome"                   :
        return  """
        <form action="/palindrome" method="post">
            Type your palindrome <input type="text" name="tested_palindrome">
            <input value ="Is it?" type="submit" />
        </form>
       """
    
    if selection == "Multiplication List"          :
        return  """
        <form action="/multiplication" method="post">
            Multiplication table size? <input type="text" name="size">
            <input value ="Generate" type="submit" />
        </form>
        """
    if selection == "Palindromes"                  :
        return  """
        <form action="/palindromes" method="post">
            Type your palindrome text <input type="text" name="tested_text">
            <input value ="reveal which words are palindromes?" type="submit" />
        </form>
       """
        
    if selection == "Most common word"             :
        return  """
        <form action="/most_common_word" method="post">
            Type your text <input type="text" name="tested_text">
            <input value ="What is the most common word?" type="submit" />
        </form>
       """
    if selection == "html list"                    :
        text = """This is an example of A multiline text.
        next line
        and the next one
        and the next next line"""
        answer = "example of an ordered list:\n"
        answer +=  text_to_html_list( text, True)
        answer += "And a non-ordered list:\n"
        answer +=  text_to_html_list( text, False)
        return answer
    if selection == "html table"                   :
        matrix = [ ['<table border="1">',"<td>1</td><td>2"] ,  ["""
            <tr>
            <td>3</td>
            ""","eeeee"] ,  ["1111","2222"]]
        return "An example of an HTML table:\n" + text_matrix_to_html(matrix)
    return selection + "is not supported"    
    
@route('/hello')
def hello():
    return "Hello World!"

@route('/get_file')
def get_file():
    return  """
        <form action="/get_file" method="post">
            Which file to download? <input type="text" name="path">
            <input value ="Download file" type="submit" />
        </form>
       """

@route('/project')
def project_main():
    return """
    <h1>Public fulfilment.</h1>""" + 5 * "<br>" + """
        <a href="https://www.facebook.com/download/648693671818448/Public%20Fulfilment_05.pptx">Download Presentation</a><br>
        <a href="https://docs.google.com/document/d/1aFoAC2c2xtnKCS5WhoenFWXHgsC_LOjtnywxWmjcmKA/edit?usp=sharing">User Centered Design</a><br>        
        <a href="https://www.facebook.com/download/230636090446192/13_11_20_spec.jpeg">Download Spec</a><br>
        <a href="https://www.facebook.com/groups/NeuroNetProject/">Team Facebook collaboration group</a><br>        """
        
@route('/')
@route('/hakita')
def hakita_main():
        return """
    <h1>Welcome to Tzahi Manistersky's HAKITA homepage.</h1>
        You can click on the followind links:<br>
        <a href="/python-basics">python-basics selected solutions</a><br>
        <a href="/project">Project</a>
        """
@route('/python-basics')            
def python_basics():
    return """
        <form action="/python-basics-selection" method="post">
        <select name='selection'>
            <option value="Hello world"                   >Hello world</option>
            <option value="Hello You"                     >Hello You</option>
            <option value="N bottles of beer on the wall" >N bottles of beer on the wall</option>
            <option value="Palindrome"                    >Palindrome</option>
            <option value="Multiplication List"           >Multiplication List</option>
            <option value="Palindromes"                   >Palindromes</option>
            <option value="Most common word"              >Most common word</option>
            <option value="html list"                     >html list</option>
            <option value="html table"                    >html table            </option>
        </select>
        <input type="submit" value="Submit">
     </form>"""





application = default_app()
