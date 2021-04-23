from flask import Flask, request, render_template,url_for,session,redirect
#some function for manage database
import database
#some function to control email validation
import control
#getting stocks information
import apis



app = Flask(__name__)


@app.route('/')

@app.route('/signin',methods=['POST','GET'])

def signin():
    return render_template('signin.html')


@app.route('/signup')

def signup():
    return render_template('signup.html')


email = ''
password = ''
stocks_names = ['tesla','apple','microsoft','amazon','nio','nvidia','moderna','nikola','facebook','amd']
#her bir hissenin ücretini tekrar tekrar hesaplamamak için oluşturulan global price değişkeni.
price = 0

@app.route('/home',methods=['POST','GET'])
def home():
    global email
    global password
    global stocks_names
    email = request.form['email']
    password = request.form['password']
    if database.find_user(email,password) and request.method == 'POST':
        name = ""
        for i in email:
            if i=="@":
                break
            name += i
        budget = database.learn_budget(email)
        stock_list = database.learn_stocks_and_piece(email)
        return render_template('home.html',stocks_names = stocks_names,name=name,budget=budget,stock_list=stock_list)

    elif not email or not password:
        return "<h2>Email veya şifrenizi girmediniz<h2>"

    else:
        return "<h2>Böyle bir kullanıcı yok.</h2>"

@app.route('/home/<name>',methods=['POST','GET'])
def stock_page(name):
    global email
    global password
    global stocks_names
    global price
    if database.find_user(email,password) and name in stocks_names:
        stock_list = database.learn_stocks_and_piece(email)
        #performans için teker teker isimler yazıldı.
        if name=='tesla':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            tesla = apis.info('TSLA')
            price = tesla[2]
            return render_template('stock.html',stock = tesla,name=name, piece=piece)

        elif name=='apple':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            apple = apis.info('AAPL')
            price = apple[2]
            return render_template('stock.html',stock = apple,name=name, piece=piece)

        elif name=='microsoft':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            microsoft = apis.info('MSFT')
            price = microsoft[2]
            return render_template('stock.html',stock = microsoft,name=name, piece=piece)

        elif name=='amazon':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            amazon = apis.info('AMZN')
            price = amazon[2]
            return render_template('stock.html',stock = amazon,name=name, piece=piece)

        elif name=='nio':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            nio = apis.info('NIO')
            price = nio[2]
            return render_template('stock.html',stock = nio,name=name, piece=piece)

        elif name=='nvidia':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            nvidia = apis.info('NVDA')
            price = nvidia[2]
            return render_template('stock.html',stock = nvidia,name=name, piece=piece)

        elif name=='moderna':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            moderna = apis.info('MRNA')
            price = moderna[2]
            return render_template('stock.html',stock = moderna,name=name, piece=piece)

        elif name=='nikola':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            nikola = apis.info('NKLA')
            price = nikola[2]
            return render_template('stock.html',stock = nikola,name=name, piece=piece)

        elif name=='facebook':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            facebook = apis.info('FB')
            price = facebook[2]
            return render_template('stock.html',stock = facebook,name=name, piece=piece)

        elif name=='amd':
            piece=0
            for i in stock_list:
                if i[0]==name:
                    piece = i[1]
            amd = apis.info('AMD')
            price = amd[2]
            return render_template('stock.html',stock = amd,name=name, piece=piece)
        
    elif name=='buy':
        return redirect(url_for('buy'))
    elif name=='sell':
        return redirect(url_for('sell'))
    else:
        return '404'





@app.route('/home/buy',methods=['POST','GET'])
def buy():
    global email
    global password
    global price
    if request.method == 'POST' and database.find_user(email,password):
        stock_name_to_buy = request.form['stock_name_to_buy']
        piece_to_buy = request.form['piece_to_buy']
        
        if stock_name_to_buy and int(piece_to_buy)>0 and price>0:
            database.add_stock(email,stock_name_to_buy,int(piece_to_buy),price)
            return 'satın alma işleminiz başarıyla tamamlandı.'
        else:
            return 'yanlış ya da eksik bilgi girildi. price :{}'.format(price)
    return 'Maalesef bir hata oluştu.Çıkış yapıp tekrar giriş yapmayı deneyin.'





@app.route('/home/sell',methods=['POST','GET'])
def sell():
    global email
    global password
    global price
    if request.method == 'POST' and database.find_user(email,password):
        stock_name_to_sell = request.form['stock_name_to_sell']
        piece_to_sell = request.form['piece_to_sell']
        
        if stock_name_to_sell and int(piece_to_sell)>0 and price>0:
            database.remove_stock(email,stock_name_to_sell,int(piece_to_sell),price)
            return 'Hisse satma işleminiz başarıyla tamamlandı.'
        else:
            return 'yanlış ya da eksik bilgi girildi. price :{}'.format(price)
    return 'Maalesef bir hata oluştu.Çıkış yapıp tekrar giriş yapmayı deneyin.'


@app.route('/succes',methods=['POST','GET'])
#controlling for succesfully sign up 
def succes():

    email = request.form['Eemail']
    password = request.form['Epassword']

    if control.control(email,password) and not database.find_user(email,password) and database.is_valid_mail(email):
        database.add_user(email,password)
        return render_template('succes.html')
    elif (database.find_user(email,password)):
        return "<h2>Zaten bir hesabınız var.</h2>"
    elif not database.is_valid_mail(email):
        return "<h2> Bu mail adresini alamazsınız<h2>"
    else:
        return "<h2>Geçersiz mail veya yeterli uzunlukta olmayan şifre</h2>"



if __name__=="__main__":
    app.run(debug=True)