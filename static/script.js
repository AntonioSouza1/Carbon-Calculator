document.addEventListener('DOMContentLoaded', function() {
    const selectElement = document.getElementById('finalidade');
    
    selectElement.addEventListener('change', function() {
        const form1 = document.getElementById('form1');
        const form2 = document.getElementById('form2');
        
        form1.classList.remove('mostrar');
        form2.classList.remove('mostrar');
        
        if (this.value === 'form1') {
            form1.style.display = 'block';
            form1.classList.add('mostrar');
        } else if (this.value === 'form2') {
            form2.style.display = 'block';
            form2.classList.add('mostrar');
        } else {
            form1.style.display = 'none';
            form2.style.display = 'none';
        }
    });
});
