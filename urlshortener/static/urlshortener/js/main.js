$(document).ready(function(){

    const services = {
        SendURLs: function(urls) {
            if(urls.length > 100){
                console.error("Too many urls");
                return;
            }
            return $.ajax({
                'type': 'post',
                'url': '/api/',
                'data': JSON.stringify(urls),
                'contentType': 'application/json'
            });
        }
    };
    var clipboard = new ClipboardJS('.btn');

    clipboard.on('success', function(e) {
        e.clearSelection();
        $(e.trigger).tooltip("enable");
        $(e.trigger).tooltip("show");
        $(e.trigger).tooltip("disable");
    });

    $("#warning-too-much-urls").hide();

    $("#urls-inpt").on('keyup keypress blur change', function(e) {
        const urls = $("#urls-inpt").val();
        if(urls.length == 0) {
            $("#warning-too-much-urls").hide();
            return;
        }
        const urlsList = urls.split("\n");
        if(urlsList.length > 100) {
            $("#process-btn").prop("disabled", true);
            $("#warning-too-much-urls").show();
            e.preventDefault();
        } else {
            $("#process-btn").prop("disabled", false);
            $("#warning-too-much-urls").hide();
        }
    });


    $("#process-btn").click(function(){
        const urls = $("#urls-inpt").val();
        
        if(!urls || urls.length == 0) {
            return;
        }

        const urlsList = urls.split("\n");
        services.SendURLs(urlsList).then(function(resp){
            var count = 1;
            const view = {
                current: 0,
                urls: resp,
                fn: function(){ 
                    this.current = count++; 
                    return this.current; 
                }
            };
            var urlList = Mustache.render($("#tmpl-short-urls").html(), view);
            $("#tbl-short-urls tbody").html(urlList);
        });
    });
});