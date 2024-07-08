var previous_form
frappe.ui.form.on('Task', {
	status:function(frm) {
		if(frm.doc.status == 'Completed'){
			frm.set_value('completed_by',frappe.session.user)
			frm.set_value('completed_on',frappe.datetime.get_today() )
		}
	},
	refresh(frm){
	    previous_form = {...frm.doc}
	},
	task_asign_to(frm){
	    previous_form.task_assign_to = frm.doc.task_assign_to
	},
	// after_save(frm){
	//     frm.trigger('validate_and_create_docshare_for_session_user')
	//    // if(frm.doc.task_assign_to !== previous_form.task_assign_to && Boolean(frm.doc.task_assign_to)){
	//     if(frm.doc.task_assign_to){
	//         frm.trigger('validate_and_create_docshare')
	//     }
	    
	// },
	// validate_and_create_docshare(frm){
	//    frappe.call({
  //            method: "buzztag.buzztag.custom_script.task.create_docshare",
  //           //type: "POST",
  //           args: {doctype:frm.doc.doctype, name:frm.doc.name, assigned_to:frm.doc.task_assign_to},
  //           callback: function(r) {
  //             console.log(r)
  //           },
  //           // error: function(r) {},
  //           // always: function(r) {},
  //           // btn: opts.btn,
  //           freeze: false,
  //           freeze_message: "",
  //           async: true,
  //           //url: "/api/method/create_docshare",
  //       });

  //   },
    // validate_and_create_docshare_for_session_user(frm){
	  //  frappe.call({
    //          method: "buzztag.buzztag.custom_script.task.create_docshare_for_task_session_user",
    //         //type: "POST",
    //         args: {doctype:frm.doc.doctype, name:frm.doc.name, assigned_to:frm.doc.task_assign_to, session_user:frappe.session.user},
    //         callback: function(r) {
    //           console.log(r)
    //         },
    //        freeze: false,
    //         async: true
    //         //url: "/api/method/create_docshare_for_task_session_user",
    //     });

    // }
});


