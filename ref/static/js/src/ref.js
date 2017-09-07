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
        debugger;
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
        $.ajax({
            type: "POST",
            url: handlerUrl1,
            data: JSON.stringify({"data": data}),
            success: function(result){
                
            }
        });
    });
}
