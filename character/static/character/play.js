$(function(){

    $('#roll_id').click(function(){
        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken': csrftoken},
            url: "roll/",
            data: {dVal: 100},
            success: function(response) {
                $("#roll_out_id").html(response["dResult"]);
            },
            error: function (response) {
                alert("Error");
            }
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');