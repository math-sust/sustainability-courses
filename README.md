# Sustainability Resources Platform (sustainable-info)

This is the code repository for the WPI Sustainability Resources Platform website (final deliverable of WPI D20 IQP), developed by Rui Huang, Akash Shaji and Emily Baker. 

You can check out the website [Here](ryc1x.github.io/sustainable-studies/)

The repository consists of a Vue.js project, which contains the necessary code for generating the website. If you plan to maintain the development, you may find the following instructions to be helpful.  

## About the Project

This project is developed with `Vue` 2.6 and managed with `NPM`.  

- Setup
- Deployment
- Development

### Setup

#### Install Dependencies

To run the project, you first need to install necessary dependencies via `npm`:

```
npm install
```

#### Compiles and hot-reloads for development

Then you can serve the project locally:

```
npm run serve
```

(The default URL used is: http://localhost:8080/)

#### Compiles and minifies for production

You can then generate production code, containing necessary files for deploying the website. 

```
npm run build
```

(This command will generate a `dist` file under the root directory)



### Deployment

To host the website for public access, you need to host the production files under `dist` directory. We are using GitHub Pages to host this lightweight front-end webpage ([Link](ryc1x.github.io/sustainable-studies/)). You may choose to use any website hosting service though. 

#### Deployment using GitHub Pages

Please refer to this [tutorial](https://cli.vuejs.org/guide/deployment.html#gitlab-pages) for a full deployment guide.

To deploy the project, navigate to `deploy.sh`, change the file (line 20/23 specifically) accordingly and run the following command:

```
bash deploy.sh
```

Then navigate to your GitHub Pages site, the website should be deployed successfully. 



### Development

TODO



## Additional Information

### Helpful Links

https://vuejs.org/

https://cli.vuejs.org/

https://vuematerial.io/