import MenuIcon from "@suid/icons-material/Menu";
import { 
  AppBar,
  Box,
  Button,
  IconButton,
  Toolbar,
  Typography, 
  Drawer,

} from "@suid/material"
import { createSignal } from 'solid-js'
import { NavigationItems } from './NavigationItems';

export default function NavigationBar() {
  const [openMenu, setOpenMenu] = createSignal(false);
  const [activeItem, setActiveItem] = createSignal<string>("Home");

  const toggleDrawer =
    (isOpen: boolean) => (event: MouseEvent | KeyboardEvent) => {
      if (event.type === "keydown") {
        const keyboardEvent = event as KeyboardEvent;
        if (keyboardEvent.key === "Tab" || keyboardEvent.key === "Shift")
          return;
      }
      setOpenMenu(isOpen);
  };

  const menuItems = () => (
    <Box
      sx={{ width: 250 }}
      role="presentation"
      // onClick={toggleDrawer(false)}
      onKeyDown={toggleDrawer(false)}
    >
      <NavigationItems activeItemSetter={setActiveItem} toggleDrawerSetter={setOpenMenu} />
    </Box>
  );

  return (
    <>
      <Drawer
        anchor="left"
        open={openMenu()}
        sx={{ zIndex: 9999 }}
        onClose={toggleDrawer(false)}
      >
        {menuItems()}
      </Drawer>
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="fixed">
          <Toolbar>
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
              onClick={toggleDrawer(true)}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              {activeItem()}
            </Typography>
            <Button color="inherit">Login</Button>
          </Toolbar>
        </AppBar>
      </Box>
    </>
  )
}