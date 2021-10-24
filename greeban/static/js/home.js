function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  console.log(decodedCookie);
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
// function product_card(data) {
//     let Q = 0;
//     fetch(`/get_quantity/${data.pk}/`)
//         .then(response =>{console.log(response); return response.json()})
//         .then(response => {
//             console.log(response)
//             Q = response.Q
//             console.log(data.pk,Q)
//             localStorage.setItem(data.pk, Q);
//             console.log(Q);
//         })
//     const temp = `
//     <div class="col-md-4  col-6 col-sm-4 px-5">
//         <div class="card border-0 shadow">
//             <div class="cardimg text-center">
//                 <a href="/product/${data.pk}">
//                     <img class="card-img-top card_img" src="media/${data.fields.product_image}"
//                     alt="Card image cap">
//                 </a>
//             </div>
//         <div class="card-body">
//             <h4 class="card-title  text-left">
//                 <a class="card-title-a" href="/product/${data.pk}">
//                     ${data.fields.product_name}
//                 </a>
//             </h4>
//             <hr class="card-title-hr">
//             <div class="row">
//                 <div class="col-md-6 col-6">
//                     <p id="rcorners2" class="shadow">${data.fields.product_quantity_per_serving_gms} gm</p>
//                 </div>
//                 <div class="col-md-6 col-6">

//                 </div>
//             </div>

//             <div class="row">
//                 <div class="col-6">
//                     <p class="price_pro"><i class="fas fa-rupee-sign"></i> ${data.fields.product_price}</p>
//                 </div>

//                 <div class="col-6 plus_minus_alig center-block">
//                     <input id="{{product.id}}" class="cart mob_plus" type="image" onclick="plus(event,${data.pk})"
//                         width="40" height="40" src="media/greeban/images/plus_prod.png"/>

//                     <p class="inline_cartinput" style="text-align:center;margin-bottom: 0rem;">
//                         <b id="Q-${data.pk}">
//                             ${Q}
//                         </b>
//                     </p>

//                     <input id="pr{{product.id}}" class="cart mob_minus" type="image" onclick="minus(event,${data.pk})"
//                     width="40" height="40" src="media/greeban/images/minus_prod.png"/>

