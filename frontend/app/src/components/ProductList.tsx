import { createSignal, Show , createResource, For, createMemo } from 'solid-js'
import { 
  Button, 
  Box, 
  Card, 
  CardHeader, 
  CardContent, 
  CardMedia,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  TableContainer 
} from "@suid/material"
import { productList, product } from '../lib/catelog'
import SearchBox from './SearchBox'
import { Title, MetaProvider } from "@solidjs/meta";

import { createTheme, ThemeProvider } from "@suid/material/styles";

const theme = createTheme({
  components: {
    MuiTableCell: {
      defaultProps: {
        color: "grey"
      }
    }
  }
});

function filter_products(products: product[] | undefined, filter: string): product[] {
  const words = filter.split(' ')
  const filtered: product[] = []
  products?.forEach((prod, index) => {
    let matches: number = 0
    words.forEach((word, index) => {
      if (prod.name.toLowerCase().includes(word.toLowerCase())) {
        matches += 1
      }
    })
    if (matches == words.length) {
      filtered.push(prod)
    }
  })
  return filtered
}

function ProductList() {
  const [products] = createResource(productList)
  const [getFilterString, setFilterString] = createSignal('')
  const filteredProducts = createMemo(() => filter_products(products()?.results, getFilterString()))

  return (
    <>
      <Box sx={{m:2}}>
        <SearchBox placeHolder="Search Products" filterSetter={setFilterString}/>
        <h2>Products</h2>
        <Box sx={{display: 'flex', flexWrap: 'wrap'}} >
          <Show when={!products.loading} fallback={"Loading..."}>
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell component={"th"}>Name</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                <For each={filteredProducts()} fallback={<TableRow><TableCell>None</TableCell></TableRow>}>
                  {
                    (product, index) =>
                      <TableRow>
                        <TableCell>{product.name}</TableCell>
                      </TableRow> 
                  }
                </For>
              </TableBody>
            </Table>
          </TableContainer>
            
          </Show>
        </Box>
      </Box>
    </>
  )
}

export default ProductList;
