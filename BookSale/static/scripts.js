  $(document).ready(function(){
            $("p").click(function(){
                alert("you clicked the header")
            });  
            $("button").bind("click",function(){
                $.getJSON("/name",{
                    
                },function(data){
                    $("h1").text(data.name);
                    
                });
                return false;
            });
        });