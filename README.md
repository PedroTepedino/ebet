# Ebet

A bet platform focused on ESports fans.

## Instalation

### Requirements

* [**Node.js**](https://nodejs.org/en/) : The JavaScript runtime that you will use to run your frontend project.
* [**Yarn**](https://classic.yarnpkg.com/en/docs/install/#windows-stable) : A package and project manager for Node.js applications.
* [**Python**](https://www.python.org/) : A recent Python 3 interpreter to run the Flask backend on.

### Installing

Install the [**Node.js**](https://nodejs.org/en/), [**Yarn**](https://classic.yarnpkg.com/en/docs/install/#windows-stable) and  [**Python**](https://www.python.org/) on your computer putting them on the path if possible.

Afterwards clone this repo to your computer.
Open your cmd or command line on your repo.
Run the following commands:

```bash
cd api
python -m venv venv
venv\Scripts\activate
pip install flask python-dotenv
```

## Running

Open two cmd or command line instances and run the following commands.

```bash
yarn start
```

After it finishes starting run on the other cmd

```bash
yarn start-api
```

Have fun!

## Acknowledgements

This guide was writen based on this blog post:
[How To Create a React + Flask Project](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project)


## Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

==========================

# About the games

## Systems

* Fazer apostas
* Tirar apostas
* Colocar/Tirar dinehiro de usuário
* Começar/Terminar/Calcular partida **(DEV ONLY)**
* Ver estatísticas dos usuários
* Ver estatísticas dos times
* Mudar apostas durante o jogo

## Data

* Registra um time
  * id
  * Esporte
  * Odd
  * Partidas passadas
* Registrar um Esport
  * id
  * Quantidade de partidas (MDn)
* Registrar Partida
  * id
  * Dia e hora de inicio
  * Duração
  * Time A
  * Time B
* Registrar Usuário
  * id
  * Login
  * Senha
  * Quantidade de Dinheiro (Carteira)
  * partidas passadas e aposta
  * idade
* Histórico dos Resultados
  * id
  * Partida (id)
  * Resultado