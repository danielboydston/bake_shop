import MailIcon from "@suid/icons-material/Mail";
import InboxIcon from "@suid/icons-material/MoveToInbox";
import {
  Box,
  Button,
  Divider,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from "@suid/material";
import { DrawerProps } from "@suid/material/Drawer";
import { createSignal } from "solid-js";


type NavigationMenuProps = {
  isOpen: boolean
}

export default function NavigationMenu(props: NavigationMenuProps) {
  const [open, setOpen] = createSignal(props.isOpen);

  const toggleDrawer =
    (isOpen: boolean) => (event: MouseEvent | KeyboardEvent) => {
      if (event.type === "keydown") {
        const keyboardEvent = event as KeyboardEvent;
        if (keyboardEvent.key === "Tab" || keyboardEvent.key === "Shift")
          return;
      }
      setOpen(isOpen);
    };


  const list = () => (
    <Box
      sx={{ width: 250 }}
      role="presentation"
      onClick={toggleDrawer(false)}
      onKeyDown={toggleDrawer(false)}
    >
      <List>
        {["Catelog", "Production", "Sales", "Purchasing", "Recipes"].map((text, index) => (
          <ListItem disablePadding>
            <ListItemButton>
              <ListItemIcon>
                {index % 2 === 0 ? <InboxIcon /> : <MailIcon />}
              </ListItemIcon>
              <ListItemText primary={text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
      <Divider />
    </Box>
  );

  return (
    <Drawer
      anchor="left"
      open={open()}
      sx={{ zIndex: 9999 }}
      onClose={toggleDrawer(false)}
    >
      {list()}
    </Drawer>
  );
}
