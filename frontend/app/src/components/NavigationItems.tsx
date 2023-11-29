import MailIcon from "@suid/icons-material/Mail";
import InboxIcon from "@suid/icons-material/MoveToInbox";
import {
  Divider,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from '@suid/material';
import { Setter, createResource, For } from 'solid-js';
import { appList } from '../lib/config';


type NavigationItemsProps = {
  activeItemSetter: Setter<string>
}

export function NavigationItems(props: NavigationItemsProps) {
  
  const [data] = createResource(appList);
  console.log(data());
  console.log(data.error);
  
  return (
    <>
      <List>
        <For each={data()}>
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