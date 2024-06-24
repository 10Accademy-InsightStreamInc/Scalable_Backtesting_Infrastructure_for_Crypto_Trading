/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "white-background-primary": "#fff",
        "cta-color": "#635dff",
        "text-primary": "#2d333a",
        mediumslateblue: "#7d78ff",
        link: "#3f59e4",
        "primary-500": "#6200ee",
        border: "#c2c8d0",
        textsecondary: "#6f7780",
        "primary-color": "#007bad",
        "light-theme-background-bg": "#fbfcfe",
        "color-variants-purple-5": "#613de4",
        "wireframe-100": "#f2f4f7",
        "light-theme-border-and-divider-border-and-divider": "#cdd5e9",
        lightgray: "#d4d4d4",
        "light-theme-text-primary-body": "#111112",
        "light-theme-background-surfaces": "#f5f7fc",
      },
      spacing: {},
      fontFamily: {
        "subtitle-1": "Roboto",
        "label-base-16-24": "Inter",
        poetsenone: "PoetsenOne",
      },
      borderRadius: {
        "31xl": "50px",
      },
    },
    fontSize: {
      base: "16px",
      xs: "12px",
      "5xl": "24px",
      lgi: "19px",
      "2xs": "11px",
      "13xl": "32px",
      "7xl": "26px",
      sm: "14px",
      inherit: "inherit",
    },
    screens: {
      lg: {
        max: "1200px",
      },
      mq900: {
        raw: "screen and (max-width: 900px)",
      },
      mq750: {
        raw: "screen and (max-width: 750px)",
      },
      mq675: {
        raw: "screen and (max-width: 675px)",
      },
      mq525: {
        raw: "screen and (max-width: 525px)",
      },
      mq450: {
        raw: "screen and (max-width: 450px)",
      },
    },
  },
  corePlugins: {
    preflight: false,
  },
};
