
frappe.ui.form.on('Project', {
	refresh:function(frm){
 	let project_name=frm.doc.name
	frm.add_custom_button(__("Allocate User"), function() {
	  console.log("hellll")
	  
	  const table_fields=[
		{
		  fieldname: "userList", fieldtype: "Link",
		  in_list_view: 1, label: "userlist",
		  options: "User", reqd: 1
		}
					
					]
	  let d = new frappe.ui.Dialog({
	  
    title: 'Enter details',
    fields: [
        
        {   
          
	 fieldname: "userdetails",
	 fieldtype: "Table",
	 label: "UserDetails",
	 cannot_add_rows: false,
	 in_place_edit: true,
	 reqd: 1,
	 data: [],
	 fields: table_fields
          
        }
    ],
    primary_action_label: 'Add User',
    primary_action(values) {
      for (let i =0; i<values.userdetails.length;i++) {
       console.log(values.userdetails[i].userList)
       frappe.call({
		    method: 'buzztag.buzztag.custom_script.project.allocate_user',
		    args: {
		    "userdetails":values.userdetails[i].userList,
		    "project_name":project_name
		    },
		    callback: function(r) {
		    
		    }
		    })
      }
        

        d.hide();
    }
});

d.show();

	
	
	})
	
	 
	}
	


})	


