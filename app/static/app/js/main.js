Swal.fire({
    title: '¿Estás seguro?',
    text: "Se quitará el producto de tu carrito",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'Cancelar',
    confirmButtonText: 'Quitar'
}).then((result) => {
    if (result.isConfirmed) {
        Swal.fire(
            '¡Quitado!',
            'Se ha quitado el producto de tu carrito',
            'success'
        )
    }
})