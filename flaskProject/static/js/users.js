fetch('https://reqres.in/api/users?page=2')
.then(response => response.json())
.then(responseJSON =>creatuserlist(responseJSON.data))
.catch(err => console.log(err));


function creatuserlist(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for(let user of users){
        const section = document.createElement("section");
        section.innerHTML= `<div style="font-size: 30px; text-align: center;  ">
        <img src = "${user.avatar}"/>
        <br>
        <span > ${user.first_name} ${user.last_name} </span>
        <br>
        <a href = "mailto: ${user.email}" > send email </a>
        <br>        </div> `;
        curr_main.appendChild(section);
    }
}
