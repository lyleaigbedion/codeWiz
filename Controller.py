import json
import web
from Models import RegisterModel, LoginModel
urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/postregistration', 'PostRegistration',
    '/postlogin', 'PostLogin'

)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

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
            return user

        return 'error'


if __name__ == "__main__":
    app.run()