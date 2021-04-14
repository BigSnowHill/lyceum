from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!»</h1>
                    <img src="{url_for('static', filename='img/MARS.jpg')}" 
                        alt="здесь должна была быть картинка, но не нашлась"><br>
                    Вот она какая, красная планета.
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                        rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1 class=index_1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.jpg')}" 
                            alt="здесь должна была быть картинка, но не нашлась"><br>
                        <div class="alert alert-primary" role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-danger" role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-warning" role="alert">
                            Присоединяйся!
                        </div>

                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <div class="container login_form" id="form">
                                    <form class="login_form" method="post">
                                        <h1>Анкета претендента</h1>
                                        <h1>на участие в миссии</h1>
                                        <div class="form-group">
                                            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        </div>
                                        <br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email"><br>
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование</label>
                                            <select class="form-control" id="classSelect" name="education">
                                              <option>начальное общее образование</option>
                                              <option>основное общее образование</option>
                                              <option>среднее общее образование</option>
                                              <option>среднее профессиональное образование</option>
                                              <option>высшее образование - бакалавриат</option>
                                              <option>высшее образование - специалитет, магистратура</option>
                                              <option>высшее образование - подготовка кадров высшей квалификации</option>
                                            </select>
                                         </div><br>
                                        <div class="form-group">
                                            <label for="about">Какие у вас есть профессии?</label><br>
                                                <input type="checkbox" name="profession" value="инженер-исследователь">инженер-исследователь<br>
                                                <input type="checkbox" name="profession" value="пилот">пилот<br>
                                                <input type="checkbox" name="profession" value="строитель">строитель<br>
                                                <input type="checkbox" name="profession" value="экзобиолог">экзобиолог<br>
                                                <input type="checkbox" name="profession" value="врач">врач<br>
                                                <input type="checkbox" name="profession" value="инженер по терраформированию">инженер по терраформированию<br>
                                                <input type="checkbox" name="profession" value="климатолог">климатолог<br>
                                                <input type="checkbox" name="profession" value="специалист по радиационной защите">специалист по радиационной защите<br>
                                                <input type="checkbox" name="profession" value="астрогеолог">астрогеолог<br>
                                                <input type="checkbox" name="profession" value="гляциолог">гляциолог<br>
                                                <input type="checkbox" name="profession" value="инженер жизнеобеспечения">инженер жизнеобеспечения<br>
                                        </div><br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div><br>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотитет принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="motivation"></textarea>
                                        </div><br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div><br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div><br>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['motivation'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
                          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
                            integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
                            crossorigin="anonymous"></script>
                    <title>Planet</title>
                </head>
                <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h2 class="alert alert-primary">Эта планета близка к Земле;</h2>
                    <h3 class="alert alert-success">На ней есть вода и атмосфера;</h3>
                    <h4 class="alert alert-danger">На ней есть небольшое мегнитоное поле;</h4>
                    <h5 class="alert alert-warning">Наконец, она просто красива!</h5>
                </body>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
                          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
                            integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
                            crossorigin="anonymous"></script>
                    <title>Results</title>
                </head>
                <body>
                    <h1>Результаты отбора</h1>
                    <h2 class="alert alert-success">Претендента на участие в миссии {nickname}</h2>
                    <h3>Поздравляем! Ваш рейтинг после {str(level)} этапа отбора</h3>
                    <h1 class="alert alert-primary">составляет {str(rating)}</h1>
                    <h3>Желаем удачи</h3>
                </body>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
                          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
                            integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
                            crossorigin="anonymous"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Results</title>
                </head>
                <body>
                    <div class="container">
                    <form class="login_form" enctype="multipart/form-data" method="post">
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </div><br>
                    </form>
                    </div>
                </body>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', mode='wb') as img:
            img.write(f.read())
        img = url_for('static', filename=f'img/{f.filename}')
        return f'''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
                                  integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
                                    integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
                                    crossorigin="anonymous"></script>
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Results</title>
                        </head>
                        <body>
                            <div class="container">
                            <form class="login_form" enctype="multipart/form-data" method="post">
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                    <img src="{img}"><br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </div><br>
                            </form>
                            </div>
                        </body>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                              integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                                            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Results</title>
                    
                    </head>
                    <body>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active" style="background-color: #000000"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1" style="background-color: #000000"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2" style="background-color: #000000"></li>
                        </ol>
                        <div class="carousel-inner" align="center">
                            <div class="carousel-item active">
                                <img class="center" src="static/img/1.jpg">
                            </div>
                            <div class="carousel-item" align="center">
                                <img class="center" src="static/img/2.jpg">
                            </div>
                            <div class="carousel-item" align="center">
                                <img class="center" src="static/img/3.jpg">
                            </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev" style="background-color: #000000">
                            <span class="carousel-control-prev-icon" aria-hidden="true" ></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next" style="background-color: #000000">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                    </div>
                    
                    </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
