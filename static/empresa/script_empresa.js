//apresenta o formulário de acordo com o que for selecionado
document.addEventListener('DOMContentLoaded', function() {
    const ramo = document.getElementById('ramo_empresa');
    const producao = document.getElementById('producao');
    const agro = document.getElementById('agro')

//apresenta o formulário conforme o ramo selecionado
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
        tx_qtGasolina.style.display = 'none';
        qtGasolina.style.display = 'none';
    }
}
//Função oculta campo etanol, aparece quando selecionado
function toggleEtanol() {
    const checkEtanol = document.getElementById('checkEtanol');
    const etanol = document.getElementById('etanol');
    const txEtanol = document.getElementById('txEtanol')
    const tx_qtEtanol = document.getElementById('tx_qtEtanol')
    const qtEtanol = document.getElementById('qtEtanol')

    etanol.classList.remove('mostrar');
    txEtanol.classList.remove('mostrar');
    tx_qtEtanol.classList.remove('mostrar')
    qtEtanol.classList.remove('mostrar')

    if (checkEtanol.checked) {
        etanol.style.display = 'block';
        txEtanol.style.display = 'block';
        tx_qtEtanol.style.display = 'block';
        qtEtanol.style.display = 'block';
    } else {
        etanol.style.display = 'none';
        txEtanol.style.display = 'none';
        tx_qtEtanol.style.display = 'none';
        qtEtanol.style.display = 'none';
    }
}
//Função oculta campo diesel, aparece quando selecionado
function toggleDiesel() {
    const checkDiesel = document.getElementById('checkDiesel');
    const diesel = document.getElementById('diesel');
    const txDiesel = document.getElementById('txDiesel')
    const tx_qtDiesel = document.getElementById('tx_qtDiesel');
    const qtDiesel = document.getElementById('qtDiesel');

    diesel.classList.remove('mostrar');
    txDiesel.classList.remove('mostrar');
    tx_qtDiesel.classList.remove('mostrar')
    qtDiesel.classList.remove('mostrar');

    if (checkDiesel.checked) {
        diesel.style.display = 'block';
        txDiesel.style.display = 'block';
        tx_qtDiesel.style.display = 'block';
        qtDiesel.style.display = 'block'
    } else {
        diesel.style.display = 'none';
        txDiesel.style.display = 'none';
        tx_qtDiesel.style.display = 'none';
        qtDiesel.style.display = 'none';
    }
}
//Função oculta campo biodiesel, aparece quando selecionado
function toggleBiodiesel() {
    const checkBiodiesel = document.getElementById('checkBiodiesel');
    const biodiesel = document.getElementById('biodiesel');
    const txBiodiesel = document.getElementById('txBiodiesel');
    const tx_qtBiodiesel = document.getElementById('tx_qtBiodiesel');
    const qtBiodiesel = document.getElementById('qtBiodiesel');

    biodiesel.classList.remove('mostrar');
    txBiodiesel.classList.remove('mostrar');
    tx_qtBiodiesel.classList.remove('mostrar');
    qtBiodiesel.classList.remove('mostrar');

    if (checkBiodiesel.checked) {
        biodiesel.style.display = 'block';
        txBiodiesel.style.display = 'block';
        tx_qtBiodiesel.style.display = 'block';
        qtBiodiesel.style.display = 'block';
    } else {
        biodiesel.style.display = 'none';
        txBiodiesel.style.display = 'none';
        tx_qtBiodiesel.style.display = 'none';
        qtBiodiesel.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', function() {
    toggleGasolina();
    toggleEtanol();
    toggleDiesel();
    toggleBiodiesel();
});
