import json
import web
from Models import RegisterModel, LoginModel

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/postlogin', 'PostLogin'

)


app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore("Sessions"), initializer={'user': None})
session_data = session.initializer


render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})
# Classes/Routes


class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        res = web.data()
        data = json.loads(res)
        #print(data)

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data['firstName']


class PostLogin:
    def POST(self):
        res = web.data()
        data = json.loads(res)
        login = LoginModel.LoginModel()
        user = login.check_user(data)
        if user:
            session_data["user"] = user
            return user

        return 'error'


class Logout:
    def DELETE(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return 'success'


if __name__ == "__main__":
    app.run()

