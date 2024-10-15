const canvas = document.getElementById('sketchCanvas');
const ctx = canvas.getContext('2d');
let drawing = false;

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

function startDrawing(e) {
  drawing = true;
  draw(e); // Draw the initial point
}

function draw(e) {
  if (!drawing) return;
  
  ctx.lineWidth = 2;
  ctx.lineCap = 'round';
  ctx.strokeStyle = '#000';

  ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

function stopDrawing() {
  drawing = false;
  ctx.beginPath(); // Reset the path
}

document.getElementById('clearCanvas').addEventListener('click', function() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});

document.getElementById('saveSketch').addEventListener('click', function() {
  const link = document.createElement('a');
  link.download = 'sketch.png';
  link.href = canvas.toDataURL();
  link.click();
});
