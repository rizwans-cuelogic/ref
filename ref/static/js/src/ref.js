/* Javascript for RefXBlock. */
function RefXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');
        var handlerUrl1 = runtime.handlerUrl(element,'create_reference');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });

    $( "#submit" ).click(function() {
        
        var error_one = 0
        var error_two = 0
        reference_name = $('#id_reference_name').val()
        reference_type = $('#id_reference_type').val()
        reference_description = $('#id_reference_description').val()
        reference_status = $('#id_reference_status').val()
        reference_link = $('#id_reference_link').val()
        data={}
        data.reference_name=reference_name 
        data.reference_type=reference_type 
        data.reference_description=reference_description
        data.reference_status=reference_status 
        data.reference_link = reference_link
        if (reference_name == '')
        {
            if ($("#id_reference_name").next(".error-message").length == 0){
                $("#id_reference_name").after("<span class='error-message'>Name is required.</p>");
            }
            $( "#id_reference_name" ).focus();
            error_one = 1;
        }   
        if(reference_link == ''){
            if ($("#id_reference_link").next(".error-message").length == 0){
                $("#id_reference_link").after("<span class='error-message'>Link is required.</p>");
            }
            $( "#id_reference_link" ).focus();
            error_two =1;
        }
        if( error_one == 0){
            $("#id_reference_name").next(".error-message").remove();
        }
        if( error_two == 0){
            $("#id_reference_link").next(".error-message").remove();
        }
        if(error_one && error_two){
            $( "#id_reference_name" ).focus();
        }
        
        if( error_one || error_two){
            return ;
        }
        $.ajax({
            type: "POST",
            url: handlerUrl1,
            data: JSON.stringify({"data": data}),
            success: function(result){
                window.location.reload(false);
            }
        });
    });


    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });
}