//                     <button id="{{product.id}}" hidden class="cart mob_cart" type="image" onclick="add_to_cart(event,${data.pk})">
//                         <i class="fas fa-cart-arrow-down"></i>
//                     </button>
//                 </div>
//             </div>
//         </div>
//     </div>`
//     return temp
// }
async function product_card(data) {
  var Q = 0;
  var product_c= await fetch(`/get_quantity/${data.pk}/`)
  //console.log(product_c)
  var product_c2= await product_c.json();
  //console.log(product_c2)
          Q = product_c2.Q
          //console.log(data.pk,Q)
          localStorage.setItem(data.pk, Q);
          //console.log(Q);
         
  // console.log(Q,"QQQ")

  const temp = `
  <div class="col-md-4  col-6 col-sm-4 px-5">
      <div class="card border-0 shadow">
          <div class="cardimg text-center">
              <a href="/product/${data.pk}">
                  <img class="card-img-top card_img" src="media/${data.fields.product_image}"
                  alt="Card image cap">
              </a>
          </div>
      <div class="card-body">
          <h4 class="card-title  text-left">
              <a class="card-title-a" href="/product/${data.pk}">
                  ${data.fields.product_name}
              </a>
          </h4>
          <hr class="card-title-hr">
          <div class="row">
              <div class="col-md-6 col-6">
                  <p id="rcorners2" class="shadow">${data.fields.product_quantity_per_serving_gms} gm</p>
              </div>
              <div class="col-md-6 col-6">

              </div>
          </div>

          <div class="row" >
              <div class="col-6">
                  <p class="price_pro"><i class="fas fa-rupee-sign"></i> ${data.fields.product_price}</p>
              </div>
                  

              <div class="col-6 plus_minus_alig center-block" id="plus_minus_block">
                  <input id="{{product.id}}" class="cart mob_plus ${Q>0?'':'d-none'}" type="image" onclick="checklogin(event,${data.pk})"
                      width="40" height="40" src="media/greeban/images/plus_prod.png"/>

                  <p class="inline_cartinput" style="text-align:center;margin-bottom: 0rem;">
                      <b id="Q-${data.pk}">
                          ${Q}
                      </b>
                  </p>
                  <input id="pr{{product.id}}" class="cart mob_minus ${Q>0?'':'d-none'} " type="image" onclick="minus(event,${data.pk})"
                  width="40" height="40" src="media/greeban/images/minus_prod.png"/>
<input id="1" class="shadow outlienadd cart mob_cart ${Q>0?'d-none':''}" type="image" src="/greeban/static/images/cart_icon.png" onclick="add_to_cart(event,${data.pk})">
                  <button id="{{product.id}}"  style="background:green;color:white;font-size: 20px;" hidden class="shadow outlienadd cart mob_cart ${Q>0?'d-none':''}" type="image" onclick="add_to_cart(event,${data.pk})">
                      <i class="fas fa-cart-arrow-down"></i>
                  </button>
              </div>
          </div>
      </div>
  </div>
  
  `

// console.log(temp)
  return temp
}
//let something;
var tempdata;
var selectedCategory='Exotic';
function get_products(category) {
selectedCategory=category;
// removes the grren color from the elements
var els = document.getElementsByClassName("addgreencolor");
while (els[0]) {
  els[0].classList.remove("addgreencolor");
}

  //   Workaround for green leafy
itemName = category;
if (category == "Leafy Greens") {
  itemName = "Leafy";
}

document.getElementById(itemName).classList.add("addgreencolor");
console.log(category, "category");

fetch(`/get_products/?category=${category}`)
  .then((response) => response.json())
  .then(async (response) => {
    tempdata = JSON.parse(response.data);
    // localStorage.setItem("mydata", JSON.stringify(tempdata));
    //console.log(tempdata,"Hello")
    document.getElementById("ourproducecarousel").innerHTML = "";
    document.getElementById("ourproducecarousel").innerHTML =
      '<div class="row">';
    let i = 0;
    for (i = 0; i < tempdata.length; i++) {
      // something=JSON.parse(response.data)[i]
      // onclick="plus(event,${data.pk})
      const temp_html = await product_card(JSON.parse(response.data)[i]);
      // if( i%3 === 0 ){
      //     console.log("ddjfksdf")
      //     document.getElementById('ourproducecarousel').innerHTML += `<div class="carousel-item active">`
      // }
      document.getElementById("ourproducecarousel").innerHTML += temp_html;
      // if( i%3 === 2 || i === tempdata.length-1){
      //     console.log("sdfhsljdfhs;lafkjsdhfkasdfh")
      //     document.getElementById('ourproducecarousel').innerHTML += '</div>'
      // }
    }
    document.getElementById("ourproducecarousel").innerHTML += `</div>`;
  });

}

