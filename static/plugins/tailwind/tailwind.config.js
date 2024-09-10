tailwind.config = {
  content: ["/css/font.css"],
  theme: {
    screens:{
      xs: '480px',
      sm:'640px',
      md:'768px',
      lg:'1024px',
      xl:'1280px',
      '2xl':'1580px',
    },
    container: {
      padding: {
        DEFAULT: '20px',
      },
      center: 'true',
    },
    extend: {
      gridTemplateColumns: {
        '16': 'repeat(16, minmax(0, 1fr))',
        '18': 'repeat(18, minmax(0, 1fr))',
      },
      gridColumn: {
        'span-13': 'span 13 / span 13',
      },
      fontFamily: {
        inter: "inter",
        mulish : "mulish",
      },
      colors: {
        darkBlue:"#232D37",
        footerBg: "#232D37E6",
        textColor:"#333333",
      },
    },
  },
};
