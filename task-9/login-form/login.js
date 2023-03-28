function validateForm() {

   
    st=false;
    var un = document.querySelector('#username').value;
    var pw = document.querySelector('#password').value;

    var login_dict = {
        nayan:"123",
        a:"1"

    }

    var username = "u";
    var password = "p";
    if (un in login_dict) {
        if (login_dict[un] == pw) {
            st=true;
         
         
            
        }
    } 
    else {
        alert("Login was unsuccessful, please check your username and password");
        return false;
    }
    if (st==true){
      
        window.location.href = "feed.html";
        return false;
    }

  }

