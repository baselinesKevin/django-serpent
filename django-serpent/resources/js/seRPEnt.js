	function createrequest(module_id) {
	    var data = {"":""};
	    var args = { type:"POST", url:module_id+"/", data:data, complete:done, success:done2 };
	    $("#jobstatus").html('<p class="style1 f-lp">Sending job to server...</p>');
	    $.ajax(args);
	    $("#jobstatus").html('<p class="style1 f-lp">Executing job on server. Please wait.</p>');
	    var d = new Date()
	    $("#jobstatus").append('<p class="style1 f-lp"><i>Job sent to server on ' + d + '.</i></p>');
	    $("#jobstatus").append('<p class="style1 f-lp"><b>Serpent is beta software. If serpent doesn\'t generate a small document in ample time, please notify your DOORS Administrator.</b></p>');
	
	}
	

	function done2(res, status) {
		$("#pinwheel").hide();
		$("#jobstatus").html('<p class="style1 f-lp">Thank you for using seRPEnt. You may close this window.</p>');
	}
	
  	function done(res, status) {
		//Internet Explorer does not like the next line ... not sure it's needed
		var data = eval('(' + res.responseText + ')');
		if (status == "success"){
			window.location=window.location + "download/" + data.filename;
		}
  	}	