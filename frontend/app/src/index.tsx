/* @refresh reload */
import { render } from 'solid-js/web'
import { Router, Routes, Route } from '@solidjs/router'
import { lazy } from "solid-js";
import { MetaProvider } from '@solidjs/meta';

import './index.css'
import NavigationBar from './components/NavigationBar'
const Home = lazy(() => import("./components/Home"));
const Catelog = lazy(() => import("./components/Catelog"));
const Production = lazy(() => import("./components/Production"));
const Sales = lazy(() => import("./components/Sales"));
const Purchasing = lazy(() => import("./components/Purchasing"));
const Recipes = lazy(() => import("./components/Recipes"));
const ProductList = lazy(() => import("./components/ProductList"));
const ProductCategoryList = lazy(() => import("./components/ProductCategoryList"));

const root = document.getElementById('root');

if (import.meta.env.DEV && !(root instanceof HTMLElement)) {
  throw new Error(
    'Root element not found. Did you forget to add it to your index.html? Or maybe the id attribute got misspelled?',
  );
}

render(() => (
    <Router>
      <header>
        <NavigationBar />
      </header>
      <main>
        <Routes>
          <Route path="/home" component={Home} />
          <Route path="/catelog" >
            <Route path="/" component={Catelog} />
            <Route path="/products" component={ProductList} />
            <Route path="/categories" component={ProductCategoryList} />
          </Route>
          <Route path="/production" component={Production} />
          <Route path="/sales" component={Sales} />
          <Route path="/purchasing" component={Purchasing} />
          <Route path="/recipes" component={Recipes} />
        </Routes>
      </main>
    </Router>
  
), root!);
