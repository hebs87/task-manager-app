$(document).ready(function() {

    //Collapsible command for the accordion from Materialize
    $('.collapsible').collapsible();

    //Category select form initialization command
    $('select').material_select();

    //Date picker commands from Materialize
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false, // Close upon selecting a date,
        container: undefined // ex. 'body' will append picker to body
    });

});