function sendMail() {
  var emailID = document.getElementById("inputemail").value;

  //Code for encrypting email id
  emailUsername = emailID.split("@");
  emailUsernameLength = emailUsername[0].length;
  emailUsername[0] = emailUsername[0].replace(
    emailUsername[0].slice(2, -2),
    "*".repeat(emailUsernameLength - 4)
  );
  document.getElementById("emailVerificationNotification").innerHTML =
    "Please enter the code sent on " + emailUsername.join("@");
  ////////////////////////////

  let csrftoken = getCookie("csrftoken");
  fetch("/sendEmail", {
    method: "POST",
    body: JSON.stringify({
      EmailID: emailID,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
    credentials: "same-origin",
  })
    .then((response) => response.json())
    .then((response) => {
      console.log(response.message);
    });
}
function removePromotions(){
  var code=document.getElementById("promocode").value;
      let csrftoken = getCookie('csrftoken');
       //document.getElementById("discount").innerText=Math.floor(Number( document.getElementById("Total_cart_price").innerText)*response/100)

      document.getElementById("final_cart_amount_incl_shipping").innerText=Number( document.getElementById("final_cart_amount_incl_shipping").innerText)+Number( document.getElementById("discount").innerText)
    document.getElementById("discount").innerText=0;
       document.getElementById("price").value=Number( document.getElementById("final_cart_amount_incl_shipping").innerText);

//                alert("promotion applied with "+response+"% discount")
        document.getElementById(
          "removePromotionsButton"
        ).style.display = 'none';
        document.getElementById(
          "applyPromotionsButton"
        ).style.display = 'block';
        document.getElementById("promocode").readOnly = false;

}

function applyPromotions(){
  var code=document.getElementById("promocode").value;
      let csrftoken = getCookie('csrftoken');

      fetch('/applyPromotions', {
          method: "POST",
          body: JSON.stringify({
              code: code
          }),
          headers: {
              "X-CSRFToken": csrftoken,
              "Content-type": "application/json; charset=UTF-8"
          },
          credentials: 'same-origin'
      })
      .then(response => response.text())
      .then(response => {
          if(response=="failure")
          alert("wrong  promocode")
          else{

               document.getElementById("discount").innerText=Math.floor(Number( document.getElementById("Total_cart_price").innerText)*response/100)

              document.getElementById("final_cart_amount_incl_shipping").innerText=Number( document.getElementById("final_cart_amount_incl_shipping").innerText)-Number( document.getElementById("discount").innerText)

               document.getElementById("price").value=Number( document.getElementById("final_cart_amount_incl_shipping").innerText);

//                alert("promotion applied with "+response+"% discount")
        document.getElementById(
          "applyPromotionsButton"
        ).style.display = 'none';
        document.getElementById(
          "removePromotionsButton"
        ).style.display = 'block';
                document.getElementById("promocode").readOnly = true;
          }
          console.log(response);
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
  }else{
      alert("wrong otp")
  }
}

// globalvar=[]
function plus(event, id) {
  //console.log(event,"event")
  event.preventDefault()
  let csrftoken = getCookie('csrftoken')

  // globalvar.push(id)
  // console.log(globalvar)
  //console.log(id,"id")
  //console.log(csrftoken, csrftoken.length)
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
          //console.log(response)

          document.getElementById(`Q-${id}`).innerText = response.cart[id]

      });

}
total=0
function plus2(event, id) {
  //console.log(event,"event")
  event.preventDefault()
  let csrftoken = getCookie('csrftoken')

  // globalvar.push(id)
  // console.log(globalvar)
  //console.log(id,"id")
  //console.log(csrftoken, csrftoken.length)
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
          //console.log(response,"resp")


          document.getElementById(`Q-${id}`).innerText = response.cart[id];
          document.getElementById(`R-${id}`).innerText=response.cart[id];
          // document.getElementsByClassName("prd_cnt").innerHTML +=1
          per_quantity=Number(document.getElementById(`PerQuantityPrice-${id}`).innerText)
          document.getElementById(`S-${id}`).innerText=per_quantity*response.cart[id];
          total+= Number(document.getElementById(`S-${id}`).innerText)

          document.getElementById("Total_Money").innerText=Number(document.getElementById("Total_Money").innerText)+per_quantity

          // Total_Money

          //console.log("hello")
           displaytotalinAdd()
          // console.log(total,"total")



      });

}


