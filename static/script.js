//função de relógio
function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById('clock').textContent = timeString;
}

// Atualiza o relógio a cada segundo
setInterval(updateClock, 1000);
// Chama a função uma vez para não ficar esperando 1 segundo para aparecer
updateClock();

//apresenta o formulário de acorno com o que for selecionado
document.addEventListener('DOMContentLoaded', function() {
    const selectElement = document.getElementById('finalidade');
    const form1 = document.getElementById('form1');
    const form2 = document.getElementById('form2');
    const ramo = document.getElementById('ramo_empresa');
    const producao = document.getElementById('producao');
    const agro = document.getElementById('agro')

//apresenta o formulário de acorno com a finalidade selecionado
    selectElement.addEventListener('change', function() {
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
//apresenta o formulário de acorno com o ramo selecionado
    ramo.addEventListener('change', function() {

        agro.classList.remove('mostrar');
        producao.classList.remove('mostrar');

        agro.style.display = 'none';
        producao.style.display = 'none';

        if (this.value === '1') {
            agro.style.display = 'block';
            agro.classList.add('mostrar');
        } else if (this.value === '2') {
            producao.style.display = 'block';
            producao.classList.add('mostrar');
        } else {
            producao.style.display = 'none';
            agro.style.display = 'none';
        }
    });
})

//Função oculta campo gasolina, aparece quando selecionado
function toggleGasolina() {
    const checkGasolina = document.getElementById('checkGasolina');
    const gasolina = document.getElementById('gasolina');
    const txGasolina = document.getElementById('txGasolina');
    const tx_qtGasolina = document.getElementById('tx_qtGasolina');
    const qtGasolina = document.getElementById('qtGasolina');

    gasolina.classList.remove('mostrar');
    txGasolina.classList.remove('mostrar');
    tx_qtGasolina.classList.remove('mostrar');
    qtGasolina.classList.remove('mostrar');

    if (checkGasolina.checked) {
        gasolina.style.display = 'block';
        txGasolina.style.display = 'block';
        tx_qtGasolina.style.display = 'block';
        qtGasolina.style.display = 'block';
    } else {
        gasolina.style.display = 'none';
        txGasolina.style.display = 'none';
        tx_qtGasolina.display = 'none';
        qtGasolina.style.display = 'none';
    }
}
//Função oculta campo etanol, aparece quando selecionado
function toggleEtanol() {
    const checkEtanol = document.getElementById('checkEtanol');
    const etanol = document.getElementById('etanol');
    const txEtanol = document.getElementById('txEtanol')

    etanol.classList.remove('mostrar');
    txEtanol.classList.remove('mostrar');

    if (checkEtanol.checked) {
        etanol.style.display = 'block';
        txEtanol.style.display = 'block';
    } else {
        etanol.style.display = 'none';
        txEtanol.style.display = 'none';
    }
}
//Função oculta campo diesel, aparece quando selecionado
function toggleDiesel() {
    const checkEtanol = document.getElementById('checkDiesel');
    const diesel = document.getElementById('diesel');
    const txDiesel = document.getElementById('txDiesel')

    diesel.classList.remove('mostrar');
    txDiesel.classList.remove('mostrar');

    if (checkDiesel.checked) {
        diesel.style.display = 'block';
        txDiesel.style.display = 'block';
    } else {
        diesel.style.display = 'none';
        txDiesel.style.display = 'none';
    }
}
//Função oculta campo biodiesel, aparece quando selecionado
function toggleBiodiesel() {
    const checkBiodiesel = document.getElementById('checkBiodiesel');
    const biodiesel = document.getElementById('biodiesel');
    const txBiodiesel = document.getElementById('txBiodiesel')

    biodiesel.classList.remove('mostrar');
    txBiodiesel.classList.remove('mostrar');

    if (checkBiodiesel.checked) {
        biodiesel.style.display = 'block';
        txBiodiesel.style.display = 'block';
    } else {
        biodiesel.style.display = 'none';
        txBiodiesel.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', function() {
    toggleGasolina();
    toggleEtanol();
    toggleDiesel();
    toggleBiodiesel();
});
