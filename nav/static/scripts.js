$(document).ready(function(){
      alert('the doc is ready ')
      var $div = $("<div>", {id: "foo", "class": "thumbnail"});
      var div2 = $("<div>",{"class":"caption"});
      var h1 = $("<h1>");
     // var data_got = null;
      //lets get the data
   /*   $(function(){
            alert("ready to initiate the downlaod function ");
            $("div.thumbnail").bind("",function(){
                  alert('inside to download the data')
                  $.getJSON("/calculate",{},function(data){
                        data_got=data;
                        alert("got the data : ",data);
                  });
            });
      });
      */
      
      $("#column").append($div.append("<span/>")
      .text("hello world"));
      $div.append(div2.append(h1).text("lets try the data download"));
      
      
    });