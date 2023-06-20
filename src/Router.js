import React from 'react';
import { StyleSheet, StatusBar } from 'react-native';
import { Scene, Stack, Router, Actions } from 'react-native-router-flux';
import Login from './components/Login';
import Register from './components/Register';
import Home2 from './components/Home';


const RouterComponent = () => {
  return (
    <Router>
      <Stack hideNavBar key="root">
        <Stack
          key="auth"
          navigationBarStyle={style.navBarStyle}
          titleStyle={style.titleStyle}
          >
          <Scene
            title="Sign In"
            key="login"
            component={Login}
            initial
          />
          <Scene
            title="Register"
            key="register"
            component={Register}
          />
        </Stack>

        <Stack
            key="main"
            navigationBarStyle={style.navBarStyle}
            titleStyle={style.titleStyle}
            >
          <Scene
            title="Home"
            key="home"
            component={Home}
            initial
          />
        </Stack>
      </Stack>
    </Router>
  );
};


export default RouterComponent;

const style = StyleSheet.create({
  navBarStyle: {
    top: StatusBar.currentHeight
  },
  titleStyle: {
    flexDirection: 'row',
    width: 200
  }
});
