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

    await listproductos();

    dataTable = $('#datos').DataTable({});

    dataTableIsInitialized = true;
};

const listproductos= async() => {
    try {
        const response = await fetch("/list_productos/");
        const data = await response.json();

        let content=``;
        data.productos.forEach((productos,index)=>{
            content+=`
                <tr>
                    <td>${productos.id}</td>
                    <td>${productos.descripcion}</td>
                    <td class="field-imagen"><img src="http://127.0.0.1:8000/media/${productos.imagen}" alt="Imagen del producto" style="max-width: 100px; max-height: 100px;"></td>
                    <td>${productos.costo}</td>
                    <td>${productos.ubicacion}</td>
                    <td>${productos.cantidad}</td>
                    <td>${productos.created}</td>
                    <td>${productos.modified}</td>
                </tr>
            `;
        });
        tableBody_productos.innerHTML = content;
    } catch(ex) {
        alert(ex);
    }
};
window.addEventListener('load', async()=>{
    await initDataTable();
});