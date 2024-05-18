function updateAnswer(data) {
    the_json = data;

    name = the_json['name'];

    answer = the_json['value'];

    the_name = document.getElementById("bold_name");
    the_name.innerHTML = name;
    
    the_answer = document.getElementById("bold_answer");
    the_answer.innerHTML = answer; 

}

function fetchAnswer() {
    the_name = document.getElementById("name_input").value;

    URL = "/lookup/" + the_name;

    fetch(URL).then( response => response.json()).then( data => updateAnswer(data) );


    
    console.log(URL);
   
}


