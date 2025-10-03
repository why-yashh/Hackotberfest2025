```javascript
let arr = [];
let hasCombine = [];
let hasMove = true;
let score = 0;

function initializeGrid() {
    arr = Array(4).fill(null).map(() => Array(4).fill(0));
    hasCombine = Array(4).fill(null).map(() => Array(4).fill(false));
    let x = Math.floor(Math.random() * 4);
    let y = Math.floor(Math.random() * 4);
    arr[x][y] = 2;
}

initializeGrid();
fill();

document.addEventListener("keydown", keyPush);

document.addEventListener("click", (event) => {
    const validButtons = ['up','down','left','right'];
    if(validButtons.includes(event.target.name)) {
        let keyCode;
        switch(event.target.name) {
            case 'up': keyCode = 38; break;
            case 'down': keyCode = 40; break;
            case 'left': keyCode = 37; break;
            case 'right': keyCode = 39; break;
        }

        document.dispatchEvent(new KeyboardEvent("keydown", { keyCode }));
    }
});


function keyPush(evt) {
    hasMove = false;
    switch (evt.keyCode) {
        case 37: // Left
            moveTiles(0, 1, (i, j, c) => arr[i][j - c - 1] == 0, (i, j, c) => arr[i][j - c - 1] == arr[i][j - c], (i, j, c) => swap(i, j - c, i, j - c - 1), (i, j, c) => combine(i, j - c, i, j - c - 1));
            break;
        case 38: // Up
            moveTiles(1, 0, (i, j, c) => arr[i - c - 1][j] == 0, (i, j, c) => arr[i - c - 1][j] == arr[i - c][j], (i, j, c) => swap(i - c, j, i - c - 1, j), (i, j, c) => combine(i - c, j, i - c - 1, j));
            break;
        case 39: // Right
            moveTiles(0, -1, (i, j, c) => arr[i][j + c + 1] == 0, (i, j, c) => arr[i][j + c + 1] == arr[i][j + c], (i, j, c) => swap(i, j + c, i, j + c + 1), (i, j, c) => combine(i, j + c, i, j + c + 1));
            break;
        case 40: // Down
            moveTiles(-1, 0, (i, j, c) => arr[i + c + 1][j] == 0, (i, j, c) => arr[i + c + 1][j] == arr[i + c][j], (i, j, c) => swap(i + c, j, i + c + 1, j), (i, j, c) => combine(i + c, j, i + c + 1, j));
            break;
    }
    fill();
}

function moveTiles(iDirection, jDirection, isEmpty, canCombine, doSwap, doCombine) {
    const startI = iDirection === -1 ? 3 : 0;
    const startJ = jDirection === -1 ? 3 : 0;
    const iIncrement = iDirection === 0 ? 1 : -1;
    const jIncrement = jDirection === 0 ? 1 : -1;

    for (let i = startI; i >= 0 && i < 4; i += iIncrement) {
        for (let j = startJ; j >= 0 && j < 4; j += jIncrement) {
            let c = 0;
            while ((iDirection === 0 && j + c >= 0 && j + c < 3) || (jDirection === 0 && i + c >= 0 && i + c < 3)) {
                if (isEmpty(i, j, c)) {
                    doSwap(i, j + c * jDirection, i, j + (c + 1) * jDirection || i + c * iDirection, i + (c + 1) * iDirection);
                } else if (canCombine(i, j, c)) {
                    doCombine(i, j + c * jDirection, i, j + (c + 1) * jDirection || i + c * iDirection, i + (c + 1) * iDirection);
                }
                c++;
            }
        }
    }
}

function fill() {
    if (!isFull()) {
        if (hasMove) {
            randomXY();
        }
    } else if (isGameOver()) {
        document.getElementById("gameOver").style.display = "block";
    }

    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            const temp = document.getElementById(i + "" + j);
            temp.innerHTML = arr[i][j] !== 0 ? arr[i][j] : '';
        }
    }
    resetHasCombine();
}

function randomXY() {
    let x, y;
    do {
        x = Math.floor(Math.random() * 4);
        y = Math.floor(Math.random() * 4);
    } while (arr[x][y] !== 0);

    const z = Math.ceil(Math.random() * 10);
    arr[x][y] = z >= 7 ? 4 : 2;
}

function swap(a, b, x, y) {
    if (arr[a][b] !== 0 || arr[x][y] !== 0) {
        [arr[a][b], arr[x][y]] = [arr[x][y], arr[a][b]];
        hasMove = true;
    }
}

function combine(a, b, x, y) {
    if (!hasCombine[x][y] && !hasCombine[a][b]) {
        arr[x][y] *= 2;
        arr[a][b] = 0;
        hasCombine[x][y] = true;
        hasMove = true;
        score += arr[x][y];
        document.getElementById('num-score').innerHTML = score;
    }
}

function resetHasCombine() {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            hasCombine[i][j] = false;
        }
    }
}

function isFull() {
    return !arr.some(row => row.includes(0));
}

function isGameOver() {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            if (i > 0 && arr[i - 1][j] === arr[i][j]) return false;
            if (j > 0 && arr[i][j - 1] === arr[i][j]) return false;
            if (i < 3 && arr[i + 1][j] === arr[i][j]) return false;
            if (j < 3 && arr[i][j + 1] === arr[i][j]) return false;
        }
    }
    return true;
}

function restart() {
    initializeGrid();
    document.getElementById('gameOver').style.display = 'none';
    document.getElementById('num-score').innerHTML = score = 0;
    fill();
}

// btn-translate
let btnTranslate = document.getElementsByClassName("btn-translate")[0];

btnTranslate.onclick = () => {
    let body = document.getElementsByTagName("body")[0];

    if(body.className != "id"){
        // ID
        body.classList.add("id");

        // .how -> span
        document.querySelector('.how span').textContent = "Bagaimana cara Bermain?";
        // .how -> p
        document.querySelector('.how p').innerHTML = "Gunakan <i><u>tombol panah</u></i> Anda untuk memindahkan ubin. Ubin dengan nomor yang sama bergabung menjadi satu ketika mereka menyentuh. Tambahkan hingga mencapai <b>2048</b>!";
        // #text-score
        document.querySelector('#text-score').textContent = "Skor : ";
        // #gameOver -> span
        document.querySelector('#gameOver span').textContent = "Permainan Selesai !!";
        // #gameOver -> #reset
        document.querySelector('#gameOver #reset').textContent = "Coba Lagi";

    } else {
        // EN
        body.classList.remove("id");

        // how -> span
        document.querySelector('.how span').textContent = "How to Play?"
        // how -> p
        document.querySelector('.how p').innerHTML = "Use your <i><u>arrow keys</u></i> to move the tiles. Tiles with the same number merge into one when they touch. Add them up to reach <b>2048</b>!"
        // #text-score
        document.querySelector('#text-score').textContent = "Score : ";
        // #gameOver -> span
        document.querySelector('#gameOver span').textContent = "Game Over !!";
        // #gameOver -> #reset
        document.querySelector('#gameOver #reset').textContent = "Try Again";
    }
}
```
