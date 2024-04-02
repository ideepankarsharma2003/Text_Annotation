const canvas = document.getElementById('myCanvas');
const context = canvas.getContext('2d');

// Game properties
const carWidth = 40;
const carHeight = 30;
const trackWidth = canvas.width;
const trackHeight = canvas.height;
const cars = [];
let isGameOver = false;

function init() {
    cars.push({
        x: 0,
        y: trackHeight - carHeight,
        speed: 2,
        direction: 'right'
    });

    addListener();
}

function addListener() {
    canvas.addEventListener('click', function(event) {
        if (!isGameOver) {
            cars.push({
                x: event.offsetX - carWidth / 2,
                y: trackHeight - carHeight,
                speed: 2,
                direction: getRandomDirection()
            });
        }
    });

    document.getElementById('restartBtn').addEventListener('click', restartGame);
}

function animate() {
    if (!isGameOver) {
        context.clearRect(0, 0, canvas.width, canvas.height);
        updateCars();
        drawTrack();
        drawCars();
    } else {
        context.font = '24px Arial';
        context.fillText('Game Over!', canvas.width / 2 - 40, canvas.height / 2);
    }

    requestAnimationFrame(animate);
}

function updateCars() {
    for (let i = 0; i < cars.length; i++) {
        const car = cars[i];
        car.y -= car.speed;

        if (car.y < 0) {
            car.y = trackHeight;
            car.direction = reverseDirection(car.direction);
        }

        if (car.x < 0 || car.x > trackWidth) {
            isGameOver = true;
        }
    }
}

function drawTrack() {
    context.beginPath();
    context.moveTo(0, trackHeight / 2);
    context.lineTo(trackWidth, trackHeight / 2);
    context.arc(trackWidth / 2, trackHeight / 2, trackHeight / 4, 0, 2 * Math.PI);
    context.fillStyle = '#2ecc71';
    context.fill();
    context.stroke();
}

function drawCars() {
    for (let i = 0; i < cars.length; i++) {
        const car = cars[i];
        context.fillStyle = '#ff0000';
        context.fillRect(car.x, car.y, carWidth, carHeight);
    }
}

function getRandomDirection() {
    const directions = ['right', 'left'];
    return directions[Math.floor(Math.random() * directions.length)];
}

function reverseDirection(dir) {
    return dir === 'right' ? 'left' : 'right';
}

function restartGame() {
    location.reload();
}

init();
animate();
