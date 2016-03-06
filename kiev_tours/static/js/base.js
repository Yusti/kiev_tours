// TODO refactoring
$(document).ready(function() {
    $("li>[href]").each(function() {
    if (this.href == window.location.href) {
        $(this).parent().addClass("active");
        }
    });
});
