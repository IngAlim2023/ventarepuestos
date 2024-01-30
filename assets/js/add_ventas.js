$(document).ready(function() {
    // Evento cuando se muestra el modal de productos
    $('#exampleModal').on('shown.bs.modal', function () {
        // Inicializar DataTables en la tabla dentro del modal
        $('#myTable').DataTable({
            dom: 'Bfrtip',
            buttons: [
                { extend: 'csv' },
                { extend: 'print'},
            ]
        });
    });

    // Evento cuando se muestra el modal de clientes
    $('#Cliente').on('shown.bs.modal', function () {
        // Inicializar DataTables en la tabla dentro del modal de clientes
        $('#myTable2').DataTable({
            dom: 'Bfrtip',
            buttons: [
                { extend: 'csv' },
                { extend: 'print'},
            ]
        });
    });
});
