$(function(){

    $('#bonus_dice_minus_id').click(function(){
        num_bonus_dice --;
        $('#num_bonus_id').html(getBonusDiceText());
    });

    $('#bonus_dice_plus_id').click(function(){
       num_bonus_dice ++;
        $('#num_bonus_id').html(getBonusDiceText());
    });

    $('#roll_id').click(function(){
        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken': csrftoken},
            url: "roll/",
            data: {d_val: 100, character_id: $("#character_id").val(), roll_skill: roll_skill, num_bonus_dice: num_bonus_dice },
            success: function(response) {
                $("#roll_out_id").html(response["d_result"]);
                $("#roll_message_id").html(response["message_out"]);
                $("#roll_debug_out_id").html(response["debug_out"]);
            },
            error: function (response) {
                alert("Error");
            }
        });
    });

    $('.d100-rollable').click(function(){
        console.log($(this).attr('value'));
        $('#roll_selection_id').html($(this).parent().prev().html()+" "+$(this).attr('value'));
        roll_skill = $(this).attr('skill-name');
        console.log(roll_skill);
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

function getBonusDiceText()
{
    var message;
    if(num_bonus_dice>=0)
        {
            message = "+"+num_bonus_dice+" Bonus Dice";
        }
        else
        {
            message = num_bonus_dice+" Penalty Dice";
        }
    return message;
}

var num_bonus_dice = 0;
var roll_skill = '';

const csrftoken = getCookie('csrftoken');
