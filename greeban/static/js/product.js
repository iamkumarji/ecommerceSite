function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
//added by rohan
function goToProfile(){
        var userLoggedIn= ""
    let csrftoken = getCookie('csrftoken')

    fetch('/checkLoginStatus', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "text/plain; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
    .then(response => response.text())
    .then(response => {
        userLoggedIn = response;
        console.log(response);;
        if(response=="success") {
            window.location.href = "/profile";
        }
        else
            $('#login').click();
    })

}
function sendMail() {
    var emailID = document.getElementById('inputemail').value;
    let csrftoken = getCookie('csrftoken');
    fetch('/sendEmail', {
        method: "POST",
        body: JSON.stringify({
            EmailID: emailID
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
    .then(response => response.json())
    .then(response => {
        console.log(response.message);
    })
}

function verifyOtp() {
    var enteredOtp = document.getElementById('partitioned').value;
    let otp = getCookie('OTP');
    if(enteredOtp == otp){
        var emailID = document.getElementById('inputemail').value;
        let csrftoken = getCookie('csrftoken');
        fetch('/activateSession', {
            method: "POST",
            body: JSON.stringify({
                EmailID: emailID
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            },
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(response => {
            console.log(response.message);
        })
        alert("logged in")
    }
}

function checklogin(name,event,id){
    var userLoggedIn= ""
    let csrftoken = getCookie('csrftoken')

     fetch('/checkLoginStatus', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "text/plain; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
    .then(response => response.text())
    .then(response => {
        userLoggedIn = response;
        console.log(response);;
        if(response=="success") {

        }
        else {
            $('#login').click();

        }
    })

    // const usr = document.getElementById("checkusr").value;
    // console.log(usr)
    // if (usr == true)
    // {
    //     console.log('uncheck')
    //     plus(event,id);
    // }
    // else
    // {
    //     console.log('check')
    //     //$('#modellogin').modal();
    // }
    //plus(event,id);
    //console.log('check')
}
//end by  rohan
function plus(event, id) {
    console.log(event, "event")
    event.preventDefault()

    let csrftoken = getCookie('csrftoken')


    fetch('/checkLoginStatus', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "text/plain; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
        .then(response => response.text())
        .then(response => {
            userLoggedIn = response;
            console.log(response);
            ;
            if (response == "success") {
                // globalvar.push(id)
                console.log(id)
                console.log(id, "id")
                console.log(csrftoken, csrftoken.length)
                fetch("/", {
                    method: "POST",
                    body: JSON.stringify({
                        prod: id
                    }),
                    headers: {
                        "X-CSRFToken": csrftoken,
                        "Content-type": "application/json; charset=UTF-8"
                    },
                    credentials: 'same-origin'
                })
                    .then(response => response.json())
                    .then(response => {
                        console.log(response)

                        document.getElementById(`Q-${id}`).innerText = response.cart[id]
                        

                    })
            } else {
                $('#login').click();

            }


        })
}


function minus(event, id) {
    event.preventDefault()
    let csrftoken = getCookie('csrftoken')
    console.log(id)
    //console.log(csrftoken, csrftoken.length)
    fetch("/", {
        method: "POST",
        body: JSON.stringify({
            prod: id,
            remove: true
        }),
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "application/json; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(response => {
            console.log(response)
            const temp = response.cart[id]
            console.log(temp)
            if (temp) {
                try{
                    document.getElementById(`Q-${id}`).innerText = temp
                    return
                }
                catch(err){
                    return
                }
                
            }
            document.getElementById(`Q-${id}`).innerText = 0
            location.reload()
        });

}

function add_to_cart(event, id) {
    event.preventDefault()

    let csrftoken = getCookie('csrftoken')
         fetch('/checkLoginStatus', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "text/plain; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
    .then(response => response.text())
    .then(response => {
        userLoggedIn = response;
        console.log(response);;
        if(response=="success") {
    fetch("/", {
        method: "POST",
        body: JSON.stringify({
            prod: id
        }),
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "application/json; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(response => {
            location.reload();
        });

        }
        else {
            $('#login').click();

        }
    })
}


// plus minus function for mobile view
function plus_m(event, id) {
    console.log(event, "event")
    event.preventDefault()

    let csrftoken = getCookie('csrftoken')


    fetch('/checkLoginStatus', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "text/plain; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
        .then(response => response.text())
        .then(response => {
            userLoggedIn = response;
            console.log(response);
            ;
            if (response == "success") {
                // globalvar.push(id)
                console.log(id)
                console.log(id, "id")
                console.log(csrftoken, csrftoken.length)
                fetch("/", {
                    method: "POST",
                    body: JSON.stringify({
                        prod: id
                    }),
                    headers: {
                        "X-CSRFToken": csrftoken,
                        "Content-type": "application/json; charset=UTF-8"
                    },
                    credentials: 'same-origin'
                })
                    .then(response => response.json())
                    .then(response => {
                        console.log(response)
                        try{
                            console.log(response.cart[id]);
                            document.getElementById(`QM-${id}`).innerText = response.cart[id]
                            document.getElementById('cart_items').innerText = Number(document.getElementById('cart_items').innerText)+Number(1)
                        }
                        catch(err){
                            document.getElementById('cart_items').innerText = Number(document.getElementById('cart_items').innerText)+Number(1)
                        }
                        
                        

                    })
            } else {
                $('#login').click();

            }


        })
}

function minus_m(event, id) {
    event.preventDefault()
    let csrftoken = getCookie('csrftoken')
    console.log(id)
    //console.log(csrftoken, csrftoken.length)
    fetch("/", {
        method: "POST",
        body: JSON.stringify({
            prod: id,
            remove: true
        }),
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-type": "application/json; charset=UTF-8"
        },
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(response => {
            console.log(response)
            const temp = response.cart[id]
            console.log(temp)
            if (temp) {
                try{
                    document.getElementById(`QM-${id}`).innerText = temp
                    document.getElementById('cart_items').innerText = Number(document.getElementById('cart_items').innerText)-Number(1)
                    return
                }
                catch(err){
                    document.getElementById('cart_items').innerText = Number(document.getElementById('cart_items').innerText)-Number(1)
                    return
                }
                
            }
            try{
                document.getElementById(`QM-${id}`).innerText = 0
                location.reload()
            }
            catch(err){
                location.reload()
            }
            
        });

}