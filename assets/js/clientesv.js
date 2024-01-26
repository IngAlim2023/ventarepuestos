let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [3] },
        { searchable: false, targets: [0] }
    ],
    pageLength: 15,
    destroy: true

};

const initDataTable= async()=>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await listclientes();

    dataTable = $('#datos').DataTable({});

    dataTableIsInitialized = true;
};

const listclientes= async() => {
    try {
        const response = await fetch("/list_clientes/");
        const data = await response.json();

        let content=``;
        data.clientes.forEach((clientes,index)=>{
            content+=`
                <tr>
                    <td>${clientes.id}</td>
                    <td>${clientes.nombre}</td>
                    <td>${clientes.apellido}</td>
                    <td>${clientes.identification}</td>
                    <td>${clientes.address}</td>
                    <td>${clientes.phone}</td>
                    <td>${clientes.created}</td>
                    <td>${clientes.modified}</td>
                </tr>
            `;
        });
        tableBody_clientes.innerHTML = content;
    } catch(ex) {
        alert(ex);
    }
};
window.addEventListener('load', async()=>{
    await initDataTable();
});