const toggleSwitch = document.querySelector('.switch input[type="checkbox"]');

toggleSwitch.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode');
});
