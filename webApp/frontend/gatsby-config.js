module.exports = {
  siteMetadata: {
    title: `Trading Bot Club`,
    siteUrl: `https://www.yourdomain.tld`
  },
  plugins: ["gatsby-plugin-styled-components", 'gatsby-plugin-postcss', "gatsby-plugin-image", "gatsby-plugin-sitemap", {
    resolve: 'gatsby-plugin-manifest',
    options: {
      "icon": "src/images/logo.png"
    }
  }, "gatsby-plugin-mdx", "gatsby-plugin-sharp", "gatsby-transformer-sharp", {
      resolve: 'gatsby-source-filesystem',
      options: {
        "name": "images",
        "path": "./src/images/"
      },
      __key: "images"
    }, {
      resolve: 'gatsby-source-filesystem',
      options: {
        "name": "pages",
        "path": "./src/pages/"
      },
      __key: "pages"
    }]
};