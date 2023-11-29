import { createSignal, Show } from 'solid-js';
import { Button } from "@suid/material";
import NavigationBar from './NavigationBar'

function Home() {
  return (
    <>
      <NavigationBar />
      <div>Bake Shop</div>
    </>
  );
}

export default Home;
