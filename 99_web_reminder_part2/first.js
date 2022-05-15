const panels = document.querySelectorAll( '.panel')

panels.forEach( panel => {
    panel.addEventListener('click', () => {
        panel.style.display = 'none';
    })
})
