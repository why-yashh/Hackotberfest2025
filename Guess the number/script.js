

document.getElementById('reset').addEventListener('click', function() {
    randomNumber = Math.floor(Math.random() * 101);
    attempts = 0;
    document.getElementById('result').textContent = '';
    document.getElementById('guess').value = '';
    document.getElementById('submit').disabled = false;
    this.style.display = 'none';
});
