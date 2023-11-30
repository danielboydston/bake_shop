import MailIcon from "@suid/icons-material/Mail";
import InboxIcon from "@suid/icons-material/MoveToInbox";
import {
  Divider,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from '@suid/material';
import { Setter, createResource, For, Show } from 'solid-js';
import { companyName } from '../lib/config';


type NavigationItemsProps = {
  activeItemSetter: Setter<string>
}

export function NavigationItems(props: NavigationItemsProps) {
  
  const [company] = createResource(companyName);
  
  return (
    <>
    
      
      <Typography variant="h6" gutterBottom>
        <Show when={!company.loading} fallback={"The Bake Shop"}>
          {company()[0].value}
        </Show>
      </Typography>
     
      <List>
        <Divider />
          <For each={["Catelog", "Production", "Purchasing", "Recipe", "Sales"]}>
            {(item) => (
              <ListItem disablePadding>
                <ListItemButton onClick={() => props.activeItemSetter(item)}>
                  <ListItemIcon>
                    <InboxIcon />
                  </ListItemIcon>
                  <ListItemText primary={item} />
                </ListItemButton>
              </ListItem>
            )}
          </For>
      </List>
      <Divider />
    </>
  )
}