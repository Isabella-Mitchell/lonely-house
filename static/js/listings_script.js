const $ = require('jquery');

function updatePageWithSelectedFilters(enabledFilters) {
    /**
     * Shows user's selected filters back to the user
     * They currently only show once the user has submitted the form. So they don't forget to apply filters
     * At present they make the page jump around - and I'm not sure the layout is correct
     * I can also get them to show on checkbox change, which means the page jumps around less
    */
    if (enabledFilters != null) {
        for (let i=0; i<enabledFilters.length; i++) {
            let filterName = enabledFilters[i];
            let filterNameAddPrefix = "";
            // refactor so it checks for a num type, not a length
            if (filterName.length <= 2) {
                filterNameAddPrefix = `Sleeps: ${filterName}`;
            } else {
                filterNameAddPrefix = filterName;
            }
            let filterNameFormatted = filterNameAddPrefix.toUpperCase().replace("_", " ");
            let newEl = $("<p></p>").text(filterNameFormatted).addClass("filter-tag");
            $('#selected-filters-text').append(newEl);
        };
    };
};

function removeSelectedPageFilters(enabledFilters){
    /**
     * Removes the user's selected filters from the user view
     * By setting the element text to an empty string
    */
    $('#selected-filters-text').text("");
};

function addEnabledFiltersToStorage(enabledFilters) {
    /**
     *Saves currently selected filters in local storage.
    */
    localStorage.setItem("selectedFilters", JSON.stringify(enabledFilters));
};


window.onload = function() {
    // Gets the user's selected filters from Local storage
    // Checks the appropraite checkboxes after page refreshes
    // Note this could be refactored
    let checkboxes = $("input[type=checkbox]")
    var userFilters = JSON.parse(localStorage.getItem("selectedFilters"))
    // could refactor to use Map
    for (const property in userFilters) {
        for (let i=0; i<checkboxes.length; i++) {
            if (checkboxes[i].value == userFilters[property]) {
                $(`#${checkboxes[i].id}`).prop('checked', true);
            };
        };
    };
    updatePageWithSelectedFilters(userFilters);
};

$(document).ready(function() {

    // Make empty array to store user's selected filters
    let enabledFilters = [];

    // Get all checkboxes on page. Duplicated by onload functuin
    let checkboxes = $("input[type=checkbox]")

    // Attach a change event handler to the checkboxes. Handler sourced from Stack Overflow
    checkboxes.change(function() {
        enabledFilters = checkboxes
            .filter(":checked") // Filter out unchecked boxes.
            .map(function() { // Extract values using jQuery map.
            return this.value;
            }) 
            .get() // Get array.

            addEnabledFiltersToStorage(enabledFilters);
    });

    $("#reset-filters").click(function() {
        localStorage.removeItem('selectedFilters');
        window.location.href = window.location.href;
    });

    $("#submit-form").click(function() {
        removeSelectedPageFilters(enabledFilters);
        updatePageWithSelectedFilters(enabledFilters);
    });

    // Enable tooltips - Bootstrap
    $('[data-toggle="tooltip"]').tooltip()

});

function sum(a, b) {
    return a + b;
  }
  module.exports = sum;