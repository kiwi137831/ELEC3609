function courseBtn1() {
    /*This function creates numberous courses enrolled by the student, or teacher
    * the number of courses is related to the database, the number of buttons is created
    * actively*/
    for (i = 0; i < courses.length; i++) {
        var firstDiv = document.getElementById("allcourses");
        //get the 'allcourses' id, allow the JS to create new div box inside this id
        var secondDiv = document.createElement("div");
        //create the first div
        secondDiv.class = "courses";
        secondDiv.style.margin = "50px 0px 50px 50px";
        secondDiv.style.width = "50%";
        secondDiv.style.height = "100px";
        //set the stylesheet of the fist div

        var thirdDiv = document.createElement("div");
        thirdDiv.class = "color_box";
        //create the thriddiv, give it class name
        thirdDiv.style.float = "left";
        thirdDiv.style.height = "100%";
        thirdDiv.style.width = "10px";
        thirdDiv.style.backgroundColor = "#4CAF50";
        thirdDiv.style.borderRadius = "10px 0px 0px 10px";
        //set the stylesheet of the thridDiv

        var fourthDiv = document.createElement("div");
        fourthDiv.class = 'btn1';
        //create the fourthDiv, give it class name

        var fifthDiv = document.createElement("input");
        var urls = "window.location='/subject/" + courses_id[i] + "';";
        fifthDiv.setAttribute("onclick",urls);
        fifthDiv.class = 'btn1';
        //set up the fifthDiv, give it atively urls which related to the courses' id
        fifthDiv.id = 'id1';

        fifthDiv.style.float = "left";
        fifthDiv.style.width = "95%";
        fifthDiv.style.height = "100px";
        fifthDiv.style.backgroundColor = "#4CAF50";
        fifthDiv.style.border = "none";
        fifthDiv.style.color = "white";
        fifthDiv.style.padding = "0px";
        fifthDiv.style.textAlign= "center";
        fifthDiv.style.textDecoration= "none";
        fifthDiv.style.display = "inline-block";
        fifthDiv.style.fontSize = "25px";
        fifthDiv.style.margin= "0px";
        fifthDiv.style.transitionDuration= "0.4s";
        fifthDiv.style.cursor = "pointer";
        fifthDiv.style.backgroundColor = "white";
        fifthDiv.style.color = "black";
        fifthDiv.style.border = "2px solid #4CAF50";
        fifthDiv.style.borderRadius = "0px 10px 10px 0px";
        //set up the css of the fifthDiv

        fifthDiv.setAttribute("value",courses[i] + detailss[i]);
        fourthDiv.appendChild(fifthDiv);
        secondDiv.appendChild(thirdDiv);
        secondDiv.appendChild(fourthDiv);
        firstDiv.appendChild(secondDiv);
        //use the appChild function to allows the JS actively display in the HTML
    }
}

window.onload=function() {
    courseBtn1();
    //use the window.onload function to call the JS function when the HTML get called
}