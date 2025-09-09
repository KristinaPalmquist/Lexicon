/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./pages/**/*.{html,js,py}",
  ],
  theme: {
    extend: {
      colors: {
        hotpink: "#ff1493",
        lightpink: "#ffe4f0",
        brightyellow: "#ffed00",
      },
    },
  },
  plugins: [],
};
