$(function () {

    // ****************************************
    //  U T I L I T Y   F U N C T I O N S
    // ****************************************

    // Updates the form with data from the response
    function update_form_data(res) {
        $("#id").val(res.id);
        $("#first_name").val(res.first_name);
        $("#last_name").val(res.last_name);
        $("#age").val(res.age);
        $("#bmi").val(res.bmi);
        $("#children").val(res.children);
        $("#sex").val(res.sex);
        $("#region").val(res.region);
        
        if (res.smoke == true) {
            $("#smoke").val("true");
        } else {
            $("#smoke").val("false");
        }
    }

    /// Clears all form fields
    function clear_form_data() {
        $("#id").val("");
        $("#first_name").val("");
        $("#last_name").val("");
        $("#age").val("");
        $("#bmi").val("");
        $("#children").val("");
        $("#sex").val("Unknown");
        $("#smoke").val("Unknown");
        $("#region").val("Unknown");
    }

    // Updates the flash message area
    function flash_message(message) {
        $("#flash_message").empty();
        $("#flash_message").append(message);
    }

    // ****************************************
    // Create a Record
    // ****************************************

    $("#create-btn").click(function () {

        let first_name = $("#first_name").val();
        let last_name = $("#last_name").val();
        let smoke = $("#smoke").val();
        let age = $("#age").val();
        let bmi = $("#bmi").val();
        let children = $("#children").val();
        let sex = $("#sex").val();
        let region = $("#region").val();

        let error = "";
        if (!first_name || first_name === "") {
            error += ", First Name"
        }
        if (!last_name || last_name === "") {
            error += ", Last Name"
        }
        if (!age || age === "") {
            error += ", Age"
        }
        if (sex === "Unknown") {
            error += ", Sex"
        }
        if (!bmi || bmi === "") {
            error += ", BMI"
        }
        if (!children || children === "") {
            error += ", Children"
        }
        if (smoke === "Unknown") {
            error += ", Smoke"
        }
        if (region === "Unknown") {     
            error += ", Region"
        }       

        if (error !== "") {
            $("#flash_message").empty();
            flash_message("Error: Missing " + error.slice(1) + " fields!")
            return
        }

        if (!Number.isInteger(Number(age)) || Number(age) < 0) {
            $("#flash_message").empty();
            flash_message("Error: Age should be positive integer!")
            return
        }

        if (!Number.isInteger(Number(children)) || Number(children) < 0) {
            $("#flash_message").empty();
            flash_message("Error: Number of Children should be positive integer!")
            return
        }
        if (isNaN(Number(bmi)) || Number(bmi) < 0) {
            $("#flash_message").empty();
            flash_message("Error: BMI should be positive number!")
            return
        }

        smoke = smoke == "true";

        let data = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "bmi": bmi,
            "sex": sex,
            "children": children,
            "smoke": smoke,
            "region": region,
        };

        $("#flash_message").empty();
        
        let ajax = $.ajax({
            type: "POST",
            url: "/records",
            contentType: "application/json",
            data: JSON.stringify(data),
        });

        ajax.done(function(res){
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });
    });


    // ****************************************
    // Update a Record
    // ****************************************

    $("#update-btn").click(function () {

        let id = $("#id").val();
        let first_name = $("#first_name").val();
        let last_name = $("#last_name").val();
        let smoke = $("#smoke").val();
        let age = $("#age").val();
        let bmi = $("#bmi").val();
        let children = $("#children").val();
        let sex = $("#sex").val();
        let region = $("#region").val();

        let error = "";
        if (!first_name || first_name === "") {
            error += ", First Name"
        }
        if (!last_name || last_name === "") {
            error += ", Last Name"
        }
        if (!age || age === "") {
            error += ", Age"
        }
        if (sex === "Unknown") {
            error += ", Sex"
        }
        if (!bmi || bmi === "") {
            error += ", BMI"
        }
        if (!children || children === "") {
            error += ", Children"
        }
        if (smoke === "Unknown") {
            error += ", Smoke"
        }
        if (region === "Unknown") {     
            error += ", Region"
        }       

        if (error !== "") {
            $("#flash_message").empty();
            flash_message("Error: Missing " + error.slice(1) + " fields!")
            return
        }

        if (!Number.isInteger(Number(age)) || Number(age) < 0) {
            $("#flash_message").empty();
            flash_message("Error: Age should be positive integer!")
            return
        }

        if (!Number.isInteger(Number(children)) || Number(children) < 0) {
            $("#flash_message").empty();
            flash_message("Error: Number of Children should be positive integer!")
            return
        }
        if (isNaN(Number(bmi)) || Number(bmi) < 0) {
            $("#flash_message").empty();
            flash_message("Error: BMI should be positive number!")
            return
        }

        smoke = smoke == "true";

        let data = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "bmi": bmi,
            "sex": sex,
            "children": children,
            "smoke": smoke,
            "region": region,
        };

        $("#flash_message").empty();

        let ajax = $.ajax({
                type: "PUT",
                url: `/records/${id}`,
                contentType: "application/json",
                data: JSON.stringify(data)
            })

        ajax.done(function(res){
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Retrieve a Record
    // ****************************************

    $("#retrieve-btn").click(function () {

        let id = $("#id").val();

        $("#flash_message").empty();

        let ajax = $.ajax({
            type: "GET",
            url: `/records/${id}`,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function(res){
            //alert(res.toSource())
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            clear_form_data()
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Delete a Record
    // ****************************************

    $("#delete-btn").click(function () {

        let id = $("#id").val();

        $("#flash_message").empty();

        let ajax = $.ajax({
            type: "DELETE",
            url: `/records/${id}`,
            contentType: "application/json",
            data: '',
        })

        ajax.done(function(res){
            clear_form_data()
            flash_message("Record has been Deleted!")
        });

        ajax.fail(function(res){
            flash_message("Server error!")
        });
    });

    // ****************************************
    // Predict a Record
    // ****************************************

    $("#predict-btn").click(function () {

        let id = $("#id").val();

        $("#flash_message").empty();

        let ajax = $.ajax({
            type: "GET",
            url: `/records/${id}/predict`,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function(res){
            $("#predict_results").empty();

            let cost = parseFloat(res.cost)
            let suggestion = ""
            let plan = ""
            if (cost < 10000) {
                suggestion = "Accept"
                plan = "normal"
            }
            else if (cost < 30000) {
                suggestion = "Conditional Accept"
                if (cost < 20000) {
                    plan = "Enhanced Version"
                }
                else {
                    plan = "Extra Condition Version"
                }
            }
            else {
                suggestion = "Refuse"
                plan = "Only Endorsed by Manager"
            }
            let table = '<table class="table table-striped" cellpadding="10">'
            table += '<thead><tr>'
            table += '<th class="col-md-2">Record ID</th>'
            table += '<th class="col-md-2">Cost</th>'
            table += '<th class="col-md-2">Suggestion</th>'
            table += '<th class="col-md-2">Plan</th>'
            table += '</tr></thead><tbody>'

            table +=  `<tr id="row_${0}"><td>${id}</td><td>${cost}</td><td>${suggestion}</td><td>${plan}</td></tr>`;

            table += '</tbody></table>';
            $("#predict_results").append(table);
            flash_message("Success")
        });

        ajax.fail(function(res){
            clear_form_data()
            flash_message(res.responseJSON.message)
        });

    });


    // ****************************************
    // Clear the form
    // ****************************************

    $("#clear-btn").click(function () {
        $("#id").val("");
        $("#flash_message").empty();
        clear_form_data()
    });

})
