function alertcourses() {
    var selectcourse1 = document.getElementById("setcourses1");
    var index1 = selectcourse1.selectedIndex;
    var value1 = selectcourse1.options[index1].value;
    //retrieve the value=courses' id
    if(value1 == 0){
        alert("you must choose a subject!");
        //This case happened if the student didn't choose a subject
        return false;
    }

    for(z = 0; z < my_subject_id.length; z++){
        if(parseInt(value1) == parseInt(my_subject_id[z])){
            //This case happened if the student choose the same subject
            alert("you can't enroll in same subject");
        }
    }

}

function setCourses1(){
    /*This function will show a selection list
      of all the subject that the student can enroll,
      this selection list is link with the database
     */
    var select = document.getElementById("setcourses1");
    select.length = 1;
    select.options[0].selected = true;
    for(var x = 0;x<id.length;x++){
        var option = document.createElement("option");
        option.setAttribute("value",id[x]);
        option.appendChild(document.createTextNode(value[x]));
        select.appendChild(option);
    }
}

function deleteCourse(){
    /*This function will show a selection list
    that shows the enrolled subject. this selection list
    is link with the database*/
    var select = document.getElementById("deletecourses");
    select.length =1;
    select.options[0].selected = true;
    for(var x =0; x<my_subject_id.length;x++){
        var option = document.createElement("option");
        option.setAttribute("value",my_subject_id[x]);
        option.appendChild(document.createTextNode(my_subject_name[x]));
        select.appendChild(option);
    }
}

window.onload=function(){
    //This function run the JS function when the HTML start
    setCourses1()
    deleteCourse()
}