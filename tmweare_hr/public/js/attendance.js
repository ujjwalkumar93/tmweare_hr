frappe.ui.form.on('Attendance', {
    employee: function(frm){
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function (position) {
                // The position object contains latitude and longitude
                const employeeLatitude = position.coords.latitude;
                const employeeLongitude = position.coords.longitude;
                frappe.call({
                    method: 'tmweare_hr.api.calculate_distance',
                    args : {
                        emp_lat : employeeLatitude,
                        emp_long : employeeLongitude
                    },
                    callback : (resp) => {
                        console.log('responce is: ', resp.message)
                        if(resp.message){
                            frm.doc.invalid_distance = resp.message
                            frm.refresh_field("invalid_distance");
                        }
                    }
                })
            }, function (error) {
                // Handle any errors that occur when trying to get the location
                switch (error.code) {
                    case error.PERMISSION_DENIED:
                        frappe.throw("User/System denied the request for geolocation.");
                        break;
                    case error.POSITION_UNAVAILABLE:
                        frappe.throw("Location information is unavailable.");
                        break;
                    case error.TIMEOUT:
                        frappe.throw("The request to get user location timed out.");
                        break;
                    case error.UNKNOWN_ERROR:
                        frappe.throw("An unknown error occurred.");
                        break;
                }
            });
        } else {
            // Geolocation is not available in this browser
            console.error("Geolocation is not available in this browser.");
        }
    },
    validate: function(frm){
        if(frm.doc.invalid_distance === 1){
            frappe.throw("You can not mark attendance as you are exceeding the allowed distance")
        }
    }
})
