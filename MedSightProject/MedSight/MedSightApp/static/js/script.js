$(document).ready(function() {
    $('#patients').DataTable({
        "lengthMenu": [[5, 10, 15, -1], [5, 10, 15, "All"]]
    });
} );
$(document).ready(function() {
    $('#doctors').DataTable({
        "lengthMenu": [[5, 10, 15, -1], [5, 10, 15, "All"]]
    });
} );