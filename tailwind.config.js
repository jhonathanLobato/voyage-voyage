/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/voyage/**/*.html'],
  theme: {
    extend: {
      colors: {
        'color-primary': '#228C6A', // algum verde
        'color-secondary': '#FF5733', // laranjão
        'color-creme': '#FFF5E1',
        'color-cinza': '#2F4F4F',
      }
    },
  },
  plugins: [],
}

