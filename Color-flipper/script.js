const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];
const btn = document.getElementById("btn");
const colorDisplay = document.querySelector(".color");

if (!btn || !colorDisplay) {
  console.error("Required elements not found: #btn or .color");
} else if (!Array.isArray(colors) || colors.length === 0) {
  console.error("Colors array is empty or invalid.");
} else {
  // Set initial color display
  colorDisplay.textContent = colors[0];

  const applyRandomColor = () => {
    const idx = getRandomNumber(colors.length);
    const value = colors[idx];
    document.body.style.backgroundColor = value;
    colorDisplay.textContent = value;
  };

  btn.addEventListener("click", applyRandomColor);

  // Keyboard accessibility: Enter or Space triggers color change when button focused
  btn.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      applyRandomColor();
    }
  });

  // Optional: click the color text to copy value to clipboard
  colorDisplay.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(colorDisplay.textContent);
      // brief feedback (could be replaced with a tooltip)
      const original = colorDisplay.textContent;
      colorDisplay.textContent = "Copied!";
      setTimeout(() => (colorDisplay.textContent = original), 1000);
    } catch (err) {
      console.error("Copy failed", err);
    }
  });
}

function getRandomNumber(max) {
  return Math.floor(Math.random() * max);
}