function minus(event, id) {
  event.preventDefault()
  let csrftoken = getCookie('csrftoken')
  //console.log(id)
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
          //console.log(response)
          const temp = response.cart[id]
          //console.log(temp)
          if (temp) {
              document.getElementById(`Q-${id}`).innerText = temp

              return
          }
          document.getElementById(`Q-${id}`).innerText = 0
                                    get_products(selectedCategory)

          // location.reload()
      });

}
function minus2(event, id) {
  event.preventDefault()
  let csrftoken = getCookie('csrftoken')
  //console.log(id)
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
          //console.log(response)
          const temp = response.cart[id]
          //console.log(temp)
          if (temp) {
              document.getElementById(`Q-${id}`).innerText = response.cart[id];
              document.getElementById(`R-${id}`).innerText=response.cart[id];
              // document.getElementsByClassName("prd_cnt").innerHTML +=1
              per_quantity=Number(document.getElementById(`PerQuantityPrice-${id}`).innerText)
              document.getElementById(`S-${id}`).innerText=per_quantity*response.cart[id];
              document.getElementById("Total_Money").innerText=Number(document.getElementById("Total_Money").innerText)-per_quantity

         displaytotalinAdd()
         return
          }else{
              document.getElementById(`Q-${id}`).innerText = 0
               displaytotalinAdd()
              location.reload()

          }

      });

}
// globalvar=[]
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
          //location.reload();
          get_products(selectedCategory)
      });

      }
      else {
          $('#login').click();

      }
  })




}
function displaytotalinAdd(){
// console.log("here")
document.getElementById("Total_cart_price").innerText=document.getElementById("Total_Money").innerText
//console.log(document.getElementById("shipping_fees").innerText)
//console.log(document.getElementById("Total_cart_price").innerText)
document.getElementById("final_cart_amount_incl_shipping").innerText=Number( document.getElementById("shipping_fees").innerText)+Number( document.getElementById("Total_cart_price").innerText)
//price_cal = Number( document.getElementById("shipping_fees").innerText)+Number( document.getElementById("Total_cart_price").innerText)
//const paisa = 100
//document.getElementById("price").innerText=price_cal*Number(paisa)
    //document.getElementsByTagName("body")[0].scrollTop
}


function checklogin(event,id){
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
      if(response=="success")
          plus(event,id)
      else
          $('#login').click();
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
function logout(event,id){
  var userLoggedIn= ""
  let csrftoken = getCookie('csrftoken')

  fetch('/logout', {
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
          alert("logged out")
          location.reload();
          location.href = "/";
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
function onAddrressSubmit(event){
  console.log("hello")
  let userinfo={}
    if ( ( $('#fullname').val() == "" )
    || ( $('#phonenumber').val() == "" )
    || ( $('#emailid').val() == "" )
    || ( $('#pincode').val() == "" )
    || ( $('#state').val() == "" )
    || ( $('#city').val() == "" )
    || ( $('#address').val() == "" )
    || ( $('#phonenumber').val().length !=10 )
    )
    {
        return;
    }

    event.preventDefault()
    $(".checkpay").show();
  userinfo.name=document.getElementById('fullname').value
  userinfo.mobile_no=document.getElementById('phonenumber').value
  userinfo.email=document.getElementById('emailid').value
  userinfo.pin=document.getElementById('pincode').value
  userinfo.state=document.getElementById('state').value
  userinfo.city=document.getElementById('city').value
  userinfo.address=document.getElementById('address').value

  // console.log(fullname,phonenumber,emailid,pincode,state,city,address)
  console.log(userinfo)
  let csrftoken = getCookie('csrftoken')

  fetch('/addUserInfo', {
      method: "POST",
      body: JSON.stringify({
          userDetails: userinfo
      }),
      headers: {
          "X-CSRFToken": csrftoken,
          "Content-type": "text/plain; charset=UTF-8"
      },
      
      credentials: 'same-origin'
  })
  .then(response => response.text())
  .then(response => {
      console.log(response)
     alert("Details updated  successfully")
  })

}
// for profile page
function getUserInfo(){
  console.log("hello")
  // console.log(fullname,phonenumber,emailid,pincode,state,city,address)
  let csrftoken = getCookie('csrftoken')

  fetch('/getUserInfo', {
      method: "POST",

      headers: {
          "X-CSRFToken": csrftoken,
          "Content-type": "text/plain; charset=UTF-8"
      },
      credentials: 'same-origin'
  })
  .then(response => response.json())
  .then(response => {
  //    alert("something");
      console.log(response);
      // document.getElementById('details').innerHTML="test"
      document.getElementById('fullname').value=response.name
      document.getElementById('phonenumber').value=response.mobile_no
      document.getElementById('emailid').value=response.email
      document.getElementById('pincode').value=response.pin
      document.getElementById('state').value=response.state;
      document.getElementById('city').value=response.city
      document.getElementById('address').value=response.address
      

  })

}
/*
var stickyOffset = $('.sticky').offset().top;

$(window).scroll(function(){
  var sticky = $('.sticky'),
      scroll = $(window).scrollTop();

  if (scroll >= stickyOffset) sticky.addClass('fixed');
  else sticky.removeClass('fixed');
});*/
