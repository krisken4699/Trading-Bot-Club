/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ['class', '[data-mode="dark"]'],
  content: [
    "./src/pages/**/*.{js,jsx,ts,tsx}",
    "./src/components/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'Metric-Thin': "Metric-Thin",
        'Metric-Light': "Metric-Light",
        'Metric-Regular': "Metric-Regular",
        'Metric-Medium': "Metric-Medium",
        'Metric-SemiBold': "Metric-SemiBold",
        'Metric-Black': "Metric-Black",
        'A1':"Gothic A1"
        // 'A1-Thin': "A1-Thin",
        // 'A1-ExtraLight': "A1-ExtraLight",
        // 'A1-Light': "A1-Light",
        // 'A1-Regular': "A1-Regular",
        // 'A1-Medium': "A1-Medium",
        // 'A1-SemiBold': "A1-SemiBold",
        // 'A1-Bold': "A1-Bold",
        // 'A1-ExtraBold': "A1-ExtraBold",
        // 'A1-Black': "A1-Black",
      },
      colors: {
        "black": '#0b0b0d',
        'primary':'#0b0b0d',
        'secondary':'#aaaaaa',
        'tertiary':'#181619',
        'quaternary':'#181b22',
        'accent1':'#272a31',
        'accent2':'#a76b09',
        'accent3':'#dda74f',
        'gold1':'#a76b09',
        'gold2':'#dda74f',
        'gray': {
          '450': '#858585',
          '350': '#ADADAD'
        },
        'AA0000': '#AA0000',
        'C4C4C4': '#C4C4C4',
        'F0F0F0': '#F0F0F0',
        'F9C74F': '#F9C74F',
        'F7F5F2': '#F7F5F2',
        'EFEFEF': '#EFEFEF',
        'A29F9A': '#A29F9A',
        '1C1D1D': '#1C1D1D',
        '666666': '#666666',
        'E8E8E1': '#E8E8E1',
        'DDDDDD': '#DDDDDD',
        'EDF4FD': '#EDF4FD',
        'EDEDED': '#EDEDED',
        '113D8B': '#113D8B',
        '111111': '#111111',
        'D9D9D9': '#D9D9D9',
        '0A122A': '#0A122A',
        '3075EC': '#3075EC',
      }
    },
  },
  variants: {
    extend: {
      borderRadius: ['hover', 'focus'],
      cursor: ['hover', 'focus'],
      borderWidth: ['hover', 'focus', 'responsive'],
      gradientColorStops: ['active', 'group-hover', 'hover'],
      backgroundColor: ['active'],
    },
  },
  plugins: [],
}
