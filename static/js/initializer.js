//$.mdb.init()
const registerForm = document.getElementById('register-form')
const loginForm = document.getElementById('login-form')
const logoutBtn = document.getElementById('logout')

async function logout(e){
    try{
        const {data} = await axios.delete("/logout")
        if(data === 'success'){
          window.location.href = '/login'
        }

    }catch(err){
        displayWarning(e)
        console.error(err);
    }

}

function displayWarning(event){
    const warningNode = document.createElement("DIV")
    warningNode.innerText = "Sorry, our server experienced an internal error"
    warningNode.style.color = 'red'
    warningNode.style.fontSize = '24px'
    event.target.appendChild(warningNode)
}

async function registerSubmit(e){

    e.preventDefault()
    console.log(e.target);
    const req = {
     firstName: e.target.firstName.value,
     lastName: e.target.lastName.value,
     email: e.target.formEmail.value,
     password: e.target.formPassword.value,
     newsletter: e.target.newsletter.checked
    }

     try{

         const {data, status} = await axios.post("/postregistration", req)

        if(status >= 200 && status < 300){
          window.location.href = '/login'
        }


     } catch (err) {
        displayWarning(e)
        console.error(err)

     }


}


async function loginSubmit(e){
    console.log(e)
    e.preventDefault()

    const req = {
     email: e.target.LoginFormEmail.value,
     password: e.target.LoginFormPassword.value,
    }

     try{
         const {data, status} = await axios.post("/postlogin", req)
         if(data === 'error'){
            alert("Could not login")
         }else{
            console.log(`Logged in as: ${data}`)
            window.location.href = '/'
         }
     } catch (err) {
        displayWarning(e)
        console.error(err)

     }


}


if(registerForm){
    registerForm.addEventListener('submit', async (e)=>{await registerSubmit(e)})
}
if(loginForm){
    loginForm.addEventListener('submit', async (e)=> {await loginSubmit(e)})
}
if(logoutBtn){
    logoutBtn.addEventListener('click', async (e)=> {await logout(e)})
}