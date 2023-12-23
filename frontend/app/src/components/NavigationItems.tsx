import MonetizationOnIcon from '@suid/icons-material/MonetizationOn';
import LocalShippingIcon from '@suid/icons-material/LocalShipping';
import FactoryIcon from '@suid/icons-material/Factory';
import MenuBookIcon from '@suid/icons-material/MenuBook';
import HomeIcon from '@suid/icons-material/Home';
import BakeryDiningIcon from '@suid/icons-material/BakeryDining';
import CategoryIcon from '@suid/icons-material/Category';
import ShoppingCartIcon from '@suid/icons-material/ShoppingCart';
import StoreIcon from '@suid/icons-material/Store';
import GroupWorkIcon from '@suid/icons-material/GroupWork';
import PeopleAltIcon from '@suid/icons-material/PeopleAlt';
import PointOfSaleIcon from '@suid/icons-material/PointOfSale';
import CakeIcon from '@suid/icons-material/Cake';
import { ExpandLess, ExpandMore } from "@suid/icons-material";
import {
  Divider,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
  Icon,
} from '@suid/material';
import { Setter, createResource, For, Show, JSX, createSignal } from 'solid-js';
import { companyName } from '../lib/config';
import { A } from '@solidjs/router'
import RecipeIconSVG from '../assets/recipe_icon.svg'

type NavigationItemsProps = {
  activeItemSetter: Setter<string>
  toggleDrawerSetter: Setter<boolean>
}

type NavigationItemProps = {
  activeItemSetter: Setter<string>,
  toggleDrawerSetter: Setter<boolean>,
  icon: JSX.Element,
  title: string,
  url: string,
  children: NavigationItemProps[]
}

export const RecipeIcon = () => (
  <Icon>
    <img src={RecipeIconSVG} height={25} width={25} />
  </Icon>
)

export function NavigationSingleLevel(props: NavigationItemProps) {
  
  return (
    <ListItem disablePadding>
      <ListItemButton>
        <A href={props.url} onClick = { () => {
            props.activeItemSetter(props.title);
            props.toggleDrawerSetter(false);
          }} style={`all: inherit; padding: 0;`} >
          <ListItemIcon>
            {props.icon}
          </ListItemIcon>
          <ListItemText primary={props.title} />
        </A>
      </ListItemButton>
    </ListItem>
  )
}

export function NavigationMultiLevel(props: NavigationItemProps) {
  const [open, setOpen] = createSignal(false);

  const handleClick = () => {
    setOpen((prev) => !prev);
  }

  return (
    <>
      <ListItem disablePadding>
        <ListItemButton onClick={handleClick}>
          
          <ListItemIcon>
            {props.icon}
          </ListItemIcon>
          <ListItemText primary={props.title} />
          {open() ? <ExpandLess /> : <ExpandMore />}
        </ListItemButton>
      </ListItem>
      { open() && 
        <List disablePadding sx={{ pl: 2 }}>
          <For each={props.children} > 
            {(child, i) => 
              <NavigationSingleLevel {...child} />
            }

          </For>
        </List>
      }
    </>
  )
}

export function NavigationItem(props: NavigationItemProps) {
  let component = (<NavigationSingleLevel {...props} />)
  if (props.children.length > 0) {
    component = (<NavigationMultiLevel {...props} />)
  }
  return component
}

export function NavigationItems(props: NavigationItemsProps) {
  
  const [company] = createResource(companyName);

  const menu: NavigationItemProps[] = [
    {
      activeItemSetter: props.activeItemSetter,
      toggleDrawerSetter: props.toggleDrawerSetter,
      title: "Home",
      url: "/home",
      icon: <HomeIcon/>,
      children: []
    },
    {
      activeItemSetter: props.activeItemSetter,
      toggleDrawerSetter: props.toggleDrawerSetter,
      title: "Catelog",
      url: "/catelog",
      icon: <MenuBookIcon/>,
      children: [
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Categories",
          url: "/catelog/categories",
          icon: <CategoryIcon/>,
          children: []
        },
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Products",
          url: "/catelog/products",
          icon: <BakeryDiningIcon/>,
          children: []
        },
      ]
    },
    {
      activeItemSetter: props.activeItemSetter,
      toggleDrawerSetter: props.toggleDrawerSetter,
      title: "Production",
      url: "/production",
      icon: <FactoryIcon/>,
      children: []
    },
    {
      activeItemSetter: props.activeItemSetter,
      toggleDrawerSetter: props.toggleDrawerSetter,
      title: "Purchasing",
      url: "/purchasing",
      icon: <LocalShippingIcon/>,
      children: [
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Purchase Orders",
          url: "/purchasing/po",
          icon: <ShoppingCartIcon/>,
          children: []
        },
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Vendors",
          url: "/purchasing/vendors",
          icon: <StoreIcon/>,
          children: []
        },
      ]
    },
    {
      activeItemSetter: props.activeItemSetter,
      toggleDrawerSetter: props.toggleDrawerSetter,
      title: "Baking",
      url: "/baking",
      icon: <CakeIcon/>,
      children: [
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Ingredients",
          url: "/baking/ingredients",
          icon: <GroupWorkIcon/>,
          children: []
        },
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Ingredient Categories",
          url: "/baking/ingredient-categories",
          icon: <CategoryIcon/>,
          children: []
        },
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Recipes",
          url: "/baking/recipes",
          icon: <RecipeIcon/>,
          children: []
        },
      ]
    },
    {
      activeItemSetter: props.activeItemSetter,
      toggleDrawerSetter: props.toggleDrawerSetter,
      title: "Sales",
      url: "/sales",
      icon: <MonetizationOnIcon/>,
      children: [
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Customers",
          url: "/sales/customers",
          icon: <PeopleAltIcon/>,
          children: []
        },
        {
          activeItemSetter: props.activeItemSetter,
          toggleDrawerSetter: props.toggleDrawerSetter,
          title: "Orders",
          url: "/sales/orders",
          icon: <PointOfSaleIcon/>,
          children: []
        },
      ]
    },
  ]
  
  return (
    <>
    
      
      <Typography variant="h6" gutterBottom>
        <Show when={!company.loading} fallback={"The Bake Shop"}>
          {company()[0].value}
        </Show>
      </Typography>
     
      <List>
        <Divider />
        <For each={menu} > 
            {(child, i) => 
              <NavigationItem 
                {...child} />
            }

        </For>
               
      </List>
      <Divider />
    </>
  )
}