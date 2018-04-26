
//#dirction of doquiz

function doquiz(){


    var url = 'http://localhost:8000/selectquiz/'+ $("#course_id").val();
    window.location.href = url;

}

//#dirction of makequiz
function makequiz(){


    var url = 'http://localhost:8000/choose_to_add/'+ $("#course_id").val();
    window.location.href = url;

}
function search_q(){

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },


    data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
});
    $.ajax({
        url:"/subject/search/",
        type: "Post",
        data: {
            content: $("#search").val(),


        },
        success: function (arg) {
            alert("search")

            $('#question').empty();
            var newq = document.getElementById('question');
for (i = 0; i < q_list.length; i++) {

    var h2 = document.createElement('h2');
    var p =document.createElement('p');
    var p2=document.createElement("p");
    h2.valueOf(q_list[i].Q_title);
    h2.href="{% url 'question:question_detail' subid=q_list[i].course_id qid=q_list[i].id %}";
    p.valueOf("Publish"+q_list[i].create+"by"+q_list[i].writer);
    p2.valueOf(q_list[i].Q_des);

    newq.parentNode.appendChild(h2);



}






        }

    })
}

function likea () {
    var aa= parseInt($("#qlike").val())+1;
    var nextq=
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },


    data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
});
$.ajax({
    url:"/subject/like/",
    type:"Post",
    dataType:"Text",
    data : {qqid:$("#qid").val(),
            like_num:$("#qlike").val(),

			},
    success:function (arg) {
        //alert("ss");
        for (i = 0; i < courses_id.length; i++) {}

    },
    error:function (arg) {
        //alert("error");

    }

})
    location.assign(location.href);

}
//#display of add question
function new_question() {

    document.getElementById("add_answer").style.display='none';
    document.getElementById("create_question").style.display='block';

}

//#display of add question
function new_questionb() {
    document.getElementById("create_question1").style.display='block';



    $(function(){

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        <!--获取csrftoken-->
        var csrftoken = getCookie('csrftoken');
        console.log(csrftoken);

        //Ajax call
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test

            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });



    });
}
