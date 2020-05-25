function myFunction(id)
{
    document.getElementById(id).innerHTML="我的第一个 JavaScript 函数";
}

function login(a,b)
{   
    var num_a,num_b
    num_a=Number(document.getElementById(a).value)
    num_b=Number(document.getElementById(b).value)
    if(Number(document.getElementById("preresulte").value)==num_a+num_b)
    {
        document.getElementById('login').value="="
    }
    else{
        document.getElementById('login').value="!="
    }

    //console.log(document.getElementById(a).value)
}